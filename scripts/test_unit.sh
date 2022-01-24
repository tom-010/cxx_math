#!/bin/bash 

set -e

bazel test ... --test_output=errors --test_arg=--gtest_filter=-*pbt_*
