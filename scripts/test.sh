#!/bin/bash 

set -e

bazel test --config=test ... --test_output=errors
