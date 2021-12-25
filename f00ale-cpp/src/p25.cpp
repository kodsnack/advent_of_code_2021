#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
std::tuple<std::string, std::string> p25(const std::string & input) {
    int64_t ans1 = 0;
    std::string ans2("-");
    std::vector<std::string> v;

    {
        bool first = true;
        for(const auto c : input) {
            if(c == '.' || c == 'v' || c == '>') {
                if(first) v.emplace_back();
                v.back().push_back(c);
                first = false;
            } else {
                first = true;
            }
        }
    }

    const auto rs = v.size();
    const auto cs = v[0].size();
    
    while(true) {
        int moves = 0;
        for (const auto m: {'>', 'v'}) {
            decltype(v) nv(v.size());
            for (auto &&ns: nv) ns = std::string(v[0].size(), '.');
            const auto o = (m == '>' ? 'v' : '>');
            const auto dr = (m == 'v' ? 1 : 0);
            const auto dc = (m == '>' ? 1 : 0);
            for (size_t r = 0; r < v.size(); r++) {
                for (size_t c = 0; c < v[0].size(); c++) {
                    if (v[r][c] == m) {
                        if (v[(r + dr) % rs][(c + dc) % cs] == '.') {
                            nv[(r + dr) % rs][(c + dc) % cs] = m;
                            moves++;
                        }
                        else {
                            nv[r][c] = m;
                        }
                    } else if (v[r][c] == o) nv[r][c] = o;
                }
            }
            v.swap(nv);
        }

        ans1++;
        if(moves == 0) break;
    }

    return {std::to_string(ans1), ans2};
}
