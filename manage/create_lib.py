import os
import re
import argparse

def main():
    parser = argparse.ArgumentParser(description='Creates a new module')
    parser.add_argument('path', help='path to the module in lib')
    parser.add_argument('--with_testdata', action='store_true', help='add example test data and use it')
    args = parser.parse_args()
    create_lib(args.path, with_testdata=args.with_testdata)


def create_lib(path, with_testdata=False):
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

    # create the testdata
    testdata_include_ = testdata_include if with_testdata else ''
    testdata_usage_ = testdata_usage if with_testdata else ''
    testdata_cpp_includes_ = testdata_cpp_includes if with_testdata else ''

    test_template_ = test_template.replace('<<testdata_usage>>', testdata_usage_)
    test_template_ = test_template_.replace('<<testdata_cpp_includes>>', testdata_cpp_includes_)
    BUILD_template_ = BUILD_template.replace('<<testdata_include>>', testdata_include_)

    if with_testdata:
        os.system('mkdir -p ' + path + '/testdata')
        with open(path + '/testdata/data.txt', 'w') as f:
            f.write('filecontent\n')

    

    # Add the new lib in the created folder
    lib_name = parts[-1]
    create_file(f'{path}/{lib_name}.h', h_template)
    create_file(f'{path}/{lib_name}.cc', cc_template)
    create_file(f'{path}/{lib_name}_test.cc', test_template_)
    create_file(f'{path}/BUILD', BUILD_template_)
    create_file(f'{path}/{lib_name}_benchmark.cc', benchmark_template)
    create_file(f'{path}/{lib_name}_sample.cc', sample_template)

    
        

h_template = '''
#ifndef LIB_<<LIB_NAME>>_H_
#define LIB_<<LIB_NAME>>_H_

<<start_of_namespace>>

int <<lib_name>>(int input);

<<end_of_namespace>>

#endif
'''

cc_template = '''
#include "<<lib_name>>.h"
#include <glog/logging.h>

<<start_of_namespace>>

int <<lib_name>>(int input) {
    return input;
}

<<end_of_namespace>>
'''

testdata_include = ''',
    data = ["testdata/data.txt"]
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
    srcs = glob(["*_test.cc"]),
    deps = [
        ":<<lib_name>>",
        "@gtest//:gtest",
        "@gtest//:gtest_main",
        "@rapidcheck//:rapidcheck",
    ]<<testdata_include>>
)

cc_binary(
    name = "<<lib_name>>_benchmark",
    srcs = ["<<lib_name>>_benchmark.cc"],
    deps = [
        ":<<lib_name>>",
        "@com_google_benchmark//:benchmark",        
    ]
)

cc_binary(
    name = "<<lib_name>>_sample",
    srcs = ["<<lib_name>>_sample.cc"],
    deps = [
        ":<<lib_name>>",
        "@com_github_google_glog//:glog"
    ]
)

'''

test_template = '''
#include "gtest/gtest.h"
#include "gmock/gmock.h"
#include <rapidcheck/gtest.h>
#include "<<lib_name>>.h"<<testdata_cpp_includes>>

using namespace <<full_namespace>>;

TEST(<<lib_name>>, nothing) {
    EXPECT_EQ(0, <<lib_name>>(0)); // TODO: implement me
}

RC_GTEST_PROP(package, pbt_identity, (const int &i)) {
    // TODO: implement me. Docs: https://github.com/emil-e/rapidcheck/tree/master/doc
    RC_ASSERT(i == package(i));
}
<<testdata_usage>>
'''

testdata_cpp_includes = '''
#include <vector>
#include <string>
#include <fstream>
'''

testdata_usage = '''
std::vector<std::string> ReadLines(std::string path) {
    std::ifstream file_in(path);
    if (!file_in) throw std::invalid_argument("file not found");
    std::vector<std::string> vec;
    std::string line;
    while (std::getline(file_in, line)) vec.emplace_back(line);
    return vec;
}

TEST(<<lib_name>>, TestDataSample) {
    auto lines = ReadLines("<<lib_path>>/testdata/data.txt");
    EXPECT_EQ("filecontent", lines[0]);
}
'''


benchmark_template = '''
#include <benchmark/benchmark.h>
#include "<<lib_name>>.h"

using namespace <<full_namespace>>;

static void BM_<<lib_name>>(benchmark::State& state) {
  // Perform setup here
  for (auto _ : state) {
    // This code gets timed
    <<lib_name>>(0);
  }
}
BENCHMARK(BM_<<lib_name>>);


// Run the benchmark
BENCHMARK_MAIN();
'''

sample_template = '''
#include "<<lib_name>>.h"
#include <iostream>
#include <glog/logging.h>

using namespace <<full_namespace>>;

int main(int argc, char **argv) {
    google::InitGoogleLogging(argv[0]);
    std::cout << "Hello <<lib_name>>: " << <<lib_name>>(123) << std::endl;
    return EXIT_SUCCESS;
}
'''

def snake_case(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

def create_file(path, template):
    template = '\n'.join(template.split('\n')[1:])
    lib_name = path.split('/')[-2]
    lib_path = '/'.join(path.split('/')[:-1])
    full_lib_name = '/'.join(path.split('/')[1:-1]) + '/' + lib_name
    template = template.replace('<<lib_name>>', lib_name)
    template = template.replace('<<full_lib_name>>', full_lib_name)
    template = template.replace('<<LIB_NAME>>', full_lib_name.upper().replace('/', '_'))
    template = template.replace('<<lib_path>>', lib_path)

    parts = path.split('/')[1:-1]
    full_namespace = '::'.join([snake_case(s) for s in parts])
    start_of_namespace = 'namespace ' + full_namespace + ' {'
    end_of_namespace = '}'
    
    indent = '  '
    t = []
    indenting = False
    for line in template.split('\n'):
        if '<<end_of_namespace>>' in line:
            indenting = False
        if indenting:
            line = indent + line
        if '<<start_of_namespace>>' in line:
            indenting = True
        t.append(line)
    template = '\n'.join(t)


    
    template = template.replace('<<full_namespace>>', full_namespace)
    template = template.replace('<<start_of_namespace>>', start_of_namespace)
    template = template.replace('<<end_of_namespace>>', end_of_namespace)

    with open(path, 'w') as file:
        file.write(template)



main()