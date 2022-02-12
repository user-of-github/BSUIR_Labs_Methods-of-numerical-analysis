#include "simple_iterations.hpp"


bool CheckConvergence(const std::vector<std::vector<double>> &main_coefficients)
{
    for (std::size_t row = 0; row < main_coefficients.size(); ++row)
    {
        const auto main_absolute{std::abs(main_coefficients.at(row).at(row))};
        std::size_t counter{0};
        const auto rest_absolute{std::accumulate(
                std::begin(main_coefficients.at(row)),
                std::end(main_coefficients.at(row)),
                0.00,
                [&](const double response, const double current) -> double {
                    return counter++ != row ? response + std::abs(current) : response;
                })};

        if (main_absolute < rest_absolute)
            return false;
    }

    return true;
}


std::vector<double> SolveBySimpleIterations(const std::vector<std::vector<double>> &main_coefficients,
                                            const std::vector<double> &free_coefficients)
{
    if (!CheckConvergence(main_coefficients))
        throw std::invalid_argument("System of linear algebraic equations does not converge");

    return {};
}