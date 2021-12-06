#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
std::tuple<std::string, std::string> p03(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<uint32_t> v;
    int cnt0s[20] = {0, };
    int cnt1s[20] = {0, };
    int maxpos = 0;
    {
        uint32_t num = 0;
        int pos = 0;
        for(const auto c : input) {
            if(c == '0') {
                cnt0s[pos]++;
                num <<= 1;
                pos++;
            } else if(c == '1') {
                cnt1s[pos]++;
                num <<= 1;
                num |= 1;
                pos++;
            } else {
                if(pos) {
                    v.push_back(num);
                }
                maxpos = std::max(maxpos, pos);
                pos = 0;
                num = 0;
            }

        }
    }

    uint32_t gamma = 0, epsilon = 0;
    for(int i = 0; i < maxpos; i++) {
        gamma <<= 1;
        epsilon <<= 1;
        if(cnt0s[i] > cnt1s[i]) {
            epsilon |= 1;
        } else {
            gamma |= 1;
        }
    }

    ans1 = gamma*epsilon;

    uint32_t oxygen = 0, co2 = 0;
    auto vv = v;
    auto mp = maxpos;

     while(mp) {
        decltype(v) vc;
        vc.swap(v);

        int c0 = 0, c1 = 0;
        mp--;
        uint32_t mask = 1<<mp;
        for(auto i : vc) {
            if(i & mask) c1++;
            else c0++;
        }
        for(auto i : vc) {
            if((c1 >= c0) && (i & mask)) v.push_back(i);
            else if((c0 > c1) && !(i & mask)) v.push_back(i);
        }
         if(v.size() == 1) {
             oxygen = v[0];
             break;
         }

    }

    mp = maxpos;
    v = vv;

    while(mp) {
        decltype(v) vc;
        vc.swap(v);
        int c0 = 0, c1 = 0;
        mp--;
        uint32_t mask = 1<<mp;
        for(auto i : vc) {
            if(i & mask) c1++;
            else c0++;
        }

        for(auto i : vc) {
            if((c0 <= c1) && !(i & mask)) v.push_back(i);
            else if((c1 < c0) && (i & mask)) v.push_back(i);
        }
        if(v.size() == 1) {
            co2 = v[0];
            break;
        }
    }

    ans2 = oxygen * co2;

    return {std::to_string(ans1), std::to_string(ans2)};
}
