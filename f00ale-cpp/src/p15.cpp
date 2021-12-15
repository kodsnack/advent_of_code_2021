#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>
#include <tuple>
#include <limits>

std::tuple<std::string, std::string> p15(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<std::string> v;

    {
        bool first = true;
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                if(first) v.emplace_back();
                first = false;
                v.back().push_back(c-'0');
            } else {
                if(c=='\n') first = true;
            }

        }
    }


    for(auto p : {1,2}) {
        if(p == 2) {
            decltype(v) n(5*v.size(), std::string(5*v[0].size(), 0));
            for(int dy = 0; dy < 5; dy++) {
                for(int dx = 0; dx < 5; dx++) {
                    for(int y = 0; y < v.size(); y++) {
                        for(int x = 0; x < v[y].size(); x++) {
                            auto tmp = v[y][x]+dx+dy;
                            while(tmp >= 10) tmp-=9;
                            n[y+dy*v.size()][x+dx*v[y].size()] = tmp;
                        }
                    }
                }
            }
            v.swap(n);
        }
        std::vector<std::vector<int>> risks(v.size(), std::vector<int>(v[0].size(), std::numeric_limits<int>::max()));

        std::deque<std::tuple<int, int, int>> q;
        q.emplace_back(0, 0, 0);
        while (!q.empty()) {
            auto[y, x, w] = q.front();
            q.pop_front();
            if (w > risks.back().back()) continue;
            if (y < 0 || y >= v.size()) continue;
            if (x < 0 || x >= v[0].size()) continue;
            if (w < risks[y][x]) {
                risks[y][x] = w;
                if (y - 1 >= 0) q.emplace_back(y - 1, x, w + v[y - 1][x]);
                if (y + 1 < v.size()) q.emplace_back(y + 1, x, w + v[y + 1][x]);
                if (x - 1 >= 0) q.emplace_back(y, x - 1, w + v[y][x - 1]);
                if (x + 1 < v[0].size()) q.emplace_back(y, x + 1, w + v[y][x + 1]);
            }
        }

        (p == 1 ? ans1 : ans2)  = risks.back().back();
    }
    return {std::to_string(ans1), std::to_string(ans2)};
}
