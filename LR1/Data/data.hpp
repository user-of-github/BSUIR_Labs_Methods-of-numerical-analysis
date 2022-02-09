#ifndef LR1_DATA_HPP
#define LR1_DATA_HPP

#include <vector>


const std::vector<std::vector<double>> kMatrixC{
        {0.2, 0,   0.2, 0,   0},
        {0,   0.2, 0,   0.2, 0},
        {0.2, 0,   0.2, 0,   0.2},
        {0,   0.2, 0,   0.2, 0},
        {0,   0,   0.2, 0,   0.2}};

const std::vector<std::vector<double>> kMatrixD{
        {2.33,  0.81,  0.67,  0.92,  -0.53},
        {-0.53, 2.33,  0.81,  0.67,  0.92},
        {0.92,  -0.53, 2.33,  0.81,  0.67},
        {0.67,  0.92,  -0.53, 2.33,  0.81},
        {0.81,  0.67,  0.92,  -0.53, 2.33}
};

const std::vector<double> kVectorB{4.2, 4.2, 4.2, 4.2, 4.2};

const std::size_t kOption{6};

const double kAccuracy{0.0001};


#endif //LR1_DATA_HPP
