#include "gauss.hpp"


constexpr double **GetSimilarMatrixToManipulate(const std::vector<std::vector<double>> &main_coefficients,
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

constexpr std::size_t Triangulate(double **full_matrix, const std::size_t rows)
{
    return 5;
}

std::vector<double> SolveByGauss(const std::vector<std::vector<double>> &main_coefficients,
                                 const std::vector<double> &free_coefficients)
{
    auto to_triangulate{GetSimilarMatrixToManipulate(main_coefficients, free_coefficients)};
    
}
