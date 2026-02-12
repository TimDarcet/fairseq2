# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import annotations

from llm_lib2.models.transformer.ac import (
    apply_ac_to_transformer as apply_ac_to_transformer,
)
from llm_lib2.models.transformer.attention_bias import (
    ALiBiAttentionBias as ALiBiAttentionBias,
)
from llm_lib2.models.transformer.attention_bias import AttentionBias as AttentionBias
from llm_lib2.models.transformer.attention_bias import (
    AttentionBiasCache as AttentionBiasCache,
)
from llm_lib2.models.transformer.attention_bias import (
    CausalAttentionBias as CausalAttentionBias,
)
from llm_lib2.models.transformer.attention_bias import (
    ChunkedAttentionBias as ChunkedAttentionBias,
)
from llm_lib2.models.transformer.attention_bias import IdentityBias as IdentityBias
from llm_lib2.models.transformer.attention_bias import (
    materialize_attention_bias as materialize_attention_bias,
)
from llm_lib2.models.transformer.attention_bias import (
    maybe_get_attention_bias_tensor as maybe_get_attention_bias_tensor,
)
from llm_lib2.models.transformer.decoder import (
    StandardTransformerDecoder as StandardTransformerDecoder,
)
from llm_lib2.models.transformer.decoder import TransformerDecoder as TransformerDecoder
from llm_lib2.models.transformer.decoder import (
    TransformerDecoderLayerHook as TransformerDecoderLayerHook,
)
from llm_lib2.models.transformer.decoder_layer import (
    StandardTransformerDecoderLayer as StandardTransformerDecoderLayer,
)
from llm_lib2.models.transformer.decoder_layer import (
    TransformerDecoderLayer as TransformerDecoderLayer,
)
from llm_lib2.models.transformer.encoder import (
    StandardTransformerEncoder as StandardTransformerEncoder,
)
from llm_lib2.models.transformer.encoder import TransformerEncoder as TransformerEncoder
from llm_lib2.models.transformer.encoder import (
    TransformerEncoderLayerHook as TransformerEncoderLayerHook,
)
from llm_lib2.models.transformer.encoder_layer import (
    StandardTransformerEncoderLayer as StandardTransformerEncoderLayer,
)
from llm_lib2.models.transformer.encoder_layer import (
    TransformerEncoderLayer as TransformerEncoderLayer,
)
from llm_lib2.models.transformer.experts import ExpertNetwork as ExpertNetwork
from llm_lib2.models.transformer.experts import (
    GroupedExpertNetwork as GroupedExpertNetwork,
)
from llm_lib2.models.transformer.experts import (
    TPShardedExpertNetwork as TPShardedExpertNetwork,
)
from llm_lib2.models.transformer.ffn import (
    DauphinFeedForwardNetwork as DauphinFeedForwardNetwork,
)
from llm_lib2.models.transformer.ffn import FeedForwardNetwork as FeedForwardNetwork
from llm_lib2.models.transformer.ffn import (
    GLUFeedForwardNetwork as GLUFeedForwardNetwork,
)
from llm_lib2.models.transformer.ffn import (
    StandardFeedForwardNetwork as StandardFeedForwardNetwork,
)
from llm_lib2.models.transformer.frontend import (
    TransformerEmbeddingFrontend as TransformerEmbeddingFrontend,
)
from llm_lib2.models.transformer.frontend import (
    TransformerFrontend as TransformerFrontend,
)
from llm_lib2.models.transformer.fsdp import (
    apply_fsdp_to_transformer as apply_fsdp_to_transformer,
)
from llm_lib2.models.transformer.model import TransformerModel as TransformerModel
from llm_lib2.models.transformer.multihead_attention import (
    AttentionState as AttentionState,
)
from llm_lib2.models.transformer.multihead_attention import (
    AttentionStateFactory as AttentionStateFactory,
)
from llm_lib2.models.transformer.multihead_attention import (
    AttentionWeightHook as AttentionWeightHook,
)
from llm_lib2.models.transformer.multihead_attention import (
    AttentionWeightStoreHook as AttentionWeightStoreHook,
)
from llm_lib2.models.transformer.multihead_attention import (
    FullAttentionState as FullAttentionState,
)
from llm_lib2.models.transformer.multihead_attention import (
    LocalAttentionState as LocalAttentionState,
)
from llm_lib2.models.transformer.multihead_attention import (
    LocalAttentionStateFactory as LocalAttentionStateFactory,
)
from llm_lib2.models.transformer.multihead_attention import (
    MultiheadAttention as MultiheadAttention,
)
from llm_lib2.models.transformer.multihead_attention import (
    StandardMultiheadAttention as StandardMultiheadAttention,
)
from llm_lib2.models.transformer.multihead_attention import (
    StaticAttentionState as StaticAttentionState,
)
from llm_lib2.models.transformer.multihead_attention import (
    init_mha_output_projection as init_mha_output_projection,
)
from llm_lib2.models.transformer.multihead_attention import (
    init_qkv_projection as init_qkv_projection,
)
from llm_lib2.models.transformer.norm_order import (
    TransformerNormOrder as TransformerNormOrder,
)
from llm_lib2.models.transformer.sdpa.base import SDPA as SDPA
from llm_lib2.models.transformer.sdpa.default import SDPAFactory as SDPAFactory
from llm_lib2.models.transformer.sdpa.default import (
    create_default_sdpa as create_default_sdpa,
)
from llm_lib2.models.transformer.sdpa.default import (
    get_default_sdpa_factory as get_default_sdpa_factory,
)
from llm_lib2.models.transformer.sdpa.default import (
    set_default_sdpa_factory as set_default_sdpa_factory,
)
from llm_lib2.models.transformer.sdpa.flash2 import Flash2SDPA as Flash2SDPA
from llm_lib2.models.transformer.sdpa.flash3 import Flash3SDPA as Flash3SDPA
from llm_lib2.models.transformer.sdpa.naive import NaiveSDPA as NaiveSDPA
from llm_lib2.models.transformer.sdpa.naive import (
    naive_scaled_dot_product_attention as naive_scaled_dot_product_attention,
)
from llm_lib2.models.transformer.sdpa.relative import (
    RelativePositionalEncoding as RelativePositionalEncoding,
)
from llm_lib2.models.transformer.sdpa.relative import (
    RelativePositionSDPA as RelativePositionSDPA,
)
from llm_lib2.models.transformer.sdpa.shaw import (
    ShawRelativePositionSDPA as ShawRelativePositionSDPA,
)
from llm_lib2.models.transformer.sdpa.shaw import (
    init_shaw_embedding as init_shaw_embedding,
)
from llm_lib2.models.transformer.sdpa.torch import TorchSDPA as TorchSDPA
