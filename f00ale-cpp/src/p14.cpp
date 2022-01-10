#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <limits>

std::tuple<std::string, std::string> p14(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::string start;
    constexpr auto OFFS = 'Z'-'A'+1;

    std::vector<char> m(OFFS * OFFS);
    {
        bool havedash = false;
        std::string tmp1, tmp2;

        for(const auto c : input) {
            if(c >= 'A' && c <= 'Z') {
                if(havedash) tmp2.push_back(c);
                else tmp1.push_back(c);
            } else if( c == '-') {
                havedash = true;
            } else if(c == '\n') {
                if(!tmp1.empty()) {
                    if (havedash) {
                        m[(tmp1[0]-'A')+(tmp1[1]-'A')*OFFS] = tmp2[0];
                    } else {
                        start = tmp1;
                    }
                }
                havedash = false;
                tmp1.clear();
                tmp2.clear();
            }

        }
    }

    std::vector<int64_t> counts('Z'-'A'+1);
    for(auto c : start) counts[c-'A']++;

    std::map<std::string, int64_t> paircounts;
    for(size_t i = 0; i < start.size()-1; i++) {
        auto c1 = start[i];
        auto c2 = start[i+1];
        std::string k = {c1,c2};
        paircounts[k]++;
    }

    auto getans = [](auto && vec) {
        int64_t mi = std::numeric_limits<int64_t>::max();
        int64_t ma = std::numeric_limits<int64_t>::min();
        for(const auto v : vec) {
            if(v) {
                if(v > ma) ma = v;
                if(v < mi) mi = v;
            }
        }
        return ma - mi;
    };

    for(int varv = 0; varv < 40; varv++) {
        if(varv == 10) ans1 = getans(counts);
        decltype(paircounts) next;
        for(auto [k,v] : paircounts) {
            auto idx = (k[0]-'A') + (k[1]-'A') * OFFS;
            counts[m[idx]-'A'] +=v;
            next[std::string{k[0],m[idx]}] += v;
            next[std::string{m[idx],k[1]}] += v;
        }
        paircounts.swap(next);
    }

    ans2 = getans(counts);

    return {std::to_string(ans1), std::to_string(ans2)};
}
