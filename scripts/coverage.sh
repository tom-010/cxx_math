#!/bin/bash

bazel coverage -s \
  --instrument_test_targets \
  --experimental_cc_coverage \
  --combined_report=lcov \
  --coverage_report_generator=@bazel_tools//tools/test/CoverageOutputGenerator/java/com/google/devtools/coverageoutputgenerator:Main \
  //...

rm bazel-out/coverage -r 2> /dev/null
mkdir -p bazel-out/coverage 2> /dev/null
genhtml -o bazel-out/coverage  bazel-out/_coverage/_coverage_report.dat

echo "Generated HTML-Output. See:"
echo "bazel-out/coverage/index.html"