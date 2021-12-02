#include "aoc.h"
#include <vector>
#include <algorithm>
#include <string>

std::tuple<std::string, std::string> p02(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<int> v;

    int x = 0, y = 0;
    int64_t x2 = 0, y2 = 0, a = 0;
    {
        std::string dir;
        int num = 0;
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                num *= 10;
                num += c - '0';
            } else if(c >= 'a' && c <= 'z') {
                dir += c;
            } else {
                if( !dir.empty() && num) {
                    if(dir == "forward") { x += num; x2 += num; y2 += a*num; }
                    else if(dir == "up") { y -= num; a -= num; }
                    else if(dir == "down") { y += num; a+= num; }
                    else { }
                    dir.clear();
                    num = 0;
                }
            }

        }
    }
    ans1 = x*y;
    ans2 = x2*y2;
    return {std::to_string(ans1), std::to_string(ans2)};
}
