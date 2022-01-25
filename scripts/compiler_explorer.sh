#!/bin/bash

if ! command -v npm &> /dev/null
then
    echo "npm not installed. Installing it.."
    sudo apt install nodejs
fi

if [ ! -d ./bazel-bin/compiler-explorer ]; then
    echo "Compiler Explorer not found. Downloading it..."
    cd ./bazel-bin
    git clone https://github.com/compiler-explorer/compiler-explorer.git
    cd compiler-explorer
    latestTag=$(git describe --tags `git rev-list --tags --max-count=1`)
    git checkout $latestTag
    npm install
    make
    cd ..
    cd ..
fi


cd ./bazel-bin/compiler-explorer
echo "Starting takes a minute..."
npm start ${@:1}