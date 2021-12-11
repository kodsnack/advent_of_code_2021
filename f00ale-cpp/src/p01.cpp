#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
std::tuple<std::string, std::string> p01(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<int> v;

    {
        int num = 0;
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                num *= 10;
                num += c-'0';
            } else {
                if(num) {
                    v.push_back(num);
                }
                num = 0;
            }

        }
    }

    for(size_t i = 1; i < v.size(); i++) {
        if(v[i] > v[i-1]) ans1++;
    }

    decltype(v) v2;
    for(size_t i = 0; i < v.size()-2; i++) {
        v2.push_back(v[i] + v[i+1] + v[i+2]);
    }

    for(size_t i = 1; i < v2.size(); i++) {
        if(v2[i] > v2[i-1]) ans2++;
    }

    return {std::to_string(ans1), std::to_string(ans2)};
}
