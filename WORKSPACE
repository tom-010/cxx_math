load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")
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

git_repository(
    name = "gtest",
    branch = "release-1.11.0",
    remote = "https://github.com/google/googletest",
)

# http_archive(
#   name = "com_google_googletest",
#   urls = ["https://github.com/google/googletest/archive/011959aafddcd30611003de96cfd8d7a7685c700.zip"],
#   strip_prefix = "googletest-011959aafddcd30611003de96cfd8d7a7685c700",
# )

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
    strip_prefix = "json-3.10.5",
    urls = [
        "https://github.com/nlohmann/json/archive/refs/tags/v3.10.5.zip",
    ],
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
