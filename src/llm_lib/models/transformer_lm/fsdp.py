# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import annotations

from torch.nn import Module

from llm_lib2.error import NotSupportedError
from llm_lib2.models.transformer_lm.model import TransformerLM
from llm_lib2.models.utils.fsdp import apply_layerwise_fsdp
from llm_lib2.nn.fsdp import FSDPWrapper


def apply_fsdp_to_transformer_lm(
    model: TransformerLM, granularity: str, wrapper: FSDPWrapper
) -> Module:
    if granularity == "layer":
        apply_layerwise_fsdp(model.decoder.layers, wrapper)

        return model

    if granularity == "stack":
        wrapped_decoder = wrapper(model.decoder)

        model.register_module("decoder", wrapped_decoder)

        return model

    raise NotSupportedError(
        f"`granularity` must be a supported granularity, but is {granularity} instead."
    )
