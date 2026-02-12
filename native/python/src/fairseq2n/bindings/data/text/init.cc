// Copyright (c) Meta Platforms, Inc. and affiliates.
// All rights reserved.
//
// This source code is licensed under the BSD-style license found in the
// LICENSE file in the root directory of this source tree.

#include "llm_lib2n/bindings/module.h"

namespace py = pybind11;

namespace llm_lib2n {

void
def_text(py::module_ &data_module)
{
    py::module_ m = data_module.def_submodule("text");

    def_sentencepiece(m);

    def_text_reader(m);

    def_text_converters(m);
}

}  // namespace llm_lib2n
