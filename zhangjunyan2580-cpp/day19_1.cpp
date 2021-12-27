#include <algorithm>
#include <stdio.h>
#include <vector>
#include <tuple>
#include <map>
#include <set>

int dist(std::tuple<int, int, int> a, std::tuple<int, int, int> b) {
    auto& [x1, y1, z1] = a; auto& [x2, y2, z2] = b;
    return std::abs(x1 - x2) + std::abs(y1 - y2) + std::abs(z1 - z2);
}

int dist2(std::tuple<int, int, int> a, std::tuple<int, int, int> b) {
    auto& [x1, y1, z1] = a; auto& [x2, y2, z2] = b;
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) + (z1 - z2) * (z1 - z2);
}

struct Scanner {
    std::vector< std::tuple<int, int, int> > S;
    std::map< std::tuple<int, int>, std::pair< std::tuple<int, int, int>, std::tuple<int, int, int> > > hash() const {
        std::map< std::tuple<int, int>, std::pair< std::tuple<int, int, int>, std::tuple<int, int, int> > > ans;
        for (auto i = S.begin(); i != S.end(); ++i)
            for (auto j = i + 1; j != S.end(); ++j)
                ans[std::make_tuple(dist(*i, *j), dist2(*i, *j))] = std::make_pair(*i, *j);
        return ans;
    }
};
std::vector<Scanner> sc;
std::vector< std::tuple<int, int, int> > sp;
Scanner bd;

std::map< std::tuple<int, int, int>, std::tuple<int, int, int> > match(const Scanner& s1, const Scanner& s2) {
    auto S1 = s1.hash(), S2 = s2.hash();
    std::set< std::tuple<int, int> > S;
    for (auto i = S1.begin(), j = S2.begin(); i != S1.end() && j != S2.end(); ) {
        if (i->first == j->first) {
            S.insert(i->first);
            ++i; ++j;
        } else if (i->first < j->first) ++i;
        else ++j;
    }
    std::map< std::tuple<int, int, int>, std::map<std::tuple<int, int, int>, int> > M;
    for (const auto &i : S) {
        const auto &[b1, b2] = S1[i];
        const auto &[b3, b4] = S2[i];
        if (!M.count(b1)) M[b1] = std::map<std::tuple<int, int, int>, int>();
        if (!M.count(b2)) M[b2] = std::map<std::tuple<int, int, int>, int>();
        M[b1][b3] += 1; M[b1][b4] += 1;
        M[b2][b3] += 1; M[b2][b4] += 1;
    }
    std::map< std::tuple<int, int, int>, std::tuple<int, int, int> > A;
    for (const auto &[k, v] : M) {
        int u = 0; std::tuple<int, int, int> P;
        for (const auto &[K, V] : v) if (V > u) u = V, P = K;
        A[k] = P;
    }
    return A;
}

char str[105];

const std::vector< std::tuple<int, int, int, int, int, int, int, int, int> > RT = {
    {-1, 0, 0, 0, -1, 0, 0, 0, 1},
    {-1, 0, 0, 0, 0, -1, 0, -1, 0},
    {-1, 0, 0, 0, 0, 1, 0, 1, 0},
    {-1, 0, 0, 0, 1, 0, 0, 0, -1},
    {0, -1, 0, -1, 0, 0, 0, 0, -1},
    {0, -1, 0, 0, 0, -1, 1, 0, 0},
    {0, -1, 0, 0, 0, 1, -1, 0, 0},
    {0, -1, 0, 1, 0, 0, 0, 0, 1},
    {0, 0, -1, -1, 0, 0, 0, 1, 0},
    {0, 0, -1, 0, -1, 0, -1, 0, 0},
    {0, 0, -1, 0, 1, 0, 1, 0, 0},
    {0, 0, -1, 1, 0, 0, 0, -1, 0},
    {0, 0, 1, -1, 0, 0, 0, -1, 0},
    {0, 0, 1, 0, -1, 0, 1, 0, 0},
    {0, 0, 1, 0, 1, 0, -1, 0, 0},
    {0, 0, 1, 1, 0, 0, 0, 1, 0},
    {0, 1, 0, -1, 0, 0, 0, 0, 1},
    {0, 1, 0, 0, 0, -1, -1, 0, 0},
    {0, 1, 0, 0, 0, 1, 1, 0, 0},
    {0, 1, 0, 1, 0, 0, 0, 0, -1},
    {1, 0, 0, 0, -1, 0, 0, 0, -1},
    {1, 0, 0, 0, 0, -1, 0, 1, 0},
    {1, 0, 0, 0, 0, 1, 0, -1, 0},
    {1, 0, 0, 0, 1, 0, 0, 0, 1},
};

std::vector< std::tuple<int, int, int> > rotate(const std::vector< std::tuple<int, int, int> > &U,
    const std::tuple<int, int, int, int, int, int, int, int, int> &R)
{
    std::vector< std::tuple<int, int, int> > A;
    const auto &[_11, _12, _13, _21, _22, _23, _31, _32, _33] = R;
    for (const auto &[x, y, z] : U) {
        int new_x = _11 * x + _12 * y + _13 * z,
            new_y = _21 * x + _22 * y + _23 * z,
            new_z = _31 * x + _32 * y + _33 * z;
        A.push_back(std::make_tuple(new_x, new_y, new_z));
    }
    return A;
}

int main() {
    bool first = true;
    while (fgets(str, 100, stdin)) {
        if (*str == '-' && *(str + 1) == '-') {
            if (!first) sc.push_back(bd);
            bd = Scanner();
            first = false;
            continue;
        }
        int x, y, z;
        sscanf(str, "%d,%d,%d", &x, &y, &z);
        bd.S.push_back(std::make_tuple(x, y, z));
    }
    sc.push_back(bd);
    bd = sc.front();
    sc.erase(sc.begin());
    while (!sc.empty()) {
        for (unsigned i = 0; i < sc.size(); ++i) {
            auto &S = sc[i];
            auto M = match(bd, S);
            if (M.size() < 12u) continue;
            std::vector< std::tuple<int, int, int> > V;
            for (const auto &[k, v] : M) V.push_back(v);
            for (const auto &R : RT) {
                std::vector< std::tuple<int, int, int> > r = rotate(V, R);
                std::set<int> dists;
                auto i = r.begin(); auto j = M.begin();
                for (; i != r.end(); ++i, ++j)
                    dists.insert(dist2(*i, j->first));
                if (dists.size() > 1u) continue;
                const auto &[x1, y1, z1] = M.begin()->first;
                const auto &[x2, y2, z2] = r[0];
                std::tuple<int, int, int> pos = std::make_tuple(x1 - x2, y1 - y2, z1 - z2);
                sp.push_back(pos);
                printf("%d %d %d\n", std::get<0>(pos), std::get<1>(pos), std::get<2>(pos));
                for (const auto &[x, y, z] : rotate(S.S, R))
                    bd.S.push_back(std::make_tuple(x + x1 - x2, y + y1 - y2, z + z1 - z2));
                std::sort(bd.S.begin(), bd.S.end());
                bd.S.resize(std::unique(bd.S.begin(), bd.S.end()) - bd.S.begin());
                break;
            }
            sc.erase(sc.begin() + i);
            break;
        }
    }
    printf("%d\n", bd.S.size());
    return 0;
}