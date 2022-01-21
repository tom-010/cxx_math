#include "gtest/gtest.h"
#include "main/hello_greet.h"

TEST(GreetingShould, ReturnHelloWorld) {
    EXPECT_EQ("Hello tom", get_greet("tom"));
    EXPECT_EQ("Hello bob", get_greet("bob"));
}