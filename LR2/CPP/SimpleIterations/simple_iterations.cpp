#include "simple_iterations.hpp"


bool CheckConvergence(const std::vector<std::vector<double>> &main_coefficients)
{
    for (std::size_t row = 0; row < main_coefficients.size(); ++row)
    {
        const auto main_absolute{std::abs(main_coefficients.at(row).at(row))};
        std::size_t counter{0};
        const auto rest_sum_absolute{std::accumulate(
                std::begin(main_coefficients.at(row)),
                std::end(main_coefficients.at(row)),
                0.00,
                [&](const double response, const double current) -> double {
                    return counter++ != row ? response + std::abs(current) : response;
                })};

        if (main_absolute < rest_sum_absolute)
            return false;
    }

    return true;
}


std::vector<std::vector<double>> ExpressMainVariables(const std::vector<std::vector<double>> &main_coefficients,
                                                      const std::vector<double> &free_coefficients)
{
    std::vector<std::vector<double>> response{};
    response.resize(main_coefficients.size());

    for (std::size_t row = 0; row < main_coefficients.size(); ++row)
    {
        const auto full_width{main_coefficients.at(row).size() + 1};
        const auto current_variable_ratio{main_coefficients.at(row).at(row)};
        response.at(row).resize(full_width);

        response.at(row).at(0) = free_coefficients.at(row) / current_variable_ratio;

        for (std::size_t col = 1; col < full_width; ++col)
            response.at(row).at(col) =
                    col - 1 != row
                    ? -1 * main_coefficients.at(row).at(col - 1) / current_variable_ratio
                    : 0;
    }

    return response;
}


double GetError(const std::vector<double> &current_variables_set,
                const std::vector<double> &previous_variables_set)
{
    double error{0.00};
    for (std::size_t counter = 0; counter < current_variables_set.size(); ++counter)
        error = std::max(error, std::abs(current_variables_set.at(counter) - previous_variables_set.at(counter)));
    return error;
}


std::pair<std::vector<double>, std::size_t>
SolveBySimpleIterations(const std::vector<std::vector<double>> &main_coefficients,
                        const std::vector<double> &free_coefficients,
                        const double epsilon,
                        const std::vector<double> &initial_values,
                        const SolvingType &type)
{
    if (!CheckConvergence(main_coefficients))
        throw std::invalid_argument("System of linear algebraic equations does not converge");

    const auto check_error([](const std::vector<double> &current_variables_set,
                              const std::vector<double> &previous_variables_set,
                              const double epsilon) -> bool {
        return GetError(current_variables_set, previous_variables_set) <= std::abs(epsilon);
    });

    const auto copy_vectors([](const std::vector<double> &from, std::vector<double> &to) -> void {
        for (std::size_t counter = 0; counter < from.size(); ++counter)
            to.at(counter) = from.at(counter);
    });

    const auto count_variable_value([](const std::vector<double> &variable_expression,
                                       const std::vector<double> &variables_set) -> double {
        double response{variable_expression.at(0)};
        for (std::size_t counter = 1; counter < variable_expression.size(); ++counter)
            response += variable_expression.at(counter) * variables_set.at(counter - 1);
        return response;
    });

    auto previous_iteration{initial_values}; // предыдущая i-я итерация
    auto current_iteration{initial_values}; // текущая i+1-я итерация
    const auto variables_expressions{
            ExpressMainVariables(main_coefficients, free_coefficients)}; // выраженные переменные с главной диагонали

    std::size_t iterations_count{0};
    do
    {
        ++iterations_count;
        copy_vectors(current_iteration, previous_iteration);
        for (std::size_t counter = 0; const auto &variable_expression : variables_expressions)
        {
            current_iteration.at(counter) = count_variable_value(
                    variable_expression,
                    type == SolvingType::kSimpleIterations ? previous_iteration : current_iteration
            );
            ++counter;
        }
    } while (!check_error(current_iteration, previous_iteration, epsilon));

    return {current_iteration, iterations_count};
}
