// Copyright (c) Meta Platforms, Inc. and affiliates.
// All rights reserved.
//
// This source code is licensed under the BSD-style license found in the
// LICENSE file in the root directory of this source tree.

#pragma once

#include <memory>
#include <string>
#include <string_view>
#include <vector>

#include <ATen/Tensor.h>

#include "llm_lib2n/api.h"
#include "llm_lib2n/data/data.h"
#include "llm_lib2n/data/immutable_string.h"

namespace llm_lib2n {

class sp_model;

class llm_lib2_API sp_decoder final {
public:
    explicit
    sp_decoder(std::shared_ptr<const sp_model> model, bool reverse = false) noexcept;

    data
    operator()(data &&d) const;

    std::string
    decode(const at::Tensor &tensor) const;

    std::string
    decode_from_tokens(const std::vector<std::string_view> &tokens) const;

private:
    template <typename T>
    std::string
    do_decode(const at::Tensor &tensor) const;

private:
    std::shared_ptr<const sp_model> model_;
    bool reverse_;
};

}  // namespace llm_lib2n
