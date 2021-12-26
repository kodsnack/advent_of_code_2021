#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
std::tuple<std::string, std::string> p25(const std::string & input) {
    int64_t ans1 = 0;
    std::string ans2("-");
    std::vector<std::string> v;

    {
        bool first = true;
        for(const auto c : input) {
            if(c == '.' || c == 'v' || c == '>') {
                if(first) v.emplace_back();
                v.back().push_back(c);
                first = false;
            } else {
                first = true;
            }
        }
    }

    const auto rs = v.size();
    const auto cs = v[0].size();
    
    while(true) {
        int moves = 0;
        {
            for (size_t r = 0; r < rs; r++) {
                for (size_t c = 0; c < cs; c++) {
                    if (v[r][c] == '>') {
                        if (v[r][(c + 1) % cs] == '.') {
                            v[r][c] = 'm';
                            moves++;
                            c++;
                        }
                    }
                }
                for (size_t c = 0; c < cs; c++) {
                    if(v[r][c] == 'm') {
                        v[r][c] = '.';
                        v[r][(c+1)%cs] = '>';
                        c++;
                    }
                }
            }
        }

        {
            for (size_t c = 0; c < cs; c++) {
                for (size_t r = 0; r < rs; r++) {
                    if (v[r][c] == 'v') {
                        if (v[(r + 1) % rs][c] == '.') {
                            v[r][c] = 'm';
                            moves++;
                            r++;
                        }
                    }
                }
                for (size_t r = 0; r < rs; r++) {
                    if (v[r][c] == 'm') {
                        v[(r + 1) % rs][c] = 'v';
                        v[r][c] = '.';
                        r++;

                    }
                }
            }

        }

        ans1++;
        if(moves == 0) break;
    }

    return {std::to_string(ans1), ans2};
}
