#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <map>
#include <array>

std::tuple<std::string, std::string> p21(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<int> v;

    {
        int num = 0;
        bool havenum = false;
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                num *= 10;
                num += c-'0';
                havenum = true;
            } else {
                if(havenum) {
                    v.push_back(num);
                }
                havenum = false;
                num = 0;
            }

        }
    }

    const std::array<int,2> o = {v[1]-1, v[3]-1};

    {
        auto p = o;
        int d = 1;
        std::array<int,2> s = {0,0};
        int rolls = 0;
        bool turn = false;
        while (s[0] < 1000 && s[1] < 1000) {
            rolls += 3;
            int tmp = 0;
            for (int i = 0; i < 3; i++) {
                tmp += d;
                d++;
                if (d > 100) d = 1;
            }
            size_t idx = turn ? 1 : 0;
            p[idx] = (p[idx] + tmp) % 10;
            s[idx] += p[idx] + 1;
            turn = !turn;
        }

        ans1 = std::min(s[0], s[1]) * rolls;
    }

    {
        std::vector<std::tuple<int, int64_t>> combos;
        {
            std::map<int, int> tmp;
            for (int d1 = 1; d1 <= 3; d1++) {
                for (int d2 = 1; d2 <= 3; d2++) {
                    for (int d3 = 1; d3 <= 3; d3++) {
                        int s = d1 + d2 + d3;
                        tmp[s]++;
                    }
                }
            }
            for (auto[val, cnt]: tmp) combos.emplace_back(val, cnt);
        }

        std::map<std::tuple<std::array<int,2>,std::array<int,2>>, int64_t> m2;
        m2[{o,{0,0}}] = 1;
        std::array<int64_t, 2> w = {0,0};
        bool turn = false;

        while(!m2.empty()) {
            decltype(m2) nm;
            const size_t idx = turn ? 1 : 0;
            for(auto & [st, cnt] : m2) {
                auto [p,s] = st;
                for (const auto & [val, num]: combos) {
                    auto np = p;
                    auto ns = s;
                    np[idx] = (np[idx] + val) % 10;
                    ns[idx] += np[idx] + 1;
                    if(ns[idx] >= 21) w[idx] += cnt*num;
                    else nm[{np,ns}] += cnt*num;
                }
            }
            m2.swap(nm);
            turn = !turn;
        }

        ans2 = std::max(w[0], w[1]);
    }

    return {std::to_string(ans1), std::to_string(ans2)};
}
