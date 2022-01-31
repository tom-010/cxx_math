#include "lib/hello_time.h"
#include "main/hello_greet.h"
#include <iostream>
#include <string>
#include <glog/logging.h>
#include <vector>
#include "absl/strings/str_join.h"
#include "Eigen/Dense"
#include "nlohmann/json.hpp"
#include "messages/address.pb.h"
#include <argparse/argparse.hpp>
#include "re2/re2.h"
#include <memory>
#include "xtensor/xarray.hpp"
#include "xtensor/xio.hpp"
#include "xtensor/xview.hpp"
#include "boost/di.hpp"
#include <string>
#include <cstddef>
#include <concepts>
 

// Declaration of the concept "Hashable", which is satisfied by any type 'T'
// such that for values 'a' of type 'T', the expression std::hash<T>{}(a)
// compiles and its result is convertible to std::size_t
template<typename T>
concept Hashable = requires(T a)
{
    { std::hash<T>{}(a) } -> std::convertible_to<std::size_t>;
};
 
struct meow {};
 
// Constrained C++20 function template:
template<Hashable T>
T f(T param) { return param; }

void check_cpp20() {
    using std::operator""s;
 
    std::cout << f("cpp 20 works"s) << '\n';    // OK, std::string satisfies Hashable
    // f(meow{}); // Error: meow does not satisfy Hashable
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

void check_json()
{
    // using json = nlohmann::json;

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

void check_proto()
{
    auto a = messages::Address();
    a.set_city("Protobuf works");
    auto s = a.SerializeAsString();

    auto a2 = messages::Address();
    a2.ParseFromString(s);

    std::cout << a2.city() << std::endl;
}

void check_re2()
{
    if (RE2::FullMatch("hello", "h.*o"))
    {
        std::cout << "re2 is working" << std::endl;
    }
}

void check_xtensor()
{
    xt::xarray<double> arr1{{1.0, 2.0, 3.0},
                            {2.0, 5.0, 7.0},
                            {2.0, 5.0, 7.0}};

    xt::xarray<double> arr2{5.0, 6.0, 7.0};

    xt::xarray<double> res = xt::view(arr1, 1) + arr2;

    std::cout << res << std::endl;
    std::cout << "xtensor works" << std::endl;
}

struct interface
{
    virtual ~interface() noexcept = default;
    virtual int get() const = 0;
};

class implementation : public interface
{
public:
    int get() const override { return 42; }
};

struct example
{
    example(std::shared_ptr<interface> i)
    {
        assert(42 == i->get());
        std::cout << "di works: " << i->get() << '\n';
    }
};

void check_di()
{
    namespace di = boost::di;
    const auto injector = di::make_injector(
        di::bind<interface>.to<implementation>());

    injector.create<std::unique_ptr<example>>();
    
}

int main(int argc, char **argv)
{
    google::InitGoogleLogging(argv[0]); // GLOG_logtostderr=1 bazel run //main:hello_world

    argparse::ArgumentParser parser("hello world");
    parser.add_argument("name")
        .help("your name")
        .default_value(std::string("world"));
    parser.add_argument("-v", "--verbose");

    try
    {
        parser.parse_args(argc, argv);
    }
    catch (const std::runtime_error &err)
    {
        std::cerr << err.what() << std::endl;
        std::cerr << parser;
        std::exit(1);
    }
    auto who = parser.get<std::string>("name");

    check_cpp20();
    check_absl();
    check_eigen();
    check_json();
    check_proto();
    check_re2();
    check_xtensor();
    check_di();


    std::cout << get_greet(who) << std::endl;
    print_localtime();
    return EXIT_SUCCESS;
}