#include <benchmark/benchmark.h>
#include "hello.h"

using namespace module::hello;

static void BM_hello(benchmark::State& state) {
  // Perform setup here
  for (auto _ : state) {
    // This code gets timed
    hello(0);
  }
}
BENCHMARK(BM_hello);


// Run the benchmark
BENCHMARK_MAIN();
