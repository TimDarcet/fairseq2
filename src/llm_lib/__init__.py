# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import annotations

from collections.abc import Callable

import llm_lib2n  # Report any llm_lib2n initialization error eagerly.

import llm_lib2.runtime.dependency
from llm_lib2.error import InvalidOperationError
from llm_lib2.runtime.dependency import DependencyContainer, DependencyResolver

__version__ = "0.8.0.dev0"


_in_call: bool = False


def init_llm_lib2(
    *,
    extras: Callable[[DependencyContainer], None] | None = None,
    no_progress: bool | None = None,
) -> DependencyResolver:
    """
    If ``no_progress`` is ``True``, all progress bars will be disabled. If
    ``None``, ``llm_lib2_NO_PROGRESS`` environment variable will be checked
    instead and progress bars will be disabled if it exists.
    """
    from llm_lib2.composition import _register_library

    global _in_call

    if llm_lib2.runtime.dependency._resolver is not None:
        raise InvalidOperationError("`init_llm_lib2()` is already called.")

    if _in_call:
        raise InvalidOperationError("`init_llm_lib2()` cannot be called recursively.")

    _in_call = True

    container = DependencyContainer()

    try:
        _register_library(container, no_progress=no_progress)

        if extras is not None:
            extras(container)
    finally:
        _in_call = False

    llm_lib2.runtime.dependency._resolver = container

    return container
