#include "lib/hello_time.h"
#include "main/hello_greet.h"
#include <iostream>
#include <string>
#include <glog/logging.h>

int main(int argc, char** argv) {
    google::InitGoogleLogging(argv[0]); // GLOG_logtostderr=1 bazel run //main:hello_world

    std::string who = "world";
    if (argc > 1) {
        who = argv[1];
    }
    std::cout << get_greet(who) << std::endl;
    print_localtime();
    return EXIT_SUCCESS;
}