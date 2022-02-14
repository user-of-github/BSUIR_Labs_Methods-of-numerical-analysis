#include <iostream>
#include <iomanip>
#include "./Utils/utils.hpp"
#include "./Utils/utils.cpp"
#include "./Data/data.h"
#include "./SimpleIterations/simple_iterations.hpp"


int main()
{
    const auto main_coefficients{kMatrixC * kOption + kMatrixD};
    const auto &free_coefficients{kVectorB};
    const auto &initial_values{kInitialValues};
    const auto &epsilon{kAccuracy};

    std::cout << main_coefficients << '\n';

    const auto[solution, number_of_iterations]{SolveBySimpleIterations(
            main_coefficients,
            free_coefficients,
            epsilon,
            initial_values,
            SolvingType::kSimpleIterations
    )};

    std::cout << "Solution: " << std::setprecision(6) << solution;
    std::cout << "Used " << number_of_iterations << " iterations";

    return 0;
}
