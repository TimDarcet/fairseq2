# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, final

from llm_lib2n import DOC_MODE
from torch import Tensor
from typing_extensions import NotRequired

from llm_lib2.data._memory import MemoryBlock
from llm_lib2.data_type import DataType
from llm_lib2.device import Device

if TYPE_CHECKING or DOC_MODE:

    @final
    class AudioDecoder:
        def __init__(
            self,
            keepdim: bool = False,
            dtype: DataType | None = None,
            device: Device | None = None,
            pin_memory: bool = False,
        ) -> None: ...

        def __call__(self, memory_block: MemoryBlock) -> AudioDecoderOutput: ...

    @final
    class WaveformToFbankConverter:
        def __init__(
            self,
            num_mel_bins: int = 80,
            waveform_scale: float = 1.0,
            channel_last: bool = False,
            standardize: bool = False,
            keep_waveform: bool = False,
            dtype: DataType | None = None,
            device: Device | None = None,
            pin_memory: bool = False,
        ) -> None: ...

        def __call__(self, waveform: WaveformToFbankInput) -> WaveformToFbankOutput: ...

else:
    from llm_lib2n.bindings.data.audio import AudioDecoder as AudioDecoder  # noqa: F401
    from llm_lib2n.bindings.data.audio import (  # noqa: F401
        WaveformToFbankConverter as WaveformToFbankConverter,
    )


class AudioDecoderOutput(TypedDict):
    waveform: Tensor
    sample_rate: float
    format: int


class WaveformToFbankInput(TypedDict):
    waveform: Tensor
    sample_rate: int | float


class WaveformToFbankOutput(TypedDict):
    fbank: Tensor
    waveform: NotRequired[Tensor]
    sample_rate: float
