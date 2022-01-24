cc_library(
    name = "rapidcheck",
    hdrs = glob([
        "include/**",
        "extras/gtest/include/**"
    ]),
    srcs = glob([
        "src/**"
    ]),
    includes = ["include", "extras/gtest/include"],
    visibility = ["//visibility:public"],
    deps = [
        "@gtest//:gtest",
    ]
)