#include "lib/hello_time.h"
#include <ctime>
#include <iostream>
#include <glog/logging.h>
#include <iomanip>
#include <ctime>

void print_localtime() {
    auto t = std::time(nullptr);
    auto tm = *std::localtime(&t);
    LOG(INFO) << std::put_time(&tm, "%d-%m-%Y %H-%M-%S") << std::endl;
}