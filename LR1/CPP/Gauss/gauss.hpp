#ifndef LR1_GAUSS_HPP
#define LR1_GAUSS_HPP

#include <iostream>
#include <vector>
#include <iomanip>


enum class GaussSolutionType
{
    kSchemeOfTheOnlySolution,
    kSchemeOfPartialSelection,
    kSchemeOfFullSelection
};


double **GetSimilarMatrixToManipulate(const std::vector<std::vector<double>> &);

void Triangulate(double **, const std::size_t, const GaussSolutionType &);

std::vector<double> GetSolutionByBackSubstitution(double **, const std::size_t);

std::vector<double> SolveByGauss(const std::vector<std::vector<double>> &,
                                 const std::vector<double> &,
                                 const GaussSolutionType & = GaussSolutionType::kSchemeOfTheOnlySolution);

void FreeMemoryFromTemporaryMatrix(double **, const std::size_t);

void Print(const double **, const std::size_t);


#endif //LR1_GAUSS_HPP