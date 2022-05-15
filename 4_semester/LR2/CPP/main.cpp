#include <iostream>
#include <iomanip>
#include "./Utils/utils.hpp"
#include "./Utils/utils.cpp"
#include "./Data/data.h"
#include "./SimpleIterations/simple_iterations.hpp"


void CustomTests();


int main()
{
    /*const auto main_coefficients{kMatrixC * kOption + kMatrixD};
    const auto &free_coefficients{kVectorB};
    const auto &initial_values{kInitialValues};
    const auto &epsilon{kAccuracy};

    const auto[solution, number_of_iterations]{SolveBySimpleIterations(
            main_coefficients,
            free_coefficients,
            epsilon,
            initial_values,
            SolvingType::kSimpleIterations
    )};

    std::cout << "Solution: " << std::setprecision(6) << solution;
    std::cout << "Used " << number_of_iterations << " iterations";*/

    CustomTests();

    return 0;
}


void CustomTests()
{
    try
    {
        const auto[solution, number_of_iterations]{SolveBySimpleIterations(
                {{1.0, 1.2, 2.1, 0.9},
                 {1.2, 1.0, 1.5, 2.5},
                 {2.1, 1.5, 1.8, 1.3},
                 {0.9, 2.5, 1.3, 3.1}},
                {21.70, 27.46, 28.76, 49.72},
                0.0001,
                {1.04, 1.30, 1.45, 1.55},
                SolvingType::kSeidel
        )};
    }
    catch(const std::exception &error)
    {
        std::cout << '\t' << error.what();
    }

    //std::cout <<std::fixed << "\n\n\n\tSolution: " << solution << "| Number of iterations: " << number_of_iterations;
}