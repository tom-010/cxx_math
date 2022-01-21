#include <benchmark/benchmark.h>
#include "main/hello_greet.h"

static void BM_get_greet(benchmark::State& state) {
  // Perform setup here
  for (auto _ : state) {
    // This code gets timed
    get_greet("tom");
  }
}
BENCHMARK(BM_get_greet);


// Run the benchmark
BENCHMARK_MAIN();