load("@rules_cc//cc:defs.bzl", "cc_library")

cc_library(
    name = "hello",
    srcs = ["hello.cc"],
    copts = ["-Wpedantic"],
    hdrs = ["hello.h"],
    deps = ["@com_github_google_glog//:glog"],
    visibility = ["//main:__pkg__"]
)

cc_test(
    name = "hello_test",
    srcs = glob(["*_test.cc"]),
    deps = [
        ":hello",
        "@gtest//:gtest",
        "@gtest//:gtest_main",
        "@rapidcheck//:rapidcheck",
    ]
)

cc_binary(
    name = "hello_sample",
    srcs = ["hello_sample.cc"],
    deps = [
        ":hello",
        "@com_github_google_glog//:glog"
    ]
)

cc_binary(
    name = "hello_benchmark",
    srcs = ["hello_benchmark.cc"],
    deps = [
        ":hello",
        "@com_google_benchmark//:benchmark",        
    ]
)

cc_binary(
    name = "hello_fuzz",
    srcs = ["hello_fuzz.cc"],
    copts = ["-fsanitize=fuzzer,address"],
    linkopts = ["-fsanitize=fuzzer,address"],
    deps = [
        ":hello",
    ]
)

