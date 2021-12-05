#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <tuple>

std::tuple<std::string, std::string> p05(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<std::tuple<int,int,int,int>> v;
    int maxx = 0, maxy = 0;
    {
        int num = 0;
        bool havenum = false;
        std::vector<int> tmp;
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                num *= 10;
                num += c-'0';
                havenum = true;
            } else {
                if(havenum) {
                    tmp.push_back(num);
                }
                havenum = false;
                num = 0;
                if(tmp.size() == 4) {
                    v.emplace_back(tmp[0], tmp[1], tmp[2], tmp[3]);
                    maxx = std::max(std::max(maxx, tmp[0]), tmp[2]);
                    maxy = std::max(std::max(maxy, tmp[1]), tmp[3]);
                    tmp.clear();
                }
            }
        }
    }
    for(auto p : {1,2}) {
        std::vector<std::vector<int>> grid;
        grid.resize(maxy + 1);
        for (auto &&g: grid) {
            g.resize(maxx + 1);
        }

        for (auto[x1, y1, x2, y2]: v) {
            int dx = (x1 < x2 ? 1 : -1);
            int dy = (y1 < y2 ? 1 : -1);
            if (x1 == x2) {
                for (int y = y1+dy; y != y2; y+=dy) grid[y][x1]++;
                grid[y1][x1]++;
                grid[y2][x2]++;
            } else if (y1 == y2) {
                for (int x = x1+dx; x != x2; x+=dx) grid[y1][x]++;
                grid[y1][x1]++;
                grid[y2][x2]++;
            } else {
                if(p == 2) {
                    grid[y1][x1]++;
                    grid[y2][x2]++;
                    x1 += dx;
                    for (int y = y1+dy; y != y2; y+=dy) {
                        grid[y][x1]++;
                        x1 += dx;
                    }
                }
            }
        }

        int cnt = 0;
        for (auto &&g: grid) {
            for (auto i: g) {
                if (i > 1) cnt++;

            }
        }

        (p == 1 ? ans1 : ans2) = cnt;
    }
    return {std::to_string(ans1), std::to_string(ans2)};
}
