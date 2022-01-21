#include "lib/hello_time.h"
#include "main/hello_greet.h"
#include <iostream>
#include <string>
#include <glog/logging.h>
#include <ranges>
#include <vector>
#include "absl/strings/str_join.h"
#include "Eigen/Dense"
#include "nlohmann/json.hpp"

void check_cpp_20()
{
    using std::views::filter;
    using std::views::reverse;
    using std::views::transform;

    std::vector<int> numbers = {6, 5, 4, 3, 2, 1};

    // Lambda function that will provide filtering
    auto is_even = [](int n)
    { return n % 2 == 0; }; // Process our dataset

    auto results = numbers | filter(is_even) | transform([](int n)
                                                         { return n++; }) |
                   reverse;

    // Use lazy evaluation to print out the results
    for (auto v : results)
    {
        std::cout << v << " "; // Output: 3 5 7
    }
    std::cout << "cpp20 works" << std::endl;
}

void check_absl()
{
    std::vector<std::string> v = {"foo", "bar", "baz"};
    std::string s = absl::StrJoin(v, "-");
    std::cout << "absl works: " << s << std::endl;
}

void check_eigen()
{
    using Eigen::MatrixXd;
    MatrixXd m(2, 2);
    m(0, 0) = 3;
    m(1, 0) = 2.5;
    m(0, 1) = -1;
    m(1, 1) = m(1, 0) + m(0, 1);
    std::cout << m << std::endl;
    std::cout << "Eigen workds" << std::endl;
}

void check_json() {
    using json = nlohmann::json;
    json j = "{ \"happy\": true, \"pi\": 3.141 }"_json;

    // or even nicer with a raw string literal
    auto j2 = R"(
    {
        "happy": true,
        "pi": 3.141
    }
    )"_json;
    std::cout << j << std::endl;
    std::cout << "json works" << std::endl;
}

int main(int argc, char **argv)
{
    google::InitGoogleLogging(argv[0]); // GLOG_logtostderr=1 bazel run //main:hello_world

    check_absl();
    check_cpp_20();
    check_eigen();
    check_json();

    std::string who = "world";
    if (argc > 1)
    {
        who = argv[1];
    }
    std::cout << get_greet(who) << std::endl;
    print_localtime();
    return EXIT_SUCCESS;
}