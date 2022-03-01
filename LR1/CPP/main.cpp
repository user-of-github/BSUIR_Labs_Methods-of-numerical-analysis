#include <iostream>
#include <cfloat>
#include "./Utils/utils.hpp"
#include "./Data/data.hpp"
#include "./Gauss/gauss.hpp"


double GetNorm(const std::vector<double> &);


int main()
{
    const auto accuracy{GetNumberOfSignsAfterDot(kAccuracy)};
    auto coefficients{kMatrixC * kOption + kMatrixD};
    const auto &free_coefficients{kVectorB};


    try
    {
        std::cout << "Scheme of the only division: \n";
        const auto only_sol{SolveByGauss(coefficients, free_coefficients, GaussSolvingType::kSchemeOfTheOnlyDivision)};
        std::cout << std::setprecision(accuracy) << "Roots: " << only_sol << '\n';

        std::cout << "Scheme of partial selection: \n";
        auto part_select{SolveByGauss(coefficients, free_coefficients, GaussSolvingType::kSchemeOfPartialSelection)};
        std::cout << std::setprecision(accuracy) << "Roots: " << part_select << '\n';

        std::cout << "Scheme of full selection: \n";
        const auto full_select{SolveByGauss(coefficients, free_coefficients, GaussSolvingType::kSchemeOfFullSelection)};
        std::cout << std::setprecision(accuracy) << "Roots: " << full_select << '\n';


        coefficients.at(1).at(2) += 0.01;
        coefficients.at(0).at(4) += 0.01;
        coefficients.at(3).at(0) -= 0.01;
        coefficients.at(4).at(2) -= 0.01;

        auto sol_with_error{SolveByGauss(coefficients, free_coefficients, GaussSolvingType::kSchemeOfFullSelection)};
        std::cout << GetNorm(sol_with_error - full_select) << '\n';
    }
    catch (const std::exception &exception)
    {
        std::cout << exception.what();
    }

    return 0;
}


double GetNorm(const std::vector<double> &vector)
{
    return std::sqrt(std::accumulate(
            std::cbegin(vector), std::cend(vector),
            0.00,
            [](const auto response, const auto current) { return response + current * current; }
    ));
}
