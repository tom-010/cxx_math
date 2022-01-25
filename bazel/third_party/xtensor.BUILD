cc_library(
    name = "xtensor",
    hdrs = glob(["include/xtensor/**"]),
    includes = ["include"],
    visibility = ["//visibility:public"],
    defines = ["XTENSOR_USE_XSIMD"],
    deps = [
        "@xtl//:xtl",
        "@xsimd//:xsimd"
    ]
)