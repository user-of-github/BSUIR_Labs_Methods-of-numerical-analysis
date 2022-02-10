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
std::vector<ValueType> operator+(const std::vector<ValueType> &nums1, const std::vector<ValueType> &nums2)
{
    auto response{nums1};
    response += nums2;
    return response;
}

constexpr int GetNumberOfSignsAfterDot(const double accuracy)
{
    auto response {1};
    auto copy_accuracy{accuracy};
    while (copy_accuracy < 1)
    {
        ++response;
        copy_accuracy *= 10;
    }
    return response;
}
