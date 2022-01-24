load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library", "cc_test")

cc_library(
    name = "hello_greet",
    srcs = ["hello_greet.cc"],
    hdrs = ["hello_greet.h"]
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
        "@argparse//:argparse"
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

cc_test(
    name = "hello_test",
    srcs = [
        "hello_greet_test.cc"
    ],
    deps = [
        ":hello_greet",
        "@gtest//:gtest",
        "@gtest//:gtest_main"
    ]
)