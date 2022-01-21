#include "lib/hello_time.h"
#include <ctime>
#include <iostream>
#include <glog/logging.h>

void print_localtime() {
    std::time_t result =std::time(nullptr);
    LOG(INFO) << std::asctime(std::localtime(&result));
}