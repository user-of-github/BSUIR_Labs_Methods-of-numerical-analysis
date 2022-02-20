#include "gauss.hpp"


bool IsNear(const double a, const double b)
{
    return std::abs(a - b) < 0.000001;
}

std::vector<std::vector<double>> GetFullSystemMatrix(const std::vector<std::vector<double>> &main_coefficients,
                                                     const std::vector<double> &free_coefficients)
{
    auto response{main_coefficients};

    for (std::size_t row = 0; row < main_coefficients.size(); ++row)
        response[row].push_back(free_coefficients.at(row));

    return response;
}

std::vector<std::size_t> Triangulate(std::vector<std::vector<double>> &full_matrix,
                                     const GaussSolvingType &solution_type)
{
    const auto subtract_rows{[&](const std::size_t from, const std::size_t which, const double ratio) -> void {
        for (std::size_t col = 0; col < full_matrix.size() + 1; ++col)
            full_matrix[from][col] -= full_matrix[which][col] * ratio;
    }};

    const auto swap_rows{[&](const std::size_t first, const std::size_t second) -> void {
        for (std::size_t col = 0; col < full_matrix.size() + 1; ++col)
            std::swap(full_matrix[first][col], full_matrix[second][col]);
    }};

    const auto find_row_with_max_main_element{[&](const std::size_t from) -> std::size_t {
        auto response{from};
        for (std::size_t row = from + 1; row < full_matrix.size(); ++row)
            if (std::abs(full_matrix[row][from]) > std::abs(full_matrix[response][from]))
                response = row;
        return response;
    }};

    auto find_position_with_max_matrix_element{[&](const std::size_t from) -> std::pair<std::size_t, std::size_t> {
        auto maximum{full_matrix[from][0]};
        for (std::size_t row = from + 1; row < full_matrix.size(); ++row)
            maximum = std::max(maximum, *std::max_element(
                    std::cbegin(full_matrix[row]),
                    --std::cend(full_matrix[row]),
                    [](const auto first, const auto second) -> bool { return std::abs(first) < std::abs(second); }
            ));

        for (std::size_t row = from + 1; row < full_matrix.size(); ++row)
            for (std::size_t col = 0; col < full_matrix.size(); ++col)
                if (full_matrix.at(row).at(col) == maximum) return {row, col};

        return {from, 0};
    }};

    std::vector<std::size_t> variables_excluding_order{};

    switch (solution_type)
    {
        case GaussSolvingType::kSchemeOfTheOnlyDivision:
            for (std::size_t row = 0; row < full_matrix.size(); ++row)
            {
                variables_excluding_order.push_back(row);
                if (IsNear(full_matrix.at(row).at(row), 0.0))
                    throw std::runtime_error("Error: Main diagonal element = 0");
                for (std::size_t lower_row = row + 1; lower_row < full_matrix.size(); ++lower_row)
                {
                    const auto ratio{full_matrix.at(lower_row).at(row) / full_matrix.at(row).at(row)};
                    subtract_rows(lower_row, row, ratio);
                }
            }
            break;
        case GaussSolvingType::kSchemeOfPartialSelection:
            for (std::size_t row = 0; row < full_matrix.size(); ++row)
            {
                const auto row_with_max_first_item{find_row_with_max_main_element(row)};
                swap_rows(row_with_max_first_item, row);
                variables_excluding_order.push_back(row);

                if (IsNear(full_matrix.at(row).at(row), 0.0))
                    throw std::runtime_error("Error: Main diagonal element = 0");

                for (std::size_t lower_row = row + 1; lower_row < full_matrix.size(); ++lower_row)
                {
                    const auto ratio{full_matrix.at(lower_row).at(row) / full_matrix.at(row).at(row)};
                    subtract_rows(lower_row, row, ratio);
                }
            }
            break;
        case GaussSolvingType::kSchemeOfFullSelection:
            for (std::size_t row = 0; row < full_matrix.size(); ++row)
            {
                const auto[row_with_max, col_with_max]{find_position_with_max_matrix_element(row)};
                variables_excluding_order.push_back(col_with_max);

                swap_rows(row_with_max, row);

                if (IsNear(full_matrix.at(row).at(col_with_max), 0.0))
                    throw std::runtime_error("Error: Main element = 0");

                for (std::size_t lower_row = row + 1; lower_row < full_matrix.size(); ++lower_row)
                {
                    const auto ratio{full_matrix[lower_row][col_with_max] / full_matrix[row][col_with_max]};
                    subtract_rows(lower_row, row, ratio);
                }
            }
            break;
    }

    return variables_excluding_order;
}

std::vector<double> GetSolutionByBackSubstitution(std::vector<std::vector<double>> &triangulated,
                                                  const std::vector<std::size_t> &variables_counting_order)
{
    std::vector<double> response(triangulated.size());

    std::size_t var_counter{0};

    for (std::size_t current_row = triangulated.size() - 1;
         current_row >= 0; --current_row) // current row in system !! (from last)
    {
        if (var_counter >= variables_counting_order.size()) break;
        // which var we can count on this row
        const auto current_variable_number{variables_counting_order.at(var_counter++)};
        response.at(current_variable_number) = triangulated[current_row].at(triangulated.size()) /
                                               triangulated.at(current_row).at(current_variable_number);

        for (int rest_row = 0; rest_row < current_row; ++rest_row)
            triangulated.at(rest_row).at(triangulated.size()) -= triangulated.at(rest_row).at(current_variable_number)
                                                                 * response.at(current_variable_number);
    }

    return response;
}

std::vector<double> SolveByGauss(const std::vector<std::vector<double>> &main_coefficients,
                                 const std::vector<double> &free_coefficients,
                                 const GaussSolvingType &solution_type)
{
    auto to_triangulate{GetFullSystemMatrix(main_coefficients, free_coefficients)};

    auto excluding_order{Triangulate(to_triangulate, solution_type)};
    std::reverse(std::begin(excluding_order), std::end(excluding_order));

    std::cout << to_triangulate;

    const auto last_row_variables_count = std::accumulate(
            std::cbegin(to_triangulate.back()),
            --std::cend(to_triangulate.back()),
            0,
            [&](const auto response, const auto current) -> std::size_t {
                return IsNear(current, 0.0) ? response : response + 1;
            });

    if (last_row_variables_count >= 2)
        throw std::runtime_error("System has infinite number of solutions");

    auto response{GetSolutionByBackSubstitution(to_triangulate, excluding_order)};

    return response;
}
