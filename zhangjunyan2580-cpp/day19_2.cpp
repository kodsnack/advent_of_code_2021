#include <stdio.h>
#include <vector>
#include <tuple>

int dist(std::tuple<int, int, int> a, std::tuple<int, int, int> b) {
    auto& [x1, y1, z1] = a; auto& [x2, y2, z2] = b;
    return std::abs(x1 - x2) + std::abs(y1 - y2) + std::abs(z1 - z2);
}

std::vector< std::tuple<int, int, int> > P;

int main() {
    int ans = 0, x, y, z;
    while (~scanf("%d%d%d", &x, &y, &z)) P.push_back(std::make_tuple(x, y, z));
    for (auto i = P.begin(); i != P.end(); ++i)
        for (auto j = i + 1; j != P.end(); ++j)
            if (dist(*i, *j) > ans) ans = dist(*i, *j);
    printf("%d\n", ans);
    return 0;
}