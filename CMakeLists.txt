cmake_minimum_required(VERSION 3.10)
project(DarkAgencySimulations VERSION 1.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3 -Wall -Wextra")

# 1. El binario independiente (el que corriste antes)
add_executable(rae_hr_simulation src/engine/main.cpp)

# 2. El módulo de Python (La magia negra)
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(dark_agency src/bindings/pybind_sim.cpp)
