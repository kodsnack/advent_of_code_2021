#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <tuple>
#include <map>
#include <queue>
#include <set>

std::tuple<std::string, std::string> p12(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;

    const uint32_t sym_start = 0;
    const uint32_t sym_end   = 1;
    std::array<uint32_t, 32> sym_conn = {0, };
    uint32_t sym_small = 0;

    {
        bool havedash = false;
        std::string tmp1,tmp2;
        auto last_idx = sym_end;
        std::map<std::string, uint32_t> idx_tab = {{"start", sym_start}, {"end", sym_end}};
        for(const auto c : input) {
            if((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
                if(havedash) tmp2.push_back(c);
                else tmp1.push_back(c);
            } else if(c == '-') {
                havedash = true;
            } else {
                if(!tmp1.empty()) {
                    auto get_idx = [&idx_tab,&last_idx](const std::string & s) {
                        if(auto it = idx_tab.find(s); it != idx_tab.end()) return it->second;
                        auto newsym = ++last_idx;
                        idx_tab[s] = newsym;
                        return newsym;
                    };
                    auto idx1 = get_idx(tmp1);
                    auto idx2 = get_idx(tmp2);

                    sym_conn[idx1] |= (1u << idx2);
                    sym_conn[idx2] |= (1u << idx1);

                    if(idx1 > sym_end && tmp1[0] >= 'a' && tmp1[0] <= 'z') sym_small |= (1u << idx1);
                    if(idx2 > sym_end && tmp2[0] >= 'a' && tmp2[0] <= 'z') sym_small |= (1u << idx2);

                    tmp1.clear();
                    tmp2.clear();
                    havedash = false;
                }
            }
        }
    }

    auto forbit = [](uint32_t u, auto && fun) {
        uint32_t idx = 0;
        while(u) {
            if(u & 1) fun(idx);
            u>>=1;
            idx++;
        }
    };


    struct state {
        uint32_t current;
        uint32_t visited;
        bool multi;
    };

    std::queue<state> q;

    forbit(sym_conn[sym_start], [&q](uint32_t i) {q.push({i, 0, false});});
    while(!q.empty()) {
        auto s = q.front();
        q.pop();

        if(s.current == sym_end) {
            ans1++;
            continue;
        }

        if(s.current == sym_start) continue;

        auto curr = (1u << s.current);

        if(!((curr & sym_small) && (curr & s.visited))) {
            s.visited |= curr;
            forbit(sym_conn[s.current], [&q, &s](uint32_t i) { q.push({i, s.visited, s.multi}); });
        }
    }

    forbit(sym_conn[sym_start], [&q](uint32_t i) {q.push({i, 0, false});});
    while(!q.empty()) {
        auto s = q.front();
        q.pop();

        if(s.current == sym_end) {
            ans2++;
            continue;
        }

        if(s.current == sym_start) continue;

        auto curr = (1u << s.current);

        if(!((curr & sym_small) && (curr & s.visited))) {
            s.visited |= curr;
            forbit(sym_conn[s.current], [&q, &s](uint32_t i) { q.push({i, s.visited, s.multi}); });
        } else if(!s.multi) {
            forbit(sym_conn[s.current], [&q, &s](uint32_t i) { q.push({i, s.visited, true}); });
        }
    }

    return {std::to_string(ans1), std::to_string(ans2)};
}
