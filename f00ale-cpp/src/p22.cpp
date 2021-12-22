#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <set>

namespace {
bool
overlap(std::tuple<int, int, int, int, int, int, bool> cube1, std::tuple<int, int, int, int, int, int, bool> cube2) {
    auto[ax1, ax2, ay1, ay2, az1, az2, aon] = cube1;
    auto[bx1, bx2, by1, by2, bz1, bz2, bon] = cube2;
    return (ax2 > bx1 && ax1 < bx2 && ay2 > by1 && ay1 < by2 && az2 > bz1 && az1 < bz2);
}
}

std::tuple<std::string, std::string> p22(const std::string &input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<std::vector<int>> v;

    {
        int num = 0;
        bool havenum = false;
        char nf = 0;
        bool neg = false;
        for (const auto c: input) {
            if (c >= '0' && c <= '9') {
                num *= 10;
                num += c - '0';
                havenum = true;
            } else if (c == 'n' || c == 'f') {
                nf = c;
            } else if (c == '-') {
                neg = true;
            } else {
                if (havenum) {
                    if(nf) {
                        v.emplace_back();
                        v.back().push_back(nf == 'n');
                        nf = 0;
                    }
                    v.back().push_back((neg ? -1 : 1) * num);
                }
                neg = false;
                havenum = false;
                num = 0;
            }
        }

    }

    for(auto & iv : v) {
        iv[2]++;
        iv[4]++;
        iv[6]++;
    }

    for(const int p : {1,2}) {
        std::vector<std::tuple<int, int, int, int, int, int, bool>> cubes;
        for (auto &iv: v) {
            //for(auto i : iv) std::cout << i << ' '; std::cout << std::endl;

            const bool on = iv[0];
            const int x1 = iv[1];
            const int x2 = iv[2];
            const int y1 = iv[3];
            const int y2 = iv[4];
            const int z1 = iv[5];
            const int z2 = iv[6];

            if ((p==2) || (x1 >= -50 && x2 <= 51)) {
                decltype(cubes) newcubes;
                auto newcube = std::make_tuple(x1, x2, y1, y2, z1, z2, on);

                for (auto cube: cubes) {
                    if (overlap(cube, newcube)) {
                        auto[bx1, bx2, by1, by2, bz1, bz2, bon] = cube;
                        if (bx1 < x1) {
                            newcubes.emplace_back(bx1, x1, by1, by2, bz1, bz2, bon);
                            bx1 = x1;
                        }

                        if (bx2 > x2) {
                            newcubes.emplace_back(x2, bx2, by1, by2, bz1, bz2, bon);
                            bx2 = x2;
                        }

                        if (by1 < y1) {
                            newcubes.emplace_back(bx1, bx2, by1, y1, bz1, bz2, bon);
                            by1 = y1;
                        }

                        if (by2 > y2) {
                            newcubes.emplace_back(bx1, bx2, y2, by2, bz1, bz2, bon);
                            by2 = y2;
                        }

                        if (bz1 < z1) {
                            newcubes.emplace_back(bx1, bx2, by1, by2, bz1, z1, bon);
                            bz1 = z1;
                        }

                        if (bz2 > z2) {
                            newcubes.emplace_back(bx1, bx2, by1, by2, z2, bz2, bon);
                            by2 = y2;
                        }

                    } else {
                        newcubes.push_back(cube);
                    }
                }

                newcubes.push_back(newcube);

                cubes.swap(newcubes);

            }
        }


        for (auto[x1, x2, y1, y2, z1, z2, on]: cubes)
            if (on)
                (p == 1 ? ans1 : ans2) += static_cast<int64_t>(x2 - x1) * (y2 - y1) * (z2 - z1);
    }
    return {std::to_string(ans1), std::to_string(ans2)};
}
