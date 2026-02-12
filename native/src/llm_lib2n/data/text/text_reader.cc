// Copyright (c) Meta Platforms, Inc. and affiliates.
// All rights reserved.
//
// This source code is licensed under the BSD-style license found in the
// LICENSE file in the root directory of this source tree.

#include "llm_lib2n/data/text/text_reader.h"

#include <memory>

#include "llm_lib2n/data/data_pipeline.h"
#include "llm_lib2n/data/text/text_data_source.h"

using namespace llm_lib2n::detail;

namespace llm_lib2n {

data_pipeline_builder
read_text(std::filesystem::path path, std::optional<std::string> maybe_key, text_options opts)
{
    auto factory = [
        path = std::move(path),
        maybe_key = std::move(maybe_key),
        opts = std::move(opts)]() mutable
    {
        return std::make_unique<text_data_source>(
            std::move(path), std::move(maybe_key), std::move(opts));
    };

    return data_pipeline_builder{std::move(factory)};
}

}  // namespace llm_lib2n
