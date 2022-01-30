load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_skylib",
    sha256 = "c6966ec828da198c5d9adbaa94c05e3a1c7f21bd012a0b29ba8ddbccb2c93b0d",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.1.1/bazel-skylib-1.1.1.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.1.1/bazel-skylib-1.1.1.tar.gz",
    ],
)

load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")

bazel_skylib_workspace()


http_archive(
    name = "gtest",
    strip_prefix = "googletest-release-1.11.0",
    urls = ["https://github.com/google/googletest/archive/refs/tags/release-1.11.0.zip"],
)

http_archive(
    name = "com_github_gflags_gflags",
    sha256 = "34af2f15cf7367513b352bdcd2493ab14ce43692d2dcd9dfc499492966c64dcf",
    strip_prefix = "gflags-2.2.2",
    urls = ["https://github.com/gflags/gflags/archive/v2.2.2.tar.gz"],
)

http_archive(
    name = "com_github_google_glog",
    sha256 = "21bc744fb7f2fa701ee8db339ded7dce4f975d0d55837a97be7d46e8382dea5a",
    strip_prefix = "glog-0.5.0",
    urls = ["https://github.com/google/glog/archive/v0.5.0.zip"],
)

http_archive(
    name = "com_google_absl",
    sha256 = "aabf6c57e3834f8dc3873a927f37eaf69975d4b28117fc7427dfb1c661542a87",
    strip_prefix = "abseil-cpp-98eb410c93ad059f9bba1bf43f5bb916fc92a5ea",
    urls = ["https://github.com/abseil/abseil-cpp/archive/98eb410c93ad059f9bba1bf43f5bb916fc92a5ea.zip"],
)

http_archive(
    name = "com_google_benchmark",
    sha256 = "2a778d821997df7d8646c9c59b8edb9a573a6e04c534c01892a40aa524a7b68c",
    strip_prefix = "benchmark-bf585a2789e30585b4e3ce6baf11ef2750b54677",
    urls = ["https://github.com/google/benchmark/archive/bf585a2789e30585b4e3ce6baf11ef2750b54677.zip"],
)

http_archive(
    name = "eigen",
    build_file = "//bazel/third_party:eigen.BUILD",
    sha256 = "1ccaabbfe870f60af3d6a519c53e09f3dcf630207321dffa553564a8e75c4fc8",
    strip_prefix = "eigen-3.4.0",
    urls = [
        "https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.zip",
    ],
)

http_archive(
    name = "json",
    build_file = "//bazel/third_party:json.BUILD",
    sha256 = "ea4b0084709fb934f92ca0a68669daa0fe6f2a2c6400bf353454993a834bb0bb",
    strip_prefix = "json-3.10.5",
    urls = [
        "https://github.com/nlohmann/json/archive/refs/tags/v3.10.5.zip",
    ],
)

http_archive(
    name = "boost_ext_di",
    build_file = "//bazel/third_party:boost_ext_di.BUILD",
    strip_prefix = "di-1.2.0",
    sha256 = "c3d0cddc478b0138be5cf46eaf00d3610fb36a1bd23fda2d79f296c83f2d22ba",
    urls = [
        "https://github.com/boost-ext/di/archive/refs/tags/v1.2.0.zip"
    ]
)

http_archive(
    name="argparse",
    build_file = "//bazel/third_party:argparse.BUILD",
    sha256 = "496e3ec5aa52a70591557dbc47a219398320515796c3427637377333c47d52be",
    strip_prefix = "argparse-2.2",
    urls = [
        "https://github.com/p-ranav/argparse/archive/refs/tags/v2.2.zip"
    ]
)

http_archive(
    name = "xsimd",
    build_file = "//bazel/third_party:xsimd.BUILD",
    strip_prefix = "xsimd-8.0.5",
    urls = [
        "https://github.com/xtensor-stack/xsimd/archive/refs/tags/8.0.5.zip"
    ]
)

