#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>


std::tuple<std::string, std::string> p08(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<std::vector<std::string>> v1;
    std::vector<std::vector<std::string>> v2;

    {
        bool pipe = false;
        std::string tmp;
        bool first = true;
        for(const auto c : input) {
            if(c >= 'a' && c <= 'z') {
                tmp.push_back(c);
            } else {
                if(!tmp.empty()) {
                    if(first) {
                        v1.emplace_back();
                        v2.emplace_back();
                        first = false;
                    }
                    if(pipe) v2.back().push_back(tmp);
                    else v1.back().push_back(tmp);
                }
                tmp.clear();
                if(c == '|') pipe = true;
                else if(c == '\n') {
                    pipe = false;
                    first = true;
                }

            }

        }
    }
/*
    for(int i = 0; i < v1.size(); i++) {
        for (auto && s : v1[i]) std::cout << ' ' << s;
        std::cout << '|';
        for (auto && s : v2[i]) std::cout << ' ' << s;
        std::cout << std::endl;
    }
    std::cout << v1.size() << ' ' << v2.size() << std::endl;
*/
    for(auto && v : v2) for(auto && s : v) {
        switch(s.size()) {
            case 2:
            case 3:
            case 4:
            case 7:
                ans1++;
                break;
            default:
                break;
        }
    }

    auto pattern = [](const std::string & s) {
        uint16_t ret = 0;
        for(auto c : s) {
            ret |= (1 << (c-'a'));
        }
        return ret;
    };

    for(size_t i = 0; i < v1.size(); i++) {
        std::map<std::string, int> m;
        std::vector<std::string> v(10);
        std::vector<std::string> fives, sixes;
        for(auto && s : v1[i]) {
            std::sort(s.begin(), s.end());
            if(s.size() == 2) { m[s] = 1; v[1] = s; }
            else if(s.size() == 3) { m[s] = 7; v[7] = s; }
            else if(s.size() == 4) { m[s] = 4; v[4] = s; }
            else if(s.size() == 7) { m[s] = 8; v[8] = s; }
            else if(s.size() == 5) fives.push_back(s);
            else if(s.size() == 6) sixes.push_back(s);
            else std::cout << "ERROR" << std::endl;
        }

        auto one_p = pattern(v[1]);

        // figure out 3
        auto c11 = v[1][0];
        auto c12 = v[1][1];
        for(auto it = fives.begin(); it != fives.end(); it++) {
            if(it->find(c11) != std::string::npos && it->find(c12) != std::string::npos) {
                m[*it] = 3;
                v[3] = *it;
                fives.erase(it);
                break;
            }
        }
        auto three_p = pattern(v[3]);

        // figure out 6
        for(auto it = sixes.begin(); it != sixes.end(); it++) {
            if((pattern(*it) & one_p) != one_p) {
                m[*it] = 6;
                v[6] = *it;
                sixes.erase(it);
                break;
            }
        }
        auto six_p = pattern(v[6]);

        // figure out 9
        for(auto it = sixes.begin(); it != sixes.end(); it++) {
            if((pattern(*it) & three_p) == three_p) {
                m[*it] = 9;
                v[9] = *it;
                sixes.erase(it);
                break;
            }
        }
        // 0 is left
        m[sixes.front()] = 0;
        v[0] = sixes.front();

        // figure out 5
        for(auto it = fives.begin(); it != fives.end(); it++) {
            auto cp = pattern(*it);
            if((cp & six_p) == cp) {
                m[*it] = 5;
                v[5] = *it;
                fives.erase(it);
                break;
            }
        }

        // 2 is left
        m[fives.front()] = 2;
        v[2] = fives.front();

        int tmp = 0;
        for(auto && s : v2[i])
        {
            std::sort(s.begin(), s.end());
            tmp *= 10;
            tmp += m[s];
        }
        ans2 += tmp;
    }

    return {std::to_string(ans1), std::to_string(ans2)};
}
