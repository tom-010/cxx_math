#!/bin/bash 

set -e

bazel test ... --test_output=errors
