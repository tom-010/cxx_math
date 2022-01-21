import os
import sys 

h_template = '''
#ifndef LIB_<<LIB_NAME>>_H_
#define LIB_<<LIB_NAME>>_H_

int <<lib_name>>();

#endif
'''

cc_template = '''
#include "<<lib_name>>.h"
#include <glog/logging.h>

int <<lib_name>>() {
    return 0;
}
'''

BUILD_template = '''
load("@rules_cc//cc:defs.bzl", "cc_library")

cc_library(
    name = "<<lib_name>>",
    srcs = ["<<lib_name>>.cc"],
    hdrs = ["<<lib_name>>.h"],
    deps = ["@com_github_google_glog//:glog"],
    visibility = ["//main:__pkg__"]
)

cc_test(
    name = "<<lib_name>>_test",
    srcs = [
        "<<lib_name>>_test.cc"
    ],
    deps = [
        ":<<lib_name>>",
        "@gtest//:gtest",
        "@gtest//:gtest_main"
    ]
)

cc_binary(
    name = "<<lib_name>>_benchmark",
    srcs = ["<<lib_name>>_benchmark.cc"],
    deps = [
        ":<<lib_name>>",
        "@com_google_benchmark//:benchmark",        
    ]
)
'''

test_template = '''
#include "gtest/gtest.h"
#include "gmock/gmock.h"
#include "<<lib_name>>.h"

TEST(<<lib_name>>, nothing) {
    EXPECT_EQ(<<lib_name>>(), 1);
}
'''

benchmark_template = '''
#include <benchmark/benchmark.h>
#include "<<lib_name>>.h"

static void BM_<<lib_name>>(benchmark::State& state) {
  // Perform setup here
  for (auto _ : state) {
    // This code gets timed
    <<lib_name>>();
  }
}
BENCHMARK(BM_<<lib_name>>);


// Run the benchmark
BENCHMARK_MAIN();
'''

def create_file(path, template):
    template = '\n'.join(template.split('\n')[1:])
    lib_name = path.split('/')[-2]
    full_lib_name = '/'.join(path.split('/')[1:-1]) + '/' + lib_name
    template = template.replace('<<lib_name>>', lib_name)
    template = template.replace('<<full_lib_name>>', full_lib_name)
    template = template.replace('<<LIB_NAME>>', full_lib_name.upper().replace('/', '_'))
    with open(path, 'w') as file:
        file.write(template)

def create_lib(path):
    # prepeare path
    parts = path.split('/')
    if parts[0] == 'lib':
        parts = parts[1:]
    path = 'lib/' + '/'.join(parts)

    # prepare folders and BUILDs
    os.system('mkdir -p '+path)
    current_path = 'lib'
    for part in parts:
        current_path += '/' + part
        os.system('touch ' + current_path + '/BUILD')

    # Add the new lib in the created folder
    lib_name = parts[-1]
    create_file(f'{path}/{lib_name}.h', h_template)
    create_file(f'{path}/{lib_name}.cc', cc_template)
    create_file(f'{path}/{lib_name}_test.cc', test_template)
    create_file(f'{path}/BUILD', BUILD_template)
    create_file(f'{path}/{lib_name}_benchmark.cc', benchmark_template)


create_lib(sys.argv[1])