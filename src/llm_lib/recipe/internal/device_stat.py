# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import annotations

from typing import final

from llm_lib2.gang import Gangs
from llm_lib2.recipe.error import DeviceTypeNotSupportedError
from llm_lib2.runtime.lookup import Lookup
from llm_lib2.utils.device_stat import NOOP_DEVICE_STAT_TRACKER, DeviceStatTracker


@final
class _DeviceStatTrackerProvider:
    def __init__(self, gangs: Gangs, trackers: Lookup[DeviceStatTracker]) -> None:
        self._gangs = gangs
        self._trackers = trackers

    def get(self) -> DeviceStatTracker:
        gang = self._gangs.root

        if gang.rank == 0:
            tracker = self._trackers.maybe_get(gang.device.type)
            if tracker is None:
                raise DeviceTypeNotSupportedError(gang.device)

            return tracker

        return NOOP_DEVICE_STAT_TRACKER
