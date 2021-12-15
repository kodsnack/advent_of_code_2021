#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <stack>
std::tuple<std::string, std::string> p10(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;

    std::vector<std::string> v;
    v.reserve(200);
    {
        bool first = true;
        for(const auto c : input) {
            if(c == '(' || c == ')' || c == '[' || c == ']' || c == '{' || c == '}' || c == '<' || c == '>') {
                if(first) v.emplace_back();
                first = false;
                v.back().push_back(c);
            } else if(c=='\n'){
                first = true;
            }

        }
    }

    std::vector<int64_t> scores;
    scores.reserve(200);
    for(auto && s : v) {
        std::stack<char> st;
        bool corrupt = false;
        for(auto c : s) {
            if(c == '(' || c == '{' || c == '[' || c == '<') st.push(c);
            else {
                if(st.empty()) break;
                if(c == ')' && st.top() != '(') {
                    ans1 += 3;
                    corrupt = true;
                    break;
                }
                if(c == ']' && st.top() != '[') {
                    ans1 += 57;
                    corrupt = true;
                    break;
                }
                if(c == '}' && st.top() != '{') {
                    ans1 += 1197;
                    corrupt = true;
                    break;
                }
                if(c == '>' && st.top() != '<') {
                    ans1 += 25137;
                    corrupt = true;
                    break;
                }
                st.pop();
            }
        }
        if(!corrupt) {
            int64_t score = 0;
            while(!st.empty()) {
                auto c = st.top();
                st.pop();
                score*=5;
                switch(c) {
                    case '(': score+=1; break;
                    case '[': score+=2; break;
                    case '{': score+=3; break;
                    case '<': score+=4; break;
                    default: break;
                }
            }
            scores.push_back(score);
        }
    }

    std::sort(scores.begin(), scores.end());
    ans2 = scores[scores.size()/2];

    return {std::to_string(ans1), std::to_string(ans2)};
}
