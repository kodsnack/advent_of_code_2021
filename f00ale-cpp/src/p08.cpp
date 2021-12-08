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

    std::vector<std::array<uint8_t, 14>> vb;
    vb.reserve(500);

    {
        uint8_t pt = 0;
        int cnt = 0;
        for(const auto c : input) {
            if(c >= 'a' && c <= 'z') {
                pt |= (1<<(c-'a'));
            } else {
                if(pt) {
                    if(!cnt) vb.emplace_back();
                    vb.back()[cnt++] = pt;
                    if(cnt == 14) cnt = 0;
                    pt = 0;
                }
            }

        }
    }

    constexpr auto popcnt = [](uint8_t c) {
        //return __builtin_popcount(c);
        int ret = 0;
        while(c) {
            if(c & 1) ret++;
            c >>= 1;
        }
        return ret;
    };

    std::array<int, 256> tab{};
    std::array<uint8_t, 10> fwd{};
    std::array<uint8_t,3> fives{}, sixes{};

    for(auto && a : vb) {
        int fc = 0, sc = 0;

        for(size_t i = 0; i < 10; i++) {
            switch(popcnt(a[i])) {
                case 2: fwd[1] = a[i]; tab[a[i]] = 1; break;
                case 3: fwd[7] = a[i]; tab[a[i]] = 7; break;
                case 4: fwd[4] = a[i]; tab[a[i]] = 4; break;
                case 5: fives[fc++] = a[i]; break;
                case 6: sixes[sc++] = a[i]; break;
                case 7: fwd[8] = a[i]; tab[a[i]] = 8; break;
                default:
                    break;
            }
        }

        // figure out 3
        for(int i = 0; i < fc; i++) {
            if((fives[i] & fwd[1]) == fwd[1]) {
                fwd[3] = fives[i];
                tab[fives[i]] = 3;
                fc--;
                std::swap(fives[i], fives[fc]);
                break;
            }
        }

        // figure out 6
        for(int i = 0; i < sc; i++) {
            if ((sixes[i] & fwd[1]) != fwd[1]) {
                fwd[6] = sixes[i];
                tab[sixes[i]] = 6;
                sc--;
                std::swap(sixes[i], sixes[sc]);
                break;
            }
        }

        // figure out 9
        for(int i = 0; i < sc; i++) {
            if((sixes[i] & fwd[3]) == fwd[3]) {
                fwd[9] = sixes[i];
                tab[sixes[i]] = 9;
                sc--;
                std::swap(sixes[i], sixes[sc]);
                break;
            }
        }

        // 0 left
        fwd[0] = sixes[0];
        tab[sixes[0]] = 0;

        // figure out 5
        for(int i = 0; i < fc; i++) {
            if((fives[i] & fwd[9]) == fives[i]) {
                fwd[5] = fives[i];
                tab[fives[i]] = 5;
                fc--;
                std::swap(fives[i], fives[fc]);
                break;
            }
        }

        // 2 left
        fwd[2] = fives[0];
        tab[fives[0]] = 2;

        int tmp = 0;
        for(size_t i = 10; i < 14; i++) {
            switch(popcnt(a[i])) {
                case 2:
                case 3:
                case 4:
                case 7:
                    ans1++;
                    break;
                default:
                    break;
            }
            tmp *= 10;
            tmp += tab[a[i]];
        }

        ans2 += tmp;
    }

    return {std::to_string(ans1), std::to_string(ans2)};
}
