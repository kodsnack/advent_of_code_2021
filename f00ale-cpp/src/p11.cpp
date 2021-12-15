#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>

std::tuple<std::string, std::string> p11(const std::string & input) {
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

    for(int varv=0; varv < 10000; varv++) {
        std::deque<std::tuple<size_t,size_t>> q;
        for (size_t y = 0; y < v.size(); y++) {
            for (size_t x = 0; x < v[y].size(); x++) {
                v[y][x]++;
                if(v[y][x]>9) {
                    v[y][x]=0;
                    q.emplace_back(y,x);
                }
            }
        }

        int flashes = 0;
        while(!q.empty()) {
            flashes++;
            auto[y, x] = q.front();
            q.pop_front();
            for (int dy = -1; dy <= 1; dy++) {
                for (int dx = -1; dx <= 1; dx++) {
                    if (dy == 0 && dx == 0) continue;
                    if (static_cast<int>(y) + dy < 0 || y + dy >= v.size()) continue;
                    if (static_cast<int>(x) + dx < 0 || x + dx >= v[y].size()) continue;
                    if (v[y + dy][x + dx] != 0) {
                        v[y + dy][x + dx]++;
                    }
                    if (v[y + dy][x + dx] > 9) {
                        v[y + dy][x + dx] = 0;
                        q.emplace_back(y + dy, x + dx);
                    }


                }
            }
        }
        if(varv < 100) ans1 += flashes;

        if(flashes == 100) {
            ans2 = varv+1;
            break;
        }
    }


    return {std::to_string(ans1), std::to_string(ans2)};
}
