#include "gtest/gtest.h"
#include "gmock/gmock.h"
#include "hello.h"

using namespace module::hello;

TEST(hello, nothing)
{
    EXPECT_EQ(hello(25), 1);
    EXPECT_EQ(hello(20), 0);
    EXPECT_EQ(hello(21), 1); // comment out and observe an mutant survive
}
