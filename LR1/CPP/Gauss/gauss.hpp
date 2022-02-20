#ifndef LR1_GAUSS_HPP
#define LR1_GAUSS_HPP

#include <iostream>
#include <vector>
#include <numeric>
#include "../Utils/utils.hpp"
#include "../Utils/utils.cpp"


enum class GaussSolvingType
{
    kSchemeOfTheOnlyDivision,
    kSchemeOfPartialSelection,
    kSchemeOfFullSelection
};

bool IsNear(const double, const double);


std::vector<std::vector<double>> GetFullSystemMatrix(const std::vector<std::vector<double>> &,
                                                     const std::vector<double> &);

std::vector<std::size_t> Triangulate(std::vector<std::vector<double>> &, const GaussSolvingType &);

std::vector<double> GetSolutionByBackSubstitution(std::vector<std::vector<double>> &, const std::vector<std::size_t> &);

std::vector<double> SolveByGauss(const std::vector<std::vector<double>> &,
                                 const std::vector<double> &,
                                 const GaussSolvingType &);


#endif //LR1_GAUSS_HPP
