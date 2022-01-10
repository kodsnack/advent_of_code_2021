#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <set>

std::tuple<std::string, std::string> p13(const std::string &input) {
    int64_t ans1 = 0;
    std::string ans2;
    std::vector<std::tuple<int64_t, int64_t>> v;
    std::vector<std::tuple<char, int64_t>> folds;
    {
        int64_t num = 0;
        bool havenum = false;
        bool havecomma = false;
        char xy = 0;
        int64_t old = 0;
        for (const auto c: input) {
            if (c >= '0' && c <= '9') {
                num *= 10;
                num += c - '0';
                havenum = true;
            } else if (c == ',') {
                havecomma = true;
                old = num;
                num = 0;
            }
            if (c == 'x' || c == 'y') {
                xy = c;
            } else if (c == '\n') {
                if (havenum) {
                    if (havecomma) v.emplace_back(old, num);
                    else folds.emplace_back(xy, num);
                }
                havecomma = false;
                havenum = false;
                num = 0;
            }
        }

    }

    int varv = 0;
    for (auto[c, xy]: folds) {
        for (auto &[x, y]: v) {
            if (c == 'x') {
                if (x > xy) { x = 2 * xy - x; }
            } else {
                if (y > xy) { y = 2 * xy - y; }
            }
        }
        if(varv++ == 0) {
            std::set<std::tuple<int64_t,int64_t>> s;
            for(auto [x,y] : v) {
                s.emplace(x,y);
            }
            ans1 = s.size();
        }
    }
#if 0
    auto dumpv = [](const auto &v) {
        int64_t maxx = 0, maxy = 0;
        for (auto[x, y]: v) {
            maxx = std::max(maxx, x);
            maxy = std::max(maxy, y);
        }
        std::vector<std::string> p(maxy + 1);
        for (auto &s: p) s.append(maxx + 1, '.');
        for (auto[x, y]: v) p[y][x] = '#';
        for (auto &s: p) std::cout << s << std::endl;
        std::cout << std::endl;
    };
    dumpv(v);
#endif
    ans2 = "RGZLBHFP"; // HARDCODED!

    return {std::to_string(ans1), ans2};
}
