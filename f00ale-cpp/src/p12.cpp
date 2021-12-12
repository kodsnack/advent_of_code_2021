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
    std::vector<std::tuple<std::string,std::string>> v;

    {
        bool havedash = false;
        std::string tmp1,tmp2;
        for(const auto c : input) {
            if((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
                if(havedash) tmp2.push_back(c);
                else tmp1.push_back(c);
            } else if(c == '-') {
                havedash = true;
            } else {
                if(!tmp1.empty()) {
                    v.emplace_back(tmp1, tmp2);
                    tmp1.clear();
                    tmp2.clear();
                    havedash = false;
                }
            }
        }
    }

    std::map<std::string, std::vector<std::string>> conns;
    for(auto & [a,b] : v) {
        conns[a].push_back(b);
        conns[b].push_back(a);
    }

    struct state {
        std::string current;
        std::map<std::string, int> visited;
        std::string multi;
    };

    std::queue<state> q;
    q.push({"start", {}, ""});
    while(!q.empty()) {
        auto s = q.front();
        q.pop();

        if(s.current == "end") {
            ans1++;
            continue;
        }

        if((s.current[0] >= 'a' && s.current[0] <= 'z') && s.visited[s.current]) continue;

        s.visited[s.current]++;
        for(auto & b : conns[s.current]) {
            q.push({b, s.visited, s.multi});
        }

    }

    for(auto & n : conns["start"]) q.push({n, {}, ""});
    while(!q.empty()) {
        auto s = q.front();
        q.pop();

        if(s.current == "start") continue;
        if(s.current == "end") {
            ans2++;
            continue;
        }

        if(!((s.current[0] >= 'a' && s.current[0] <= 'z') && s.visited[s.current])) {
            s.visited[s.current]++;
            for (auto &b: conns[s.current]) {
                q.push({b, s.visited, s.multi});
            }
        } else if(s.multi.empty()) {
            s.multi = s.current;
            for (auto &b: conns[s.current]) {
                q.push({b, s.visited, s.multi});
            }
        }
    }

    return {std::to_string(ans1), std::to_string(ans2)};
}
