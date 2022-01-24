import argparse
import os 
import os.path

BUILD_template = '''
cc_binary(
    name = "<<name>>",
    srcs = ["<<name>>.cc"],
    deps = [
        "@com_github_google_glog//:glog",
        "@argparse//:argparse",       
    ]
)
'''

cc_template = '''
#include <glog/logging.h>
#include <argparse/argparse.hpp>

/**
 * @brief app: <<name>>
 * 
 * TODO: describe, what <<name>> does 
 *
 * @param argc 
 * @param argv 
 * @return int 
 */
int main(int argc, char **argv) {
    google::InitGoogleLogging(argv[0]);
    
    argparse::ArgumentParser parser("<<name>>");
    // TODO: specify args
    parser.add_argument("name") 
        .help("your name")
        .default_value(std::string("world"));
    parser.add_argument("-v", "--verbose");

    try {
        parser.parse_args(argc, argv);
    }
    catch (const std::runtime_error& err) {
        std::cerr << err.what() << std::endl;
        std::cerr << parser;
        std::exit(1);
    }

    // TODO: implement me
    auto who = parser.get<std::string>("name");

    return EXIT_SUCCESS;
}
'''

def create_file(path, template, name):
    template = '\n'.join(template.split('\n')[1:])
    template = template.replace('<<name>>', name)
    with open(path, 'w') as file:
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


def main():
    parser = argparse.ArgumentParser(description='Creates a new app (file with main)')
    parser.add_argument('path', help='path to the location where the cc-file will be created')
    parser.add_argument('name', help='name of the executable in the package of the path')
    args = parser.parse_args()
    create_app(args.name, args.path)

def create_app(name, path):
    os.system(f'mkdir -p {path} 2> /dev/null')
    parts = path.split('/')
    current_path = '.'
    for part in parts:
        current_path += '/' + part
        os.system('touch ' + current_path + '/BUILD')
    if os.path.isfile(path + f'/{name}.cc'):
        print(path + f'/{name}.cc already exists')
        exit(1)
    create_file(path + f'/{name}.cc', cc_template, name)
    append_BUILD_file(path + f'/BUILD', BUILD_template, name)

main()