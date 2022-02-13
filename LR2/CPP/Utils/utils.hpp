#pragma once

#ifndef LR1_UTILS_HPP
#define LR1_UTILS_HPP

#include <vector>
#include <stdexcept>
#include <ostream>
#include <iostream>


template<typename ValueType>
std::vector<ValueType> &operator*=(std::vector<ValueType> &, const std::size_t);

template<typename ValueType>
std::vector<ValueType> operator*(const std::vector<ValueType> &, const std::size_t);

template<typename ValueType>
std::vector<ValueType> &operator+=(std::vector<ValueType> &, const std::vector<ValueType> &);

template<typename ValueType>
std::vector<ValueType> operator+(const std::vector<ValueType> &, const std::vector<ValueType> &);


template <typename ValueType>
std::ostream & operator << (std::ostream &, const std::vector<ValueType> &);


#endif //LR1_UTILS_HPP
