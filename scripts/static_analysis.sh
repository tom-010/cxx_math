#!/bin/bash

# --quiet \  dont print progress
# --enable=all \  enable all checks

cppcheck . \
    --std=c++20 \
    --quiet \
    --enable=all \
    --suppressions-list=.cppcheckignore \
    --suppress=missingInclude \
    --error-exitcode=1 || exit 1

# --project=compile_commands.json \