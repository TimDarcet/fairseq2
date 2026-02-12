# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

cmake_minimum_required(VERSION 3.21.0)

project(llm_lib2n VERSION 0.8.0 LANGUAGES C CXX)

if(NOT CMAKE_BUILD_TYPE AND NOT CMAKE_CONFIGURATION_TYPES)
    set_property(CACHE CMAKE_BUILD_TYPE PROPERTY VALUE RelWithDebInfo)
endif()

if(DEFINED ENV{CONDA_PREFIX} AND NOT DEFINED ENV{CONDA_BUILD_SYSROOT})
    message(FATAL_ERROR
        "It looks like you are in a Conda environment, but the `compilers` package is not installed. Please run `conda install -c conda-forge compilers=1.2.0 zlib libxcrypt` first."
    )
endif()

include(CMakeDependentOption)
include(CMakePackageConfigHelpers)
include(CheckLanguage)
include(GNUInstallDirs)

if(PROJECT_IS_TOP_LEVEL)
    include(CTest)
endif()

list(APPEND CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake/modules)

include(cmake/base.cmake)
include(cmake/summary.cmake)

# Prefer pthread over other thread libraries.
set(THREADS_PREFER_PTHREAD_FLAG TRUE)

# ------------------------------------------------------------
# Options
# ------------------------------------------------------------

option(llm_lib2N_BUILD_FOR_NATIVE
    #DESCRIPTION
        "Builds for the processor type of the compiling machine."
    #VALUE
        OFF
)

option(llm_lib2N_INSTALL_STANDALONE
    #DESCRIPTION
        "Installs with relative rpaths."
    #VALUE
        ON
)

option(llm_lib2N_PERFORM_LTO
    #DESCRIPTION
        "Performs link-time optimization."
    #VALUE
        OFF
)

option(llm_lib2N_RUN_CLANG_TIDY
    #DESCRIPTION
        "Runs clang-tidy as static analyzer during compilation."
    #VALUE
        OFF
)

set(llm_lib2N_SANITIZERS
    #VALUE
        ""
    #TYPE
        CACHE STRING
    #DESCRIPTION
        "Sanitizers to enable."
)
set_property(CACHE llm_lib2N_SANITIZERS PROPERTY
    STRINGS
        "" "asan" "ubsan" "tsan"
)

option(llm_lib2N_TREAT_WARNINGS_AS_ERRORS
    #DESCRIPTION
        "Treats compilation warnings as errors."
    #VALUE
        OFF
)

option(llm_lib2N_SUPPORT_IMAGE
    #DESCRIPTION
        "Supports JPEG/PNG decoding."
    #VALUE
        ON
)

option(llm_lib2N_USE_LIBTORCH
    #DESCRIPTION
        "Uses libtorch instead of PyTorch."
    #VALUE
        OFF
)

option(llm_lib2N_USE_CUDA
    #DESCRIPTION
        "Builds the CUDA kernels."
    #VALUE
        OFF
)

