cmake_minimum_required(VERSION 3.19)
project(CPP)
set(CMAKE_CXX_STANDARD 20)

add_executable(main main.cpp ./Utils/utils.cpp Data/data.h SimpleIterations/simple_iterations.cpp)