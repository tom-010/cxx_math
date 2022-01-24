import argparse
import os 
import os.path
import re

def main():
    parser = argparse.ArgumentParser(description='Creates a new message in an given lib')
    parser.add_argument('path', help='path to the lib')
    parser.add_argument('message_name', help='name of the message')
    args = parser.parse_args()
    create_message(args.path, args.message_name)

def create_message(path, name):
    path = '/'.join([part for part in path.split('/') if part])
    if not path.endswith('/messages'):
        path += '/messages'

    os.system(f'mkdir -p {path} 2> /dev/null')
    parts = path.split('/')
    current_path = '.'
    for part in parts:
        current_path += '/' + part
        os.system('touch ' + current_path + '/BUILD')
    if os.path.isfile(path + f'/{snake_case(name)}.proto'):
        print(path + f'/{snake_case(name)}.proto already exists')
        exit(1)

    create_or_append(path + f'/{snake_case(name)}.proto', message_template, name)

    template = BUILD_template
    if not file_contains(path + '/BUILD', 'proto_library'):
        template = 'load("@rules_proto//proto:defs.bzl", "proto_library")\n\n' + template
    create_or_append(path + '/BUILD', template, name)


def file_contains(path, needle):
    with open(path, 'r') as file:
        return needle in file.read()

BUILD_template = '''
# Convention:
# A cc_proto_library that wraps a proto_library named <<snake_case_name>>_proto
# should be called <<snake_case_name>>_cc_proto.
cc_proto_library(
    name = "<<snake_case_name>>_cc_proto",
    deps = [":<<snake_case_name>>_proto"],
    visibility = ["//main:__pkg__"]
)

# Conventions:
# 1. One proto_library rule per .proto file.
# 2. A file named <<snake_case_name>>.proto will be in a rule named <<snake_case_name>>_proto.
proto_library(
    name = "<<snake_case_name>>_proto",
    srcs = ["<<snake_case_name>>.proto"],
    deps = [
        # ":other", # Dep on other messages in this file
        # Well known protos should be included as deps in the
        # proto_library rules of the source files importing them.
        # A list of all @com_google_protobuf well known protos can
        # seen with:
        # `bazel query 'kind(proto_library, @com_google_protobuf//:all)'`
        "@com_google_protobuf//:any_proto", # TODO: this is only required when we use the message-type google.protobuf.Any. You may want to delete this
    ],
)

# Example: create another library, that is only used to include
# proto_library(
#     name = "other_proto",
#     srcs = ["other.proto"],
#     deps = [],
# )

'''

message_template = '''
syntax = "proto3";

package <<package>>;

// Always import protos with a full path relative to the WORKSPACE file.
// import "<<dir_path>>/other_message.proto";

// Well known protos should be imported with full path relative to
// @com_google_protobuf.
import "google/protobuf/any.proto";

message <<name>> {
  int32 id = 1;
  string name = 2;
  google.protobuf.Any stuff = 3; // generic type
  // ImportedType other = 4; // imported user-defined type
}
'''

def create_or_append(path, template, name):
    dir_path = '/'.join(path.split('/')[:-1])
    template = '\n'.join(template.split('\n')[1:])
    template = template.replace('<<name>>', name)
    template = template.replace('<<dir_path>>', dir_path)
    template = template.replace('<<snake_case_name>>', snake_case(name))
    package = '.'.join(dir_path.replace('lib/', '').split('/'))
    template = template.replace('<<package>>', package)
    with open(path, 'a') as file:
        file.write(template)

def append_BUILD_file(path, template, name):
    template = '\n'.join(template.split('\n')[1:])
    template = template.replace('<<name>>', name)
    

    with open(path, 'r') as file:
        empty = 'load' not in file.read()


    if empty:
        template = 'load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library", "cc_test")\n\n' + template
    else:
        template = '\n\n' + template

    with open(path, 'a') as f:
        f.write(template)


def snake_case(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

main()