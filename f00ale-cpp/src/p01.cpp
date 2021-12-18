#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
std::tuple<std::string, std::string> p01(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;

    {
        int num = 0;
        int l1 = 0, l2 = 0, l3 = 0;
        int cnt = 0;
        bool havenum = false;
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                num *= 10;
                num += c-'0';
                havenum = true;
            } else if(havenum) {
                cnt++;

                if(cnt > 1) {
                    if(num > l1) ans1++;
                }
                if(cnt > 3) {
                    if(num > l3) ans2++; // N_i + N_i-1 + N_i-2 > N_i-1 + N_i-2 + N_i-3 -> N_i > N_i-3
                }
                l3 = l2;
                l2 = l1;
                l1 = num;
                num = 0;
            }

        }
    }

    return {std::to_string(ans1), std::to_string(ans2)};
}
