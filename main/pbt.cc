#include <gtest/gtest.h>
#include <rapidcheck/gtest.h>

#include <vector>
#include <algorithm>

RC_GTEST_PROP(PbtExample, pbt_StayTheSameOnDoubleReversal,
              (const std::vector<int> &l0)) {
  auto l1 = l0;
  std::reverse(begin(l1), end(l1));
  std::reverse(begin(l1), end(l1));
  RC_ASSERT(l0 == l1);
}
 
RC_GTEST_PROP(PbtExample, pbt_CopyOfStringIsIdenticalToOriginal, (const std::string &str)) {
  const auto strCopy = str;
  RC_ASSERT(strCopy == str);
}