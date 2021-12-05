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

    std::vector<std::vector<char>> grid;
    grid.resize(maxy + 1);
    for (auto &&g: grid) {
        g.resize(maxx + 1);
    }


    for (auto[x1, y1, x2, y2]: v) {
        if (x1 == x2) {
            for (int y = std::min(y1,y2); y <= std::max(y1,y2); y++) {
                if(grid[y][x1] == 1) ans1++;
                grid[y][x1]++;
            }
        } else if (y1 == y2) {
            for (int x = std::min(x1,x2); x <= std::max(x1,x2); x++) {
                if(grid[y1][x] == 1) ans1++;
                grid[y1][x]++;
            }
        }
    }

    ans2 = ans1;

    for (auto[x1, y1, x2, y2]: v) {
        if(x1 != x2 && y1 != y2) {
            int dx = (x1 < x2 ? 1 : -1);
            int dy = (y1 < y2 ? 1 : -1);
            if(grid[y1][x1] == 1) ans2++;
            grid[y1][x1]++;
            if(grid[y2][x2] == 1) ans2++;
            grid[y2][x2]++;
            x1 += dx;
            for (int y = y1+dy; y != y2; y+=dy) {
                if(grid[y][x1] == 1) ans2++;
                grid[y][x1]++;
                x1 += dx;
            }

        }
    }


    return {std::to_string(ans1), std::to_string(ans2)};
}
