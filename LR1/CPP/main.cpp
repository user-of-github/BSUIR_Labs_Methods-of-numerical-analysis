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

    try
    {
        std::cout << "Scheme of the only division: \n";
        const auto only_sol{SolveByGauss(coefficients, free_coefficients, GaussSolvingType::kSchemeOfTheOnlyDivision)};
        std::cout << std::setprecision(accuracy) << "Roots: " << only_sol << '\n';

        std::cout << "Scheme of partial selection: \n";
        const auto part_select{SolveByGauss(coefficients, free_coefficients, GaussSolvingType::kSchemeOfPartialSelection)};
        std::cout << std::setprecision(accuracy) << "Roots: " << part_select << '\n';

        std::cout << "Scheme of full selection: \n";
        const auto full_select{SolveByGauss(coefficients, free_coefficients, GaussSolvingType::kSchemeOfFullSelection)};
        std::cout << std::setprecision(accuracy) << "Roots: " << full_select;
    }
    catch (const std::exception &exception)
    {
        std::cout << exception.what();
    }

    return 0;
}
