#!/bin/bash

set -e 

if [ ! -d ./bazel-bin/cling ]; then
    echo "Cling not found. Downloading it..."
    cd ./bazel-bin
    wget "https://root.cern.ch/download/cling/cling_2020-11-05_ROOT-ubuntu2004.tar.bz2"
    tar -xvjf cling_2020-11-05_ROOT-ubuntu2004.tar.bz2
    mv cling_2020-11-05_ROOT-ubuntu2004 cling
    rm cling_2020-11-05_ROOT-ubuntu2004.tar.bz2
    cd ..
fi

./bazel-bin/cling/bin/cling