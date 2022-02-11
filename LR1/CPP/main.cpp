#include <iostream>
#include "./Utils/utils.hpp"
#include "./Utils/utils.cpp"
#include "./Data/data.hpp"
#include "./Gauss/gauss.hpp"


int main()
{
    const auto accuracy{GetNumberOfSignsAfterDot(kAccuracy)};
    const auto coefficients{kMatrixC * kOption + kMatrixD};
    const auto &free_coefficients{kVectorB};

    const auto response{SolveByGauss(
            coefficients,
            free_coefficients,
            GaussSolutionType::kSchemeOfTheOnlySolution
    )};

    std::cout << "Solution: ";
    for (const auto &item : response)
        std::cout << std::setprecision(accuracy) << item << ' ';

    return 0;
}