http_archive(
    name = "xtl",
    build_file = "//bazel/third_party:xtl.BUILD",
    strip_prefix = "xtl-0.7.4",
    sha256 = "5e0bea21c3a134e23c73082e0eec3d9e4fbec56e3a434526460042b6c26695a7",
    urls = [
        "https://github.com/xtensor-stack/xtl/archive/refs/tags/0.7.4.zip"
    ]
)

http_archive(
    name = "xtensor",
    build_file = "//bazel/third_party:xtensor.BUILD",
    sha256 = "0823e26127fa387efa45b77c2d151ad38e0f9a490850729821f9a8ae399d0069",
    strip_prefix = "xtensor-0.24.0",
    urls = [
        "https://github.com/xtensor-stack/xtensor/archive/refs/tags/0.24.0.zip"
    ]
)

http_archive(
    name="rapidcheck",
    build_file = "//bazel/third_party:rapidcheck.BUILD",
    sha256 = "4b1f727cc942b04d7e0f6bd8500163d870c3e8ed93d24644397c6685b039314b",
    strip_prefix = "rapidcheck-08b505857e32d52a20b2240b5125d937d67a6d86",
    urls = [
        "https://github.com/emil-e/rapidcheck/archive/08b505857e32d52a20b2240b5125d937d67a6d86.zip"
    ]
)

http_archive(
    name = "re2",
    strip_prefix = "re2-2021-11-01",
    sha256 = "3a20f05c57f907f78b817a53f2fb6e48077d2b1d0b17b39caf875c20f262230b",
    urls = [
        "https://github.com/google/re2/archive/refs/tags/2021-11-01.zip"
    ]
)

http_archive(
    name = "rules_python",
    sha256 = "e5470e92a18aa51830db99a4d9c492cc613761d5bdb7131c04bd92b9834380f6",
    strip_prefix = "rules_python-4b84ad270387a7c439ebdccfd530e2339601ef27",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_python/archive/4b84ad270387a7c439ebdccfd530e2339601ef27.tar.gz",
        "https://github.com/bazelbuild/rules_python/archive/4b84ad270387a7c439ebdccfd530e2339601ef27.tar.gz",
    ],
)

http_archive( # required by protobuf
    name = "net_zlib_zlib",
    build_file = "//bazel/third_party:zlib.BUILD",
    strip_prefix = "zlib-1.2.11",
    sha256 = "f5cc4ab910db99b2bdbba39ebbdc225ffc2aa04b4057bc2817f1b94b6978cfc3",
    urls = [
        "https://github.com/madler/zlib/archive/refs/tags/v1.2.11.zip",
    ],
)

http_archive(
    name = "com_google_protobuf",
    repo_mapping = {"@zlib": "@net_zlib_zlib"},
    strip_prefix = "protobuf-3.19.3",
    sha256 = "6b6bf5cd8d0cca442745c4c3c9f527c83ad6ef35a405f64db5215889ac779b42",
    urls = [
        "https://github.com/google/protobuf/archive/v3.19.3.zip",
    ],
)


http_archive(
    name = "hedron_compile_commands",
    url = "https://github.com/hedronvision/bazel-compile-commands-extractor/archive/084957eaa1bf6e2bd031f50b1f5d04c89273103a.tar.gz",
    strip_prefix = "bazel-compile-commands-extractor-084957eaa1bf6e2bd031f50b1f5d04c89273103a",
)
load("@hedron_compile_commands//:workspace_setup.bzl", "hedron_compile_commands_setup")
hedron_compile_commands_setup()


http_archive(
    name = "rules_foreign_cc",
    url = "https://github.com/bazelbuild/rules_foreign_cc/archive/0.2.0.tar.gz",
    sha256 = "d54742ffbdc6924f222d2179f0e10e911c5c659c4ae74158e9fe827aad862ac6",
    strip_prefix = "rules_foreign_cc-0.2.0",
)
load("@rules_foreign_cc//foreign_cc:repositories.bzl", "rules_foreign_cc_dependencies")
rules_foreign_cc_dependencies()