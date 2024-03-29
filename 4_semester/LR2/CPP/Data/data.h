#ifndef CPP_DATA_H
#define CPP_DATA_H

#include <vector>
#include "../Utils/utils.hpp"
#include "../Utils/utils.hpp"


const std::vector<std::vector<double>> kMatrixC{
        {0.01, 0.00, -0.02, 0.00, 0.00},
        {0.01, 0.01, -0.02, 0.00, 0.00},
        {0.00, 0.01, 0.01,  0.00, -0.02},
        {0.00, 0.00, 0.01,  0.01, 0.00},
        {0.00, 0.00, 0.00,  0.01, 0.01}
};

const std::vector<std::vector<double>> kMatrixD{
        {1.33,  0.21,  0.17,  0.12,  -0.13},
        {-0.13, -1.33, 0.11,  0.17,  0.12},
        {0.12,  -0.13, -1.33, 0.11,  0.17},
        {0.17,  0.12,  -0.13, -1.33, 0.11},
        {0.11,  0.67,  0.12,  -0.13, -1.33}
};

const std::vector kVectorB{1.2, 2.2, 4.0, 0.0, -1.2};

const std::size_t kOption{6};

const std::vector kInitialValues{0.0, 0.0, 0.0, 0.0, 0.0};

const double kAccuracy{0.0001};

#endif //CPP_DATA_H
