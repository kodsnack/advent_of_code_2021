#include <stdio.h>
#include <string.h>
#include <algorithm>

#define MIN -131072
#define MAX 131071

char op[15];
int x1, x2, y1, y2, z1, z2;

struct Operation {
    int op, x1, x2, y1, y2, z1, z2;
} Q[1005];
int opc;

long long dq(int p, int xl, int yl, int zl, int xr, int yr, int zr) {
    if (xl > xr || yl > yr || zl > zr || !p) return 0;
    if (Q[p].x1 > xr || Q[p].x2 < xl || Q[p].y1 > yr || Q[p].y2 < yl || Q[p].z1 > zr || Q[p].z2 < zl)
        return dq(p - 1, xl, yl, zl, xr, yr, zr);
    long long sum = 0;
    int x0 = std::max(Q[p].x1, xl), y0 = std::max(Q[p].y1, yl), z0 = std::max(Q[p].z1, zl),
        x1 = std::min(Q[p].x2, xr), y1 = std::min(Q[p].y2, yr), z1 = std::min(Q[p].z2, zr);
    sum += dq(p - 1, xl, yl, zl, std::min(x0 - 1, xr), yr, zr);
    sum += dq(p - 1, std::max(x1 + 1, xl), yl, zl, xr, yr, zr);
    sum += dq(p - 1, x0, yl, zl, x1, std::min(y0 - 1, yr), zr);
    sum += dq(p - 1, x0, std::max(y1 + 1, yl), zl, x1, yr, zr);
    sum += dq(p - 1, x0, y0, zl, x1, y1, std::min(z0 - 1, zr));
    sum += dq(p - 1, x0, y0, std::max(z1 + 1, zl), x1, y1, zr);
    if (Q[p].op)
        sum += (long long) (x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1);
    return sum;
}

int main() {
    while (~scanf("%s x=%d..%d,y=%d..%d,z=%d..%d", op, &x1, &x2, &y1, &y2, &z1, &z2))
        Q[++opc] = (Operation) { *(op + 1) == 'n', x1, x2, y1, y2, z1, z2 };
    printf("%lld\n", dq(opc, MIN, MIN, MIN, MAX, MAX, MAX));
    return 0;
}