load("@rules_foreign_cc//foreign_cc:defs.bzl", "cmake")


filegroup(
    name = "all",
    srcs = glob(["**"]),
    visibility = ["//visibility:public"]
)

# TODO: https://github.com/cschuet/leveldb uses ports.h to configure leveld. Do I need this?

cmake(
    name = "leveldb",
    visibility = ["//visibility:public"],
    env = {
        "CXXFLAGS": "-Wno-error",
        "CFLAGS": "-Wno-error"
    },
    cache_entries = {
        "CMAKE_BUILD_TYPE": "Release",
        "BUILD_SHARED_LIBS": "OFF",
        # Turning off building tests and benchmarks as those would
        # requires first pulling down those git submodules (which
        # would also require using 'git_repository' instead of
        # 'http_archive'.
        "LEVELDB_BUILD_TESTS": "OFF",
        "LEVELDB_BUILD_BENCHMARKS": "OFF",
        "CXXFLAGS": "-Wno-error",
        "CFLAGS": "-Wno-error"
    },
    lib_source = ":all",
    out_static_libs = ["libleveldb.a"],
)