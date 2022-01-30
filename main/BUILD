load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library", "cc_test")

cc_library(
    name = "hello_greet",
    srcs = ["hello_greet.cc"],
    hdrs = ["hello_greet.h"]
)

cc_binary(
    name = "light",
    srcs = ["light.cc"]
)

cc_binary(
    name = "hello_world",
    srcs = ["hello_world.cc"],
    deps = [
        ":hello_greet",
        "//messages:person_cc_proto",
        "//lib:hello_time",
        "@com_google_absl//absl/strings",
        "@eigen//:eigen",
        "@json//:json",
        "@argparse//:argparse",
        "@re2//:re2",
        "@com_github_google_leveldb//:leveldb",
        "@xtensor//:xtensor",
        "@boost_ext_di//:di"
    ]
)

cc_binary(
    name = "benchmark",
    srcs = ["benchmark.cc"],
    deps = [
        ":hello_greet",
        "@com_google_benchmark//:benchmark",        
    ]
)

cc_binary(
    name = "benchmark_simd",
    srcs = ["benchmark_simd.cc"],
    deps = [
        "@xtensor//:xtensor",
        "@com_google_benchmark//:benchmark", 
    ]
)

cc_test(
    name = "pbt",
    srcs = [
        "pbt.cc"
    ],
    deps = [
        "@rapidcheck//:rapidcheck",
        "@gtest//:gtest",
        "@gtest//:gtest_main"
    ]
)

cc_test(
    name = "hello_test",
    srcs = [
        "hello_greet_test.cc"
    ],
    deps = [
        ":hello_greet",
        "@gtest//:gtest",
        "@gtest//:gtest_main"
    ],
    data = ["testdata/somefile.txt"]
)