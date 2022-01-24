#!/bin/bash

set -e

# experimental. Follow this guide for further development: https://fbinfer.com/docs/infer-workflow/

rm compile_commands.json
./scripts/refresh_compile_commands.sh
python3 scripts/tools/infer_clean_compile_commands.py compile_commands.json ./bazel-out/infer_compile_commands.json
./scripts/infer.sh run --compilation-database ./bazel-out/infer_compile_commands.json --keep-going