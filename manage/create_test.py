import argparse
import os 
import os.path


def main():
    parser = argparse.ArgumentParser(description='Creates a new test (test-file + add to BUILD)')
    parser.add_argument('path', help='path to the location where the _test.cc-file will be created')
    parser.add_argument('name', help='name of the test in the package of the path')
    parser.add_argument('--with_mock', action='store_true', help='if set a mock-example for simple usage is generated')
    args = parser.parse_args()
    create_test(args.name, args.path, with_mock=args.with_mock)


BUILD_template = '''
cc_binary(
    name = "<<name>>",
    srcs = ["<<name>>.cc"],
    deps = [
        "@com_github_google_glog//:glog",        
    ]
)
'''

test_template = '''
#include "gtest/gtest.h"
<<mock_example>>
TEST(<<name>>, nothing) {
    <<mock_usage_example>>EXPECT_EQ(1, 1); // TODO: implement me
}
'''

mock_template = '''#include "gmock/gmock.h"

class MockExample {
 public:
  MOCK_METHOD((std::pair<bool, int>), GetPair, ());
};
'''

mock_usage_example = '''auto m = MockExample{};
    EXPECT_CALL(m, GetPair); // Note, that this has to come BEFORE the expected call
    m.GetPair().second // Something has to call it. Normally production-code
    // no assert required, as the mock is checked in the end automatically
    '''

def create_test(name, path, with_mock=False):
    os.system(f'mkdir -p {path} 2> /dev/null')
    parts = path.split('/')
    current_path = '.'
    for part in parts:
        current_path += '/' + part
        os.system('touch ' + current_path + '/BUILD')
    if os.path.isfile(path + f'/{name}.cc'):
        print(path + f'/{name}.cc already exists')
        exit(1)
    create_file(path + f'/{name}_test.cc', test_template, name, with_mock=with_mock)
    # append_BUILD_file(path + f'/BUILD', BUILD_template, name)

def create_file(path, template, name, with_mock=False):
    template = '\n'.join(template.split('\n')[1:])
    template = template.replace('<<name>>', name)
    
    the_mock_template = mock_template if with_mock else ''
    template = template.replace('<<mock_example>>', the_mock_template)

    the_mock_usage_example = mock_usage_example if with_mock else ''
    template = template.replace('<<mock_usage_example>>', the_mock_usage_example)

    with open(path, 'w') as file:
        file.write(template)

main()