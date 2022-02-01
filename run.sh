#!/bin/bash

set -e 

# clang-12 \
#   -fexperimental-new-pass-manager \
#   -fpass-plugin=/usr/lib/mull-ir-frontend-12 \
#   -g -grecord-command-line \
#   main.cc -o hello-world

# mull-runner-12 ./hello-world -ide-reporter-show-killed 
# # --ld-search-path=
# # ldd bin/core-test

rm ./bazel-bin/lib/module/hello/hello_test -f
bazel build --config=mutant //lib/module/hello:hello_test
mull-runner-12 \
  ./bazel-bin/lib/module/hello/hello_test \
  --ld-search-path=./bazel-bin/_solib_k8/ \
  --ld-search-path=/lib/x86_64-linux-gnu