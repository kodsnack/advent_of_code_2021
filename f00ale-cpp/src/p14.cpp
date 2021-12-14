#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
std::tuple<std::string, std::string> p14(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::string start;
    std::map<std::string,std::string> m;
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
                        m[tmp1] = tmp2;
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

    std::map<std::string, int64_t> paircounts;
    for(size_t i = 0; i < start.size()-1; i++) {
        auto c1 = start[i];
        auto c2 = start[i+1];
        std::string k = {c1,c2};
        paircounts[k]++;
    }

    auto countem = [&start](auto && pairs) {
        std::vector<int64_t> cnts('Z' - 'A' + 1);
        for(auto [k,v]:pairs) {
            cnts[k[0] - 'A'] += v;
            cnts[k[1] - 'A'] += v;
        }

        cnts[start.front() - 'A']++;
        cnts[start.back() - 'A']++;
        std::sort(cnts.begin(), cnts.end());
        cnts.erase(std::remove(cnts.begin(), cnts.end(), 0), cnts.end());
        return (cnts.back() - cnts.front()) / 2;
    };

    for(int varv = 0; varv < 40; varv++) {
        if(varv == 10) ans1 = countem(paircounts);
        decltype(paircounts) next;
        for(auto [k,v] : paircounts) {
            next[k[0]+m[k]] += v;
            next[m[k]+k[1]] += v;
        }
        paircounts.swap(next);
    }

    ans2 = countem(paircounts);

    return {std::to_string(ans1), std::to_string(ans2)};
}
