# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import annotations

from llm_lib2.data.tokenizers import TokenizerHubAccessor
from llm_lib2.models import ModelHubAccessor
from llm_lib2.models.nllb.config import NLLB_FAMILY, NllbConfig
from llm_lib2.models.nllb.tokenizer import NllbTokenizer, NllbTokenizerConfig
from llm_lib2.models.transformer import TransformerModel

get_nllb_model_hub = ModelHubAccessor(
    NLLB_FAMILY, kls=TransformerModel, config_kls=NllbConfig
)

get_nllb_tokenizer_hub = TokenizerHubAccessor(
    NLLB_FAMILY, kls=NllbTokenizer, config_kls=NllbTokenizerConfig
)
