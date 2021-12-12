#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <limits>

std::tuple<std::string, std::string> p07(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<int> v;
    {
        int num = 0;
        bool havenum = false;
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                num *= 10;
                num += c-'0';
                havenum = true;
            } else {
                if(havenum) {
                    v.push_back(num);
                }
                havenum = false;
                num = 0;
            }

        }
    }

    ans1 = std::numeric_limits<decltype(ans1)>::max();
    ans2 = std::numeric_limits<decltype(ans2)>::max();

    for(auto i : v) {
        int tmp1 = 0, tmp2 = 0;
        for(auto j : v) {
            auto x = std::abs(i-j);
            tmp1 += x;
            tmp2 += (x*(x+1))/2;
        }
        if(tmp1 < ans1) ans1 = tmp1;
        if(tmp2 < ans2) ans2 = tmp2;
    }

    return {std::to_string(ans1), std::to_string(ans2)};
}
