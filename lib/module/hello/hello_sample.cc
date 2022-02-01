#include "hello.h"
#include <iostream>
#include <glog/logging.h>

using namespace module::hello;

int main(int argc, char **argv) {
    google::InitGoogleLogging(argv[0]);
    std::cout << "Hello hello: " << hello(123) << std::endl;
    return EXIT_SUCCESS;
}
