cmake_minimum_required(VERSION 3.19)
project(SimpleIterations_CPP)
set(CMAKE_CXX_STANDARD 20)
add_executable(SimpleIterations_CPP main.cpp ./Utils/utils.cpp Data/data.h SimpleIterations/simple_iterations.cpp)