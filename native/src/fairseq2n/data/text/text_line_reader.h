// Copyright (c) Meta Platforms, Inc. and affiliates.
// All rights reserved.
//
// This source code is licensed under the BSD-style license found in the
// LICENSE file in the root directory of this source tree.

#pragma once

#include <memory>
#include <utility>

#include "llm_lib2n/span.h"
#include "llm_lib2n/data/byte_stream.h"
#include "llm_lib2n/data/record_reader.h"
#include "llm_lib2n/data/text/text_reader.h"

namespace llm_lib2n::detail {

class text_line_reader final : public record_reader {
public:
    explicit
    text_line_reader(std::unique_ptr<byte_stream> &&stream, line_ending le)
      : record_reader{std::move(stream)}, line_ending_{le}
    {}

    line_ending
    actual_line_ending() const noexcept
    {
        return line_ending_;
    }

private:
    std::optional<std::size_t>
    maybe_find_record_end(memory_span chunk, bool first_chunk) override;

    bool
    infer_line_ending(span<const char> chars);

private:
    line_ending line_ending_;
};

}  // namespace llm_lib2n::detail
