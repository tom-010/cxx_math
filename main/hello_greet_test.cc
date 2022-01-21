#include "gtest/gtest.h"
#include "gmock/gmock.h"
#include "main/hello_greet.h"
#include <iostream>

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
}