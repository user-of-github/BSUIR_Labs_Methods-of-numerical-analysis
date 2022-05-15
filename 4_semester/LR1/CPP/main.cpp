#include <iostream>
#include "./Utils/utils.hpp"
#include "./Data/data.hpp"
#include "./Gauss/gauss.hpp"


void TestMyVariant();

void TestOtherCases();


int main()
{
    //TestMyVariant();
    TestOtherCases();

    return 0;
}


void TestMyVariant()
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
        //std::cout << GetNorm(sol_with_error - full_select) << '\n';
    }
    catch (const std::exception &exception)
    {
        std::cout << exception.what();
    }
}


void TestOtherCases()
{
    auto solution{SolveByGauss({{3, 2},
                                {1, 4}}, {1, -3}, GaussSolvingType::kSchemeOfTheOnlyDivision)};
    std::cout << "---------------\nSolution: " << solution << '\n';

    solution = SolveByGauss({{1, 1,  1},
                             {2, -1, -6},
                             {3, -2, 0}}, {2, -1, 8}, GaussSolvingType::kSchemeOfPartialSelection);
    std::cout << "---------------\nSolution: " << solution << '\n';

    solution = SolveByGauss({{1, 2, 3, 4},
                             {2, 1, 2, 3},
                             {3, 2, 1, 2},
                             {4, 3, 2, 1}},
                            {7, 6, 7, 18},
                            GaussSolvingType::kSchemeOfPartialSelection);
    std::cout << "---------------\nSolution: " << solution << '\n';

    try
    {
        solution = SolveByGauss({{1, 3, -2, -2},
                                 {-1, -2, 1, 2},
                                 {-2, -1, 3, 1},
                                 {-3, -2, 3, 3}},
                                {-3, 2, -2, -1},
                                GaussSolvingType::kSchemeOfFullSelection);
        std::cout << "---------------\nSolution: " << solution << '\n';
    }
    catch (const std::exception &exception)
    {
        std::cout << "---------------\n" << exception.what();
    }
}