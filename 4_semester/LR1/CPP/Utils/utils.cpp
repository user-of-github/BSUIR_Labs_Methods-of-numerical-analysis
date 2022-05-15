#pragma once

#include "utils.hpp"


template<typename ValueType>
std::vector<ValueType> &operator*=(std::vector<ValueType> &nums, const std::size_t ratio)
{
    for (auto &item : nums)
        item *= ratio;

    return nums;
}

template<typename ValueType>
std::vector<ValueType> operator*(const std::vector<ValueType> &nums, const std::size_t ratio)
{
    auto response{nums};

    for (auto &item : response)
        item *= ratio;

    return response;
}

template<typename ValueType>
std::vector<ValueType> &operator+=(std::vector<ValueType> &nums, const std::vector<ValueType> &rhs)
{
    if (nums.size() != rhs.size())
        throw std::invalid_argument{"Sizes are not equal"};

    for (std::size_t counter = 0; counter < nums.size(); ++counter)
        nums.at(counter) += rhs.at(counter);

    return nums;
}

template<typename ValueType>
std::vector<ValueType> &operator-=(std::vector<ValueType> &nums, const std::vector<ValueType> &rhs)
{
    if (nums.size() != rhs.size())
        throw std::invalid_argument{"Sizes are not equal"};

    for (std::size_t counter = 0; counter < nums.size(); ++counter)
        nums.at(counter) -= rhs.at(counter);

    return nums;
}

template<typename ValueType>
std::vector<ValueType> operator+(const std::vector<ValueType> &nums1, const std::vector<ValueType> &nums2)
{
    auto response{nums1};
    response += nums2;
    return response;
}

template<typename ValueType>
std::vector<ValueType> operator-(const std::vector<ValueType> &nums1, const std::vector<ValueType> &nums2)
{
    auto response{nums1};
    response -= nums2;
    return response;
}

constexpr int GetNumberOfSignsAfterDot(const double accuracy)
{
    auto response{1};
    auto copy_accuracy{accuracy};
    while (copy_accuracy < 1)
    {
        ++response;
        copy_accuracy *= 10;
    }
    return response;
}


template<typename ValueType>
std::ostream &operator<<(std::ostream &stream, const std::vector<ValueType> &object)
{
    if constexpr (std::is_same_v<ValueType, double>)
    {
        for (const auto &item : object)
            stream << std::setw(4) << std::fixed << std::setprecision(2) << std::left << item << ' ';
        stream << '\n';
    }
    else if constexpr(std::is_same_v<ValueType, std::vector<double>>)
    {
        for (const auto &row : object)
            stream << row;
    }
    else if constexpr(std::is_same_v<ValueType, std::size_t>)
    {
        for (const auto &item : object)
            stream << item << ' ';
        stream << '\n';
    }

    return stream;
}

/*double GetNorm(const std::vector<double> &vector)
{
    return std::sqrt(std::accumulate(
            std::cbegin(vector), std::cend(vector),
            0.00,
            [](const auto response, const auto current) { return response + current * current; }
    ));
}*/

