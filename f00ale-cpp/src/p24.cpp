#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>
std::tuple<std::string, std::string> p24(const std::string &pinput) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;

    struct cmd {
        explicit cmd(std::string i) : inst(std::move(i)), reg1(0), reg2(0), num2(0) {};
        std::string inst;
        char reg1;
        char reg2;
        int num2;
    };
    std::vector<cmd> v;

    {
        int num = 0;
        bool havenum = false;
        std::string tmp;
        bool neg = false;
        for (const auto c: pinput) {
            if (c >= '0' && c <= '9') {
                num *= 10;
                num += c - '0';
                havenum = true;
            } else if (c >= 'a' && c <= 'z') {
                tmp += c;
            } else if (c == '-') {
                neg = true;
            } else {
                if (tmp.size() == 3) {
                    v.emplace_back(tmp);
                } else if (tmp.size() == 1) {
                    if (v.back().reg1) {
                        v.back().reg2 = tmp[0];
                    } else {
                        v.back().reg1 = tmp[0];
                    }
                } else if (havenum) {
                    v.back().num2 = neg ? -num : num;
                }
                neg = false;
                tmp.clear();
                havenum = false;
                num = 0;
            }

        }
    }

    std::vector<std::vector<int>> nums;

    for (auto[i, c1, c2, n2]: v) {
        if (i == "inp") nums.emplace_back();
        if (i != "inp" && c2 == 0) {
            nums.back().push_back(n2);
        }
    }

    std::vector<std::tuple<int, int, int, int64_t>> params;
    int64_t tmp_max = 1;
    for (auto n: nums) {
        // tmp_max holds maximum value that z can have to be able to reach 0
        if(n[2] == 1) tmp_max *= 26;
        else tmp_max /= 26;
        params.emplace_back(n[2], n[3], n[9], tmp_max);
    }

    auto step = [](int64_t z, int inp, int p1, int p2, int p3) {
        auto x = z % 26 + p2;
        z /= p1;
        if (x != inp) {
            z*= 26;
            z+= inp+p3;
        }
        return z;
    };

    std::unordered_map<int64_t,std::tuple<int64_t,int64_t>> zs;
    zs[0] = {0,0};
    for (auto[p1, p2, p3, max] : params) {
        decltype(zs) nsz;
        for(auto [z,n] : zs) {
            auto [minn,maxn] = n;
            for (int d = 1; d < 10; d++) {
                auto nz = step(z, d, p1, p2, p3);
                if(nz > max) continue;

                auto nmin = minn*10+d;
                auto nmax = maxn*10+d;

                if (auto it = nsz.find(nz); it != nsz.end()) {
                    auto[omin, omax] = it->second;
                    it->second = {std::min(nmin, omin), std::max(nmax, omax)};
                } else {
                    nsz[nz] = {nmin, nmax};
                }
            }
        }
        zs.swap(nsz);
    }

    std::tie(ans2,ans1) = zs[0];

    return {std::to_string(ans1), std::to_string(ans2)};
}
