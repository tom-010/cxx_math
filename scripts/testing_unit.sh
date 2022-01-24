#!/bin/bash

# https://github.com/bazelbuild/bazel-watcher#installation
ibazel test ... --test_arg=--gtest_filter=-*pbt_*