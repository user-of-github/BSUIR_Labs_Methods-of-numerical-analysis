#include <iostream>
#include "./Utils/utils.hpp"
#include "./Utils/utils.cpp"
#include "./Data/data.h"
#include "./SimpleIterations/simple_iterations.hpp"


int main()
{
    const auto main_coefficients{kMatrixC * kOption + kMatrixD};
    const auto free_coefficients{kVectorB};

    const auto response {SolveBySimpleIterations(main_coefficients, free_coefficients)};

    return 0;
}
