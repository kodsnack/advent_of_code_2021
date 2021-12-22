cmake_minimum_required(VERSION 3.18)
project(aoc21_f00ale)

set(CMAKE_CXX_STANDARD 17)

if(${SANITIZE})
add_compile_options(-fsanitize=address,leak)
add_link_options(-fsanitize=address,leak)
endif()

add_compile_options(-Wall -Wextra -march=native)

#if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
#    message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
#    file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/v0.15/conan.cmake"
#            "${CMAKE_BINARY_DIR}/conan.cmake"
#            TLS_VERIFY ON)
#endif()
#
#include(${CMAKE_BINARY_DIR}/conan.cmake)
#
#conan_cmake_run(REQUIRES benchmark/1.5.2
#        BASIC_SETUP CMAKE_TARGETS NO_OUTPUT_DIRS
#        BUILD missing)

add_library(aoc21_problems OBJECT
        src/p01.cpp
        src/p02.cpp
        src/p03.cpp
        src/p04.cpp
        src/p05.cpp
        src/p06.cpp
        src/p07.cpp
        src/p08.cpp
        src/p09.cpp
        src/p10.cpp
        src/p11.cpp
        src/p12.cpp
        src/p13.cpp
        src/p14.cpp
        src/p15.cpp
        src/p16.cpp
        src/p17.cpp
        src/p18.cpp
        src/p19.cpp
        src/p20.cpp
        src/p21.cpp
        src/p22.cpp
#        src/p23.cpp
#        src/p24.cpp
#        src/p25.cpp
        )

add_executable(aoc21 src/main.cpp)
target_link_libraries(aoc21 PRIVATE aoc21_problems)

#add_executable(bench src/bench.cpp)
#target_link_libraries(bench PRIVATE aoc21_problems CONAN_PKG::benchmark)
