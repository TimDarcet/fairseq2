# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import annotations

from llm_lib2.models import ModelHubAccessor
from llm_lib2.models.jepa.config import JEPA_FAMILY, JepaConfig
from llm_lib2.models.jepa.model import JepaModel

get_jepa_model_hub = ModelHubAccessor(JEPA_FAMILY, JepaModel, JepaConfig)
