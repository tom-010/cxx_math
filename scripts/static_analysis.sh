#!/bin/bash

# --quiet \  dont print progress
# --enable=all \  enable all checks

cppcheck . \
    --std=c++20 \
    --quiet \
    --enable=all \
    --suppress=missingInclude \
    --error-exitcode=1 || exit 1