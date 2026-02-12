// Copyright (c) Meta Platforms, Inc. and affiliates.
// All rights reserved.
//
// This source code is licensed under the BSD-style license found in the
// LICENSE file in the root directory of this source tree.

#pragma once

#include <pybind11/pybind11.h>

#include <llm_lib2n/data/py.h>

namespace pybind11::detail {

template <>
struct type_caster<llm_lib2n::py_object> {
    PYBIND11_TYPE_CASTER(llm_lib2n::py_object, const_name("Any"));

public:
    bool
    load(handle src, bool)
    {
        value = llm_lib2n::py_object{src.ptr()};

        return true;
    }

    static handle
    cast(const llm_lib2n::py_object &src, return_value_policy, handle)
    {
        auto ptr = static_cast<PyObject *>(src.ptr());

        handle h{ptr};

        h.inc_ref();

        return h;
    }

    static handle
    cast(llm_lib2n::py_object &&src, return_value_policy, handle)
    {
        auto ptr = static_cast<PyObject *>(src.release());

        return handle{ptr};
    }
};

}  // namespace pybind11::detail
