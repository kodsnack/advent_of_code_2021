#include "aoc.h"
#include <vector>
#include <algorithm>
#include <iostream>
#include <stack>
#include <queue>
#include <string.h>

struct node {
    int a = -1, b = -1;
    bool havea = false;
    int *pa = nullptr, *pb = nullptr;
    int *na = nullptr, *nb = nullptr;
    node *parent = nullptr;
    node *suba = nullptr;
    node *subb = nullptr;
};

void rec(node * n) {
    std::cout << '[';
    if(n->suba) rec(n->suba); else std::cout << n->a;
    std::cout << ',';
    if(n->subb) rec(n->subb); else std::cout << n->b;
    std::cout << ']';
};

void constructl(node *n, bool first = true) {
    static int * ln = nullptr;
    if(first) ln = nullptr;
    if(n->suba) constructl(n->suba, false); else { n->pa = ln; ln = &n->a;}
    if(n->subb) constructl(n->subb, false); else { n->pb = ln; ln = &n->b;}
}

void constructr(node *n, bool first = true) {
    static int * ln = nullptr;
    if(first) ln = nullptr;
    if(n->subb) constructr(n->subb, false); else { n->nb = ln; ln = &n->b; }
    if(n->suba) constructr(n->suba, false); else { n->na = ln; ln = &n->a; }
}

bool split(node *n) {
    bool ret = false;
    if(n->suba) ret = split(n->suba); else {
        if(n->a >= 10) {
            n->suba = new node;
            //memset(n->suba,0,sizeof(node));
            n->suba->a = n->a / 2;
            n->suba->b = (n->a+1) / 2;
            n->a = 0;
            return true;
        }
    }
    if(!ret) {
        if (n->subb) ret = split(n->subb);
        else {
            if (n->b >= 10) {

                n->subb = new node;
                //memset(n->subb, 0, sizeof(node));
                n->subb->a = n->b / 2;
                n->subb->b = (n->b + 1) / 2;
                n->b = 0;
                return true;
            }
        }
    }
    return ret;
}
int64_t getmagn(node*n) {
    int64_t a = n->suba ? getmagn(n->suba) : n->a;
    int64_t b = n->subb ? getmagn(n->subb) : n->b;
    return 3*a + 2*b;
}
node * copy(node * n) {
    node * ret = new node;
    memcpy(ret, n, sizeof(node));
    if(n->suba) ret->suba = copy(n->suba);
    if(n->subb) ret->subb = copy(n->subb);
    return ret;
}

bool explode(node *n, int level = 0) {
    level++;
    if(level >= 4) {
        if(n->suba) {

            auto sub = n->suba;
            if(sub->suba || sub->subb) return explode(sub, level);
            else {
                n->suba = nullptr;
                //std::cout << "explode A " << sub->a << ',' << sub->b << std::endl;
                n->a = 0;
                if (sub->pa) { /*std::cout << "Add " << sub->a << " to " << *(sub->pa) << std::endl;*/ *(sub->pa) += sub->a; } //else std::cout << "No left" << std::endl;
                if (sub->nb) { /*std::cout << "Add " << sub->b << " to " << *(sub->nb) << std::endl;*/ *(sub->nb) += sub->b; } //else std::cout << "No right" << std::endl;
                delete sub;
                return true;
            }
        }
        if(n->subb) {
            auto sub = n->subb;
            if(sub->suba || sub->subb) return explode(sub, level);
            else {
                n->subb = nullptr;
                //std::cout << "explode B " << sub->a << ',' << sub->b << std::endl;
                n->b = 0;
                if (sub->pa) { *(sub->pa) += sub->a; }
                if (sub->nb) { *(sub->nb) += sub->b; }
                delete sub;
                return true;
            }
        }
    } else {
        if(n->suba) if(explode(n->suba, level)) return true;
        if(n->subb) if(explode(n->subb, level)) return true;
    }
    return false;
}

std::tuple<std::string, std::string> p18(const std::string & input) {
    int64_t ans1 = 0;
    int64_t ans2 = 0;
    std::vector<node*> v;

    {
        int num = 0;
        bool havenum = false;
        std::stack<node*> st;
        for(const auto c : input) {
            if(c >= '0' && c <= '9') {
                num *= 10;
                num += c-'0';
                havenum = true;
            } else {
                if(havenum) {
                    if(st.top()->havea) {
                        st.top()->b = num;
                    } else {
                        st.top()->a = num;
                        st.top()->havea = true;
                    }
                }
                havenum = false;
                num = 0;

                if(c == '[') {
                    auto curr = new node;
                    //memset(curr,0,sizeof(node));

                    if(!st.empty()) {
                        curr->parent = st.top();
                        if(st.top()->havea) {
                            st.top()->subb = curr;
                        } else {
                            st.top()->suba = curr;
                            st.top()->havea = true;
                        }
                    }
                    st.push(curr);
                } else if(c==']') {
                    auto curr = st.top();
                    st.pop();
                    if(st.empty()) v.push_back(curr);
                }
            }

        }
    }

    std::deque<node*> q;

    for(auto e : v) {
        q.push_back(copy(e));
    }

    for(size_t i = 0; i < v.size(); i++) {
        for(size_t j = 0; j < v.size(); j++) {
            if(i == j) continue;
            auto n = new node;
            n->suba = copy(v[i]);
            n->subb = copy(v[j]);
            bool red = true, sp = true;
            do {
                constructl(n);
                constructr(n);

                red = explode(n);
                if (red) continue;
                sp = split(n);
            } while ((red || sp));

            auto tmp = getmagn(n);
            if (tmp > ans2) ans2 = tmp;
        }
    }

    while(q.size() > 1) {
        auto n1 = q.front(); q.pop_front();
        auto n2 = q.front(); q.pop_front();
        auto n = new node;
        //memset(n,0,sizeof(node));
        n->havea = true;
        n->suba = n1;
        n->subb = n2;

        bool red = true, sp = true;

        do {
            constructl(n);
            constructr(n);

            red = explode(n);
            if(red) continue;
            sp = split(n);
        } while((red || sp));

        q.push_front(n);
    }

    ans1 = getmagn(q.front());

    return {std::to_string(ans1), std::to_string(ans2)};
}
