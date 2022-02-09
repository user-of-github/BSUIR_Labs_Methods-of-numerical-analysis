#include <iostream>
#include "./Utils/utils.hpp"
#include "./Utils/utils.cpp"
#include "./Data/data.hpp"
#include "./Gauss/gauss.hpp"


int main()
{
    const auto coefficients{kMatrixC * kOption + kMatrixD};
    const auto &free_coefficients{kVectorB};

    const auto response{SolveByGauss(coefficients, free_coefficients)};

    std::cout << "Solution: ";
    for (const auto &item : response)
        std::cout << item << ' ';

    return 0;
}
