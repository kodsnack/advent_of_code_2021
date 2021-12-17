#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
std::tuple<std::string, std::string> p17(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<int> v;

    {
        int num = 0;
        bool havenum = false;
        bool neg = false;
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                num *= 10;
                num += c - '0';
                havenum = true;
            } else if(c == '-') {
                neg = true;
            } else {
                if(havenum) {
                    v.push_back(neg ? -num : num);
                }
                neg = false;
                havenum = false;
                num = 0;
            }

        }
    }


    if(v.size() < 4) return {};

    int targetx1 = v[0];
    int targetx2 = v[1];
    int targety1 = v[2];
    int targety2 = v[3];

    for(int iyv = std::min(targety1,targety2); iyv < -2*std::min(targety1,targety2); iyv++) {
        for(int ixv = 0; ixv <= std::max(targetx1,targetx2); ixv++) {
            int yv = iyv;
            int xv = ixv;
            int y = 0, x = 0;
            int maxy = 0;
            bool hit = false;
            while(true) {
                x += xv;
                y += yv;
                if(xv > 0) xv--;
                else if(xv < 0) xv++;
                yv--;
                maxy = std::max(maxy, y);
                if(x>=targetx1 && x<=targetx2 && y >= targety1 && y <= targety2) {
                    hit = true;
                    break;
                }
                if(y < std::min(targety1, targety1)) break;
                if(x > std::max(targetx1, targetx2)) break;
            }
            if(hit) {
                if(maxy > ans1) ans1 = maxy;
                ans2++;
            }

        }
    }

  return {std::to_string(ans1), std::to_string(ans2)};
}
