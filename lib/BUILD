load("@rules_cc//cc:defs.bzl", "cc_library")

cc_library(
    name = "hello_time",
    srcs = ["hello_time.cc"],
    hdrs = ["hello_time.h"],
    deps = ["@com_github_google_glog//:glog"],
    visibility = ["//main:__pkg__"]
)
