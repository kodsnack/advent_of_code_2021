#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>
#include <tuple>
#include <set>
std::tuple<std::string, std::string> p23(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;

    std::string start;
    {
        for(const auto c : input) {
            if(c == '.' || (c >= 'A' && c <= 'D')) {
                start += c;
            }
        }
    }

    static constexpr std::array<int, 27> xvals{
        0,1,2,3,4,5,6,7,8,9,10,
        2, 4, 6, 8,
        2, 4, 6, 8,
        2, 4, 6, 8,
        2,4,6,8};

    auto canmove = [](const std::string & s, char c, int from, int to) -> int {
        if(c == '.') return 0;
        if(s[to] != '.') return 0;
        if(from == to) return 0;
        if(to == 2 || to == 4 || to == 6 || to == 8) return 0; // cannot stop outside door
        if(from <= 10 && to <= 10) return 0; // trying to move from hallway to hallway
        auto idx = c - 'A';
        if(to > 10 && (to-11)%4 != idx) return 0; // not trying to move into correct room
        if(to > 10) {
            // if moving to pit - pit must be empty or only occupied by correct
            auto tt = to+4;
            while(tt < static_cast<int>(s.size())) {
                if(s[tt] != c) return 0;
                tt+=4;
            }
        }
        if(from > 10 && to > 10 && (to-11)%4 == (from-11%4)) return 0; // no movement within room
        if(from >= 15 && s[from-4] != '.') return 0; // blocked in
        auto fx = xvals[from];
        auto tx = xvals[to];
        if(fx > tx) {
            while(fx > tx) if(s[--fx] != '.') return 0;
        } else if(fx < tx) {
            while(fx < tx) if(s[++fx] != '.') return 0;
        }

        fx = xvals[from];
        tx = xvals[to];
        int steps = 0;
        if(fx > tx) {
            steps = fx - tx;
        } else {
            steps = tx - fx;
        }
        if(to > 10) {
            steps += 1 + (to-11)/4;
        }
        if(from > 10) {
            steps += 1 + (from-11)/4;
        }

        return steps;
    };


    for(auto p : {1,2}) {
        using type = std::tuple<int, std::string>;
        std::priority_queue<type, std::vector<type>, std::greater<>> q;

        if(p == 1) {
            q.emplace(0, start);
        } else {
            q.emplace(0, start.substr(0,15) + "DCBADBAC" + start.substr(15));
        }
        const std::string GOAL = (p == 1) ? "...........ABCDABCD" : "...........ABCDABCDABCDABCD";

        std::set<std::string> seen;
        while (!q.empty()) {
            auto[score, st] = q.top();
            q.pop();

            if (seen.count(st)) continue;
            seen.insert(st);
            //std::cout << "  " << score << '\n';

            if (st == GOAL) {
                (p == 1 ? ans1 : ans2) = score;
                break;
            }

            for (size_t i = 0; i < st.size(); i++) {
                if(i == 2 || i == 4 || i == 6 || i == 8) continue;
                auto c = st[i];
                if (c != '.') {
                    for (size_t j = 0; j < st.size(); j++) {
                        if(i == j || j == 2 || j == 4 || j == 6 || j == 8) continue;
                        if (auto steps = canmove(st, c, i, j); steps > 0) {
                            auto newscore = steps;
                            if (c > 'A') newscore *= 10;
                            if (c > 'B') newscore *= 10;
                            if (c > 'C') newscore *= 10;
                            //std::cout << i << " -> " << j << ' ' << steps << '\n';
                            std::swap(st[i], st[j]);
                            //printstate(st);
                            if(!seen.count(st)) q.emplace(score + newscore, st);
                            std::swap(st[i], st[j]);
                        }
                    }
                }
            }

        }
    }


    return {std::to_string(ans1), std::to_string(ans2)};
}
