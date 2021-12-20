#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <tuple>

std::tuple<std::string, std::string> p20(const std::string &input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<std::string> v;

    {
        bool first = true;
        for (const auto c: input) {
            if (c == '.' || c == '#') {
                if (first) {
                    v.emplace_back();
                    first = false;
                }
                v.back().push_back(c);
            } else if (c == '\n') {
                first = true;
            }

        }
    }


    for (auto p: {1, 2}) {
        char outside = '.';

        std::vector<std::string> img(v.size() - 1);
        for (size_t i = 0; i < img.size(); i++) img[i] = v[i + 1];

        for (int varv = 0; varv < (p == 1 ? 2 : 50); varv++) {
            char newoutside = v[0][outside == '.' ? 0 : 511];

            std::vector<std::string> newimg(img.size() + 4);
            for (auto &s: newimg) s.append(img[0].size() + 4, newoutside);

            std::vector<std::string> tmpimg(img.size() + 4);
            tmpimg[0].append(img[0].size() + 4, outside);
            tmpimg[1].append(img[0].size() + 4, outside);
            for (size_t i = 0; i < img.size(); i++) {
                tmpimg[i + 2].append(2, outside);
                tmpimg[i + 2].append(img[i]);
                tmpimg[i + 2].append(2, outside);
            }
            tmpimg[tmpimg.size() - 2].append(img[0].size() + 4, outside);
            tmpimg[tmpimg.size() - 1].append(img[0].size() + 4, outside);

            for (size_t y = 1; y < newimg.size() - 1; y++) {
                for (size_t x = 1; x < newimg[y].size() - 1; x++) {
                    size_t idx = 0;
                    for (int dy = -1; dy <= 1; dy++) {
                        for (int dx = -1; dx <= 1; dx++) {
                            idx <<= 1;
                            idx |= (tmpimg[y + dy][x + dx] == '#' ? 1 : 0);
                        }
                    }
                    newimg[y][x] = v[0][idx];
                }
            }

            img.swap(newimg);
            outside = newoutside;
        }
        int64_t tmp = 0;
        for (auto &s: img) for (auto c: s) if (c == '#') tmp++;

        (p == 1 ? ans1 : ans2) = tmp;
    }

    return {std::to_string(ans1), std::to_string(ans2)};
}
