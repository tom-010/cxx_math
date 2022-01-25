#include <benchmark/benchmark.h>
#include "xtensor/xarray.hpp"
#include "xtensor/xio.hpp"
#include "xtensor/xview.hpp"

static void BM_xtensor(benchmark::State &state)
{
    xt::xarray<double> arr1{{1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0},
                            {2.0, 5.0, 7.0, 2.0, 5.0, 7.0, 2.0, 5.0, 7.0},
                            {2.0, 5.0, 7.0, 2.0, 5.0, 7.0, 2.0, 5.0, 7.0},
                            {1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0},
                            {2.0, 5.0, 7.0, 2.0, 5.0, 7.0, 2.0, 5.0, 7.0},
                            {2.0, 5.0, 7.0, 2.0, 5.0, 7.0, 2.0, 5.0, 7.0},
                            {1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0},
                            {2.0, 5.0, 7.0, 2.0, 5.0, 7.0, 2.0, 5.0, 7.0},
                            {2.0, 5.0, 7.0, 2.0, 5.0, 7.0, 2.0, 5.0, 7.0}};
    xt::xarray<double> arr2{5.0, 6.0, 7.0, 5.0, 6.0, 7.0, 5.0, 6.0, 7.0};

    // Perform setup here
    for (auto _ : state)
    {
        xt::xarray<double> res = ((arr1 * arr1 * arr1) + (arr1 * arr1 * arr1) + arr2) * arr1;
        res * res * res;
    }
}
BENCHMARK(BM_xtensor);

// Run the benchmark
BENCHMARK_MAIN();

// #define XTENSOR_USE_XSIMD causes this improvement:
// BM_xtensor       1544 ns         1544 ns       373008  <- witout simd
// BM_xtensor        677 ns          677 ns       856160  <- with simd, activated via #define XTENSOR_USE_XSIMD
// To reproduce the first line go to bazel/third_party/xtensor.BUILD and remove XTENSOR_USE_XSIMD from defines