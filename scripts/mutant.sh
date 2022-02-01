#!/bin/bash

set -e 

bazel test ${@:1} --config=test