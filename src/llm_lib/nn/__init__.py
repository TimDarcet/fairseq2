# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import annotations

from llm_lib2.nn.batch_layout import BatchLayout as BatchLayout
from llm_lib2.nn.embedding import Embedding as Embedding
from llm_lib2.nn.embedding import ShardedEmbedding as ShardedEmbedding
from llm_lib2.nn.embedding import StandardEmbedding as StandardEmbedding
from llm_lib2.nn.embedding import VocabShardedEmbedding as VocabShardedEmbedding
from llm_lib2.nn.embedding import init_scaled_embedding as init_scaled_embedding
from llm_lib2.nn.incremental_state import IncrementalState as IncrementalState
from llm_lib2.nn.incremental_state import IncrementalStateBag as IncrementalStateBag
from llm_lib2.nn.normalization import LayerNorm as LayerNorm
from llm_lib2.nn.normalization import RMSNorm as RMSNorm
from llm_lib2.nn.normalization import StandardLayerNorm as StandardLayerNorm
from llm_lib2.nn.position_encoder import (
    InterpolatedPositionEncoder as InterpolatedPositionEncoder,
)
from llm_lib2.nn.position_encoder import (
    LearnedPositionEncoder as LearnedPositionEncoder,
)
from llm_lib2.nn.position_encoder import PositionEncoder as PositionEncoder
from llm_lib2.nn.position_encoder import (
    ReferenceRotaryEncoder as ReferenceRotaryEncoder,
)
from llm_lib2.nn.position_encoder import RotaryEncoder as RotaryEncoder
from llm_lib2.nn.position_encoder import (
    Sinusoidal2dPositionEncoder as Sinusoidal2dPositionEncoder,
)
from llm_lib2.nn.position_encoder import (
    Sinusoidal3dPositionEncoder as Sinusoidal3dPositionEncoder,
)
from llm_lib2.nn.position_encoder import (
    SinusoidalNdPositionEncoder as SinusoidalNdPositionEncoder,
)
from llm_lib2.nn.position_encoder import (
    SinusoidalPositionEncoder as SinusoidalPositionEncoder,
)
from llm_lib2.nn.projection import ColumnShardedLinear as ColumnShardedLinear
from llm_lib2.nn.projection import IdentityProjection as IdentityProjection
from llm_lib2.nn.projection import Linear as Linear
from llm_lib2.nn.projection import Projection as Projection
from llm_lib2.nn.projection import RowShardedLinear as RowShardedLinear
from llm_lib2.nn.projection import TiedProjection as TiedProjection
from llm_lib2.nn.projection import init_bert_projection as init_bert_projection
from llm_lib2.nn.residual import AdditiveResidualConnect as AdditiveResidualConnect
from llm_lib2.nn.residual import DropPathResidualConnect as DropPathResidualConnect
from llm_lib2.nn.residual import ResidualConnect as ResidualConnect
from llm_lib2.nn.residual import ScaledResidualConnect as ScaledResidualConnect
from llm_lib2.nn.sharded import Sharded as Sharded
from llm_lib2.nn.sharded import get_shard_dims as get_shard_dims
