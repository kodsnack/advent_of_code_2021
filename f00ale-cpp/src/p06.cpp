#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <numeric>
std::tuple<std::string, std::string> p06(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<int64_t> cnts(9), n(9);

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
                    cnts[num]++;
                }
                havenum = false;
                num = 0;
            }
        }
    }

    for (int i = 0; i < 256; i++) {
        if(i == 80) {
            ans1 = std::accumulate(cnts.begin(), cnts.end(), int64_t{0});
        }
        n.swap(cnts);

        for (int j = 0; j < 8; j++) {
            cnts[j] = n[j + 1];
        }
        cnts[8] = n[0];
        cnts[6] += n[0];
    }

    ans2 = std::accumulate(cnts.begin(), cnts.end(), int64_t{0});

    return {std::to_string(ans1), std::to_string(ans2)};
}
