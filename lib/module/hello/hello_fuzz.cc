#include <cstdint>
#include <iostream>
#include "hello.h"

using namespace module::hello;

extern "C" int LLVMFuzzerTestOneInput(const uint8_t* Data, size_t Size) {
    hello(*Data);
    return 0;
}