if(CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")
    set(default_thread_lib tbb)
else()
    set(default_thread_lib)
endif()

set(llm_lib2N_THREAD_LIB
    #VALUE
        ${default_thread_lib}
    #TYPE
        CACHE STRING
    #DESCRIPTION
        "Thread library to use."
)
set_property(CACHE llm_lib2N_THREAD_LIB PROPERTY
    STRINGS
        "" "tbb"
)

if(llm_lib2N_THREAD_LIB STREQUAL "tbb")
    if(NOT CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")
        message(FATAL_ERROR "Intel oneTBB is only supported on x86-64 systems.")
    endif()
endif()

option(llm_lib2N_BUILD_PYTHON_BINDINGS
    #DESCRIPTION
        "Builds the Python bindings."
    #VALUE
        ON
)

cmake_dependent_option(llm_lib2N_PYTHON_DEVEL
    #DESCRIPTION
        "Copies the Python extension module to the source tree for `pip install --editable`."
    #VALUE
        ON
    #DEPENDS_ON
        llm_lib2N_BUILD_PYTHON_BINDINGS
    #HIDDEN_VALUE
        OFF
)

# ------------------------------------------------------------
# Sanitizers
# ------------------------------------------------------------

llm_lib2n_set_sanitizers()

# ------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------

find_package(Iconv REQUIRED)

find_package(SndFile REQUIRED)

find_package(Threads REQUIRED)

if(llm_lib2N_THREAD_LIB STREQUAL "tbb")
    find_package(TBB 2021.8 REQUIRED)
endif()

find_package(Torch 1.13 REQUIRED)

if(llm_lib2N_BUILD_PYTHON_BINDINGS)
    find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)
    if(Python3_VERSION VERSION_LESS 3.8)
        message(FATAL_ERROR "llm_lib2n requires CPython 3.8 or greater!")
    endif()
endif()

if(llm_lib2N_RUN_CLANG_TIDY)
    if(NOT CMAKE_CXX_COMPILER_ID MATCHES "Clang")
        message(FATAL_ERROR "llm_lib2n requires Clang when `llm_lib2N_RUN_CLANG_TIDY` is set!")
    endif()

    find_package(ClangTidy REQUIRED)
endif()

add_subdirectory(third-party)

llm_lib2n_add_fmt()

llm_lib2n_add_kaldi_native_fbank()

llm_lib2n_add_natsort()

llm_lib2n_add_sentencepiece()

llm_lib2n_add_zip()

if(llm_lib2N_SUPPORT_IMAGE)
    llm_lib2n_add_libjpeg_turbo()

    llm_lib2n_add_libpng()
endif()

if(llm_lib2N_BUILD_PYTHON_BINDINGS)
    llm_lib2n_add_pybind11()
endif()

if(PROJECT_IS_TOP_LEVEL AND BUILD_TESTING)
    llm_lib2n_add_gtest()
endif()

# ------------------------------------------------------------
# CUDA
# ------------------------------------------------------------

# By default, we build our CUDA kernels only for the Volta architecture.
if(NOT DEFINED CMAKE_CUDA_ARCHITECTURES)
    set(CMAKE_CUDA_ARCHITECTURES 70-real 70-virtual)
endif()

if(llm_lib2N_USE_CUDA)
    if(NOT TORCH_CUDA_VERSION)
        message(FATAL_ERROR
            "llm_lib2n requires a CUDA version of PyTorch when `llm_lib2N_USE_CUDA` is set!"
        )
    endif()

    enable_language(CUDA)

    find_package(CUDAToolkit REQUIRED)

    if(NOT CUDAToolkit_VERSION_MAJOR EQUAL TORCH_CUDA_VERSION_MAJOR)
        message(FATAL_ERROR
            "llm_lib2n requires the version of the CUDA Toolkit (${CUDAToolkit_VERSION}) to match the version of CUDA that was used to build PyTorch (${TORCH_CUDA_VERSION})!"
        )
    endif()

    if(NOT CUDAToolkit_VERSION_MINOR EQUAL TORCH_CUDA_VERSION_MINOR)
        message(WARNING
            "llm_lib2n will use CUDA Toolkit ${CUDAToolkit_VERSION} which has a minor version mismatch with CUDA ${TORCH_CUDA_VERSION} that was used to build PyTorch. Most likely this should not be a problem."
        )
    endif()
endif()

# ------------------------------------------------------------
# Package Installation
# ------------------------------------------------------------

if(llm_lib2N_INSTALL_STANDALONE)
    set(install_lib_dir lib)
    set(install_inc_dir include)
else()
    set(install_lib_dir ${CMAKE_INSTALL_LIBDIR})
    set(install_inc_dir ${CMAKE_INSTALL_INCLUDEDIR})
endif()

set(install_pkg_dir ${install_lib_dir}/cmake/llm_lib2n-${PROJECT_VERSION})

configure_package_config_file(
    #INPUT
        ${PROJECT_SOURCE_DIR}/src/llm_lib2n-config.cmake.in
    #OUTPUT
        ${PROJECT_BINARY_DIR}/lib/cmake/llm_lib2n/llm_lib2n-config.cmake
    INSTALL_DESTINATION
        ${install_pkg_dir}
    NO_SET_AND_CHECK_MACRO
)

write_basic_package_version_file(
    #OUTPUT
        ${PROJECT_BINARY_DIR}/lib/cmake/llm_lib2n/llm_lib2n-config-version.cmake
    VERSION
        ${PROJECT_VERSION}
    COMPATIBILITY
        AnyNewerVersion
)

install(
    FILES
        ${PROJECT_BINARY_DIR}/lib/cmake/llm_lib2n/llm_lib2n-config.cmake
        ${PROJECT_BINARY_DIR}/lib/cmake/llm_lib2n/llm_lib2n-config-version.cmake
    DESTINATION
        ${install_pkg_dir}
    COMPONENT
        devel
)

install(
    EXPORT
        llm_lib2n-targets
    FILE
        llm_lib2n-targets.cmake
    DESTINATION
        ${install_pkg_dir}
    COMPONENT
        devel
    NAMESPACE
        llm_lib2n::
)

export(
    EXPORT
        llm_lib2n-targets
    FILE
        ${PROJECT_BINARY_DIR}/lib/cmake/llm_lib2n/llm_lib2n-targets.cmake
    NAMESPACE
        llm_lib2n::
)

# ------------------------------------------------------------
# Targets
# ------------------------------------------------------------

add_subdirectory(src/llm_lib2n)

if(llm_lib2N_BUILD_PYTHON_BINDINGS)
    add_subdirectory(python/src/llm_lib2n)
endif()

if(PROJECT_IS_TOP_LEVEL AND BUILD_TESTING)
    add_subdirectory(tests)
endif()

# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------

llm_lib2n_print_project_summary()
