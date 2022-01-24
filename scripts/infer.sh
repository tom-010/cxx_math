#!/bin/bash

# infer is a static analysis tool: https://fbinfer.com/docs/getting-started/
# this scripts just makes running easier. For checking the codebase use `./scripts/check_infer.sh`

if [ ! -L ./bazel-bin/infer ]; then
    echo "Infer-tool not found. Downloading it..."
    export VERSION=1.1.0
    curl -sSL "https://github.com/facebook/infer/releases/download/v$VERSION/infer-linux64-v$VERSION.tar.xz" | tar -C ./bazel-bin/ -xJ
    cd bazel-bin
    ln -s "infer-linux64-v$VERSION/bin/infer" infer
    cd ..
fi

./bazel-bin/infer -o bazel-out/infer-out ${@:1}