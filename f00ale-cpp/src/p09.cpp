#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>

std::tuple<std::string, std::string> p09(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<std::string> v;
    v.reserve(200);
    {
        bool first = true;
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                if(first) {
                    v.emplace_back();
                    v.back().reserve(200);
                }
                first = false;
                v.back().push_back(c-'0');
            } else {
                first = true;
            }
        }
    }

    std::vector<std::tuple<size_t,size_t>> lowpoints;

    for(size_t y = 0; y < v.size(); y++) {
        for(size_t x = 0; x < v[y].size(); x++) {
            bool low = true;
            if(y > 0) low &= (v[y][x] < v[y-1][x]);
            if(y < (v.size()-1)) low &= (v[y][x] < v[y+1][x]);
            if(x > 0) low &= (v[y][x] < v[y][x-1]);
            if(x < (v[y].size()-1)) low &= (v[y][x] < v[y][x+1]);
            if(low) {
                ans1 += (v[y][x])+1;
                lowpoints.emplace_back(y, x);
            }
        }
    }


    std::deque<std::tuple<size_t, size_t>> q;
    std::vector<int> basinsizes;
    for(auto [ly,lx] : lowpoints) {
        basinsizes.emplace_back();
        std::deque<std::tuple<size_t, size_t>> q;
        q.emplace_back(ly,lx);
        while(!q.empty()) {
            auto [y,x] = q.front();
            q.pop_front();
            if(v[y][x]>=9) continue;
            v[y][x] = 9;
            basinsizes.back()++;
            if(y > 0) q.emplace_back(y-1,x);
            if(y < (v.size()-1)) q.emplace_back(y+1,x);
            if(x > 0) q.emplace_back(y,x-1);
            if(x < (v[y].size()-1)) q.emplace_back(y,x+1);
        }
    }
    std::sort(basinsizes.begin(), basinsizes.end(), std::greater<>());

    ans2 = basinsizes[0] * basinsizes[1] * basinsizes[2];

    return {std::to_string(ans1), std::to_string(ans2)};
}
