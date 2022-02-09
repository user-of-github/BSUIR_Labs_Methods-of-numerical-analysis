#include "gauss.hpp"


double **GetSimilarMatrixToManipulate(const std::vector<std::vector<double>> &main_coefficients,
                                      const std::vector<double> &free_coefficients)
{
    const auto rows{main_coefficients.size()};

    auto response{new double *[rows]};
    for (std::size_t counter = 0; counter < rows; ++counter)
        response[counter] = new double[rows + 1];

    for (std::size_t row = 0; row < rows; ++row)
        for (std::size_t col = 0; col < rows; ++col)
            response[row][col] = main_coefficients.at(row).at(col);

    for (std::size_t row = 0; row < rows; ++row)
        response[row][rows] = free_coefficients.at(row);

    return response;
}

void Triangulate(double **full_matrix, const std::size_t rows)
{
    const auto subtract_rows{[&](const std::size_t from, const std::size_t which, const double ratio) -> void {
        for (std::size_t col = 0; col < rows + 1; ++col)
            full_matrix[from][col] -= full_matrix[which][col] * ratio;
    }};

    for (std::size_t row = 0; row < rows; ++row)
    {
        for (std::size_t lower_row = row + 1; lower_row < rows; ++lower_row)
        {
            const auto ratio{full_matrix[lower_row][row] / full_matrix[row][row]};
            subtract_rows(lower_row, row, ratio);
        }
    }
}

std::vector<double> GetSolutionByBackSubstitution(double **triangulated, const std::size_t variables_count)
{
    std::vector<double> response(variables_count);
    for (int current_x = (int) variables_count - 1; current_x >= 0; --current_x)
    {
        response.at(current_x) = triangulated[current_x][variables_count] / triangulated[current_x][current_x];
        for (int rest_row = 0; rest_row < current_x; ++rest_row)
            triangulated[rest_row][variables_count] -= triangulated[rest_row][current_x] * response.at(current_x);
    }

    return response;
}

std::vector<double> SolveByGauss(const std::vector<std::vector<double>> &main_coefficients,
                                 const std::vector<double> &free_coefficients)
{
    const std::size_t variables_count{main_coefficients.size()};
    auto to_triangulate{GetSimilarMatrixToManipulate(main_coefficients, free_coefficients)};

    Triangulate(to_triangulate, variables_count);
    auto response{GetSolutionByBackSubstitution(to_triangulate, variables_count)};
    FreeMemoryFromTemporaryMatrix(to_triangulate, variables_count);

    return response;
}

void FreeMemoryFromTemporaryMatrix(double **matrix, const std::size_t rows)
{
    for (std::size_t row = 0; row < rows; ++row)
        delete[] matrix[row];

    delete[] matrix;
}

void Print(const double **matrix, const std::size_t rows)
{
    const auto cols{rows + 1};
    for (std::size_t row = 0; row < rows; ++row)
    {
        for (std::size_t col = 0; col < cols; ++col)
            std::cout << std::setw(3) << std::fixed << std::setprecision(4) << std::left << matrix[row][col] << ' ';
        std::cout << '\n';
    }
    std::cout << "___________________________________________________\n";
}
