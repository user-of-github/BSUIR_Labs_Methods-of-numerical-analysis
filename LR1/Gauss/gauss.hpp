#ifndef LR1_GAUSS_HPP
#define LR1_GAUSS_HPP

#include <vector>


constexpr double **GetSimilarMatrixToManipulate(const std::vector<std::vector<double>> &);

constexpr std::size_t Triangulate(double **, const std::size_t);

std::vector<double> SolveByGauss(const std::vector<std::vector<double>> &, const std::vector<double> &);


#endif //LR1_GAUSS_HPP