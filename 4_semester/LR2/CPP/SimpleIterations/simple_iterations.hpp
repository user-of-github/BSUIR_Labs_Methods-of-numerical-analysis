#ifndef CPP_SIMPLE_ITERATIONS_HPP
#define CPP_SIMPLE_ITERATIONS_HPP

#include <vector>
#include  <numeric>
#include <iostream>
#include "../Utils/utils.hpp"


enum class SolvingType
{
    kSimpleIterations,
    kSeidel
};

bool CheckConvergence(const std::vector<std::vector<double>> &); // сходимость

std::vector<std::vector<double>> ExpressMainVariables(const std::vector<std::vector<double>> &,
                                                      const std::vector<double> &);

double GetError(const std::vector<double> &, const std::vector<double> &); // погрешность


std::pair<std::vector<double>, std::size_t> SolveBySimpleIterations(const std::vector<std::vector<double>> &,
                                                                    const std::vector<double> &,
                                                                    const double,
                                                                    const std::vector<double> &,
                                                                    const SolvingType &);


#endif //CPP_SIMPLE_ITERATIONS_HPP
