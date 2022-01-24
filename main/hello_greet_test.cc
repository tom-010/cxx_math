#include "gtest/gtest.h"
#include "gmock/gmock.h"
#include "main/hello_greet.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>

class MyMock {
 public:
  MOCK_METHOD((std::pair<bool, int>), GetPair, ());
};



TEST(MockShould, ReactProperly) {
    auto m = MyMock{};
    EXPECT_CALL(m, GetPair);
    std::cout << m.GetPair().second << std::endl;
    
}

TEST(GreetingShould, ReturnHelloWorld) {
    EXPECT_EQ("Hello tom", get_greet("tom"));
    EXPECT_EQ("Hello bob", get_greet("bob"));
    EXPECT_EQ(2, 2);
}


std::vector<std::string> ReadLines(std::string path) {
    std::vector<std::string> vec;

    std::ifstream file_in(path);
    system("ls main");
    if (!file_in) 
        throw std::invalid_argument("file not found");

    std::string line;
    while (std::getline(file_in, line))
    {
        vec.emplace_back(line);
    }
    return vec;
}

TEST(File, Read) {
    auto lines = ReadLines("main/testdata/somefile.txt");
    std::cout << lines[0] << std::endl;
}