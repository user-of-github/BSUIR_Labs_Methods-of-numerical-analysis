#ifndef CPP_SIMPLE_ITERATIONS_HPP
#define CPP_SIMPLE_ITERATIONS_HPP

#include <vector>
#include  <numeric>
#include <iostream>


bool CheckConvergence(const std::vector<std::vector<double>> &);

std::vector<double> SolveBySimpleIterations(const std::vector<std::vector<double>> &, const std::vector<double> &);


#endif //CPP_SIMPLE_ITERATIONS_HPP
