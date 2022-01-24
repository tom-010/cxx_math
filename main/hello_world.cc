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
#include "messages/address.pb.h" 
#include <argparse/argparse.hpp>
#include "re2/re2.h"
#include "leveldb/db.h"


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

    // or even nicer with a raw string literal
    auto j = R"(
    {
        "happy": true,
        "pi": 3.141
    }
    )"_json;
    std::cout << j << std::endl;
    std::cout << "json works" << std::endl;
}

void check_proto() {
    auto a = messages::Address();
    a.set_city("Protobuf works");
    auto s = a.SerializeAsString();
    
    auto a2 = messages::Address();
    a2.ParseFromString(s);

    std::cout << a2.city() << std::endl;

}

void check_re2() {
    if(RE2::FullMatch("hello", "h.*o")) {
        std::cout << "re2 is working" << std::endl;
    }
}

void check_leveldb() {
    leveldb::DB* db;
    leveldb::Options options;
    options.create_if_missing = true;
    leveldb::Status status = leveldb::DB::Open(options, "/tmp/testdb", &db);
    std::cout << "leveldb ok" << std::endl;
    // https://github.com/google/leveldb/blob/main/doc/index.md
    delete db;
}

int main(int argc, char **argv)
{
    google::InitGoogleLogging(argv[0]); // GLOG_logtostderr=1 bazel run //main:hello_world

    argparse::ArgumentParser parser("hello world");
    parser.add_argument("name")
        .help("your name")
        .default_value(std::string("world"));
    parser.add_argument("-v", "--verbose");

    try {
        parser.parse_args(argc, argv);
    }
    catch (const std::runtime_error& err) {
        std::cerr << err.what() << std::endl;
        std::cerr << parser;
        std::exit(1);
    }
    auto who = parser.get<std::string>("name");


    check_absl();
    check_cpp_20();
    check_eigen();
    check_json();
    check_proto();
    check_re2();
    check_leveldb();


    std::cout << get_greet(who) << std::endl;
    print_localtime();
    return EXIT_SUCCESS;
}