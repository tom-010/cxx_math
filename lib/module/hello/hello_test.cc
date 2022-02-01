#include "gtest/gtest.h"
#include "gmock/gmock.h"
#include <rapidcheck/gtest.h>
#include "hello.h"

using namespace module::hello;

TEST(hello, nothing) {

    EXPECT_EQ(1, hello(25));
    EXPECT_EQ(0, hello(20));
    EXPECT_EQ(1, hello(21));

}

