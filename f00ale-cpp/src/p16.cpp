#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>
#include <numeric>
uint64_t parsepack(std::deque<char> & q, int64_t & vers, std::string pref = "") {
    auto pop = [](auto && q, int n) {
        uint32_t ret = 0;
        for(int i = 0; i < n; i++) {
            ret <<= 1;
            if(q.front() == '1') ret |= 1;
            q.pop_front();
        }
        return ret;
    };
    auto ver = pop(q, 3);
    auto typ = pop(q, 3);
    vers += ver;
    //std::cout << pref << "ver " << ver << " type " << typ << std::endl;
    if(typ == 4) {
        bool done = false;
        uint64_t num = 0;
        while(!done) {
            auto tmp = pop(q, 5);
            num <<= 4;
            num += tmp & 0xf;
            done = ! (tmp & 0x10);
        }
        //std::cout << pref << "num = " << num << std::endl;
        return num;
    } else {
        auto lentype = pop(q,1);
        //std::cout << pref  << "lentype " << lentype << std::endl;
        std::vector<uint64_t> rets;
        if(!lentype) {
            auto len = pop(q,15);
            //std::cout << pref  << "sublen " << len << std::endl;
            auto oldsize = q.size();
            while(oldsize-q.size() < len) {
                rets.push_back(parsepack(q, vers, pref+"  "));
            }
        } else {
            auto numpacks = pop(q,11);
            //std::cout << pref  << numpacks << " subpackets" << std::endl;
            for(uint32_t i = 0; i < numpacks; i++) {
                rets.push_back(parsepack(q, vers, pref+"  "));
            }
        }
        switch (typ) {
            case 0: return std::accumulate(rets.begin(), rets.end(), 0llu);
            case 1: return std::accumulate(rets.begin(), rets.end(), 1llu, [](auto && i1, auto && i2){return i1*i2;});
            case 2: return *std::min_element(rets.begin(), rets.end());
            case 3: return *std::max_element(rets.begin(), rets.end());
            case 5: return rets[0] > rets[1] ? 1 : 0;
            case 6: return rets[0] < rets[1] ? 1 : 0;
            case 7: return rets[0] == rets[1] ? 1 : 0;
            default:
                std::cout << "unhandeld type " << typ << std::endl;
        }
    }
    return 0;
};


std::tuple<std::string, std::string> p16(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<int> v;

    {
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                v.push_back(c-'0');
            } else if(c >= 'A' && c <= 'F') {
                v.push_back(10+c-'A');
            }
        }
    }

    std::deque<char> q;
    for(auto i : v) {
        q.push_back(i & 0x8 ? '1' : '0');
        q.push_back(i & 0x4 ? '1' : '0');
        q.push_back(i & 0x2 ? '1' : '0');
        q.push_back(i & 0x1 ? '1' : '0');
    }

    ans2 = parsepack(q, ans1);

    return {std::to_string(ans1), std::to_string(ans2)};
}
