#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
std::tuple<std::string, std::string> p04(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<int> v;
    std::vector<std::vector<int>> boards;

    {
        int num = 0;
        bool first = true;
        int cnt = 0;
        bool havenum = false;
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                num *= 10;
                num += c-'0';
                havenum = true;
            } else {
                if(havenum) {
                    if(first) {
                        v.push_back(num);
                    } else {
                        if(cnt == 0) {
                            boards.emplace_back();
                        }
                        boards.back().push_back(num);
                        cnt++;
                        if(cnt == 25) cnt = 0;
                    }
                }
                if(c == '\n') first = false;
                havenum = false;
                num = 0;
            }

        }
    }

    auto bc = boards;

    for(auto curr : v) {
        for(auto && board : boards) {
            for(auto & x : board) {
                if(x == curr) x = -1;
            }
        }

        for(auto && board : boards) {
            bool match = false;
            for(int row = 0; row < 5; row++) {
                match = true;
                for(int col = 0; col < 5; col++) {
                    if(board[row*5+col] != -1) match = false;
                }
                if(match) break;
            }
            if(!match) {
                for(int col = 0; col < 5; col++) {
                    match = true;
                    for(int row = 0; row < 5; row++) {
                        if(board[row*5+col] != -1) match = false;
                    }
                    if(match) break;
                }
            }

            if(match) {
                for(auto i : board) {
                    if(i != -1) ans1 += i;
                }
                ans1 *= curr;
                break;
            }

        }

        if(ans1) break;
    }

    boards = bc;

    for(auto curr : v) {
        for(auto && board : boards) {
            for(auto & x : board) {
                if(x == curr) x = -1;
            }
        }

        for(auto && board : boards) {
            bool match = false;
            for(int row = 0; row < 5; row++) {
                match = true;
                for(int col = 0; col < 5; col++) {
                    if(board[row*5+col] != -1) {
                        match = false;
                        break;
                    }
                }
                if(match) break;
            }
            if(!match) {
                for(int col = 0; col < 5; col++) {
                    match = true;
                    for(int row = 0; row < 5; row++) {
                        if(board[row*5+col] != -1) {
                            match = false;
                            break;
                        }
                    }
                    if(match) break;
                }
            }

            if(match) {
                ans2 = board[0]; // save
                board[0] = -2; // mark for deletion
            }
        }

        if(boards.size() == 1 && boards[0][0] == -2) {
            if(ans2 < 0) ans2 = 0;
            for(auto i : boards[0]) {
                if(i > 0) ans2 += i;
            }
            ans2 *= curr;
            break;

        }

        boards.erase(std::remove_if(boards.begin(), boards.end(), [](auto && b) { return b[0] == -2;}), boards.end());

    }


    return {std::to_string(ans1), std::to_string(ans2)};
}
