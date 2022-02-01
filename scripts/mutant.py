#!/usr/bin/python3
import argparse
import os 

#########################################################################################################
# Install this tool: 
# https://github.com/mull-project/mull/releases/download/0.15.1/Mull-12-0.15.1-LLVM-12.0-ubuntu-20.04.deb
#########################################################################################################


parser = argparse.ArgumentParser(description='Mutation-Testing of a module')
parser.add_argument('path', type=str, help="The path to the module where there is a _test that tests this complete module. This test is used to kill the mutants. Only the files referenced by any test are regarded.")

args = parser.parse_args()
path = args.path

parts = [p for p in path.split('/') if p]

print("building...")

target = '//' + '/'.join(parts)+':'+parts[-1]+'_test'
res = os.system(f'bazel build --config=mutant {target}')
if not res == 0:
    exit(1)

print("searching...")
path = '/'.join(parts)
command = f'''
mull-runner-12 \
  ./bazel-bin/{path}/{parts[-1]}_test \
  --ld-search-path=./bazel-bin/_solib_k8/ \
  --ld-search-path=/lib/x86_64-linux-gnu
'''.replace('\n', ' ')
print(command)
os.system(command)


# rm ./bazel-bin/lib/module/hello/hello_test -f
# bazel build --config=mutant //lib/module/hello:hello_test
# mull-runner-12 \
#   ./bazel-bin/lib/module/hello/hello_test \
#   --ld-search-path=./bazel-bin/_solib_k8/ \
#   --ld-search-path=/lib/x86_64-linux-gnu