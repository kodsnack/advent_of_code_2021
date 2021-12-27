#include <stdio.h>

int x1, x2, y1, y2, ans;

void simulate(int xl, int xr, int vx, int vy) {
    int x = 0, y = 0;
    while (1) {
        x += vx; y += vy; if (vx) --vx; --vy;
        if ((xl <= x && x <= xr) && (y1 <= y && y <= y2)) { ++ans; return; }
        if (x > xr || y < y1) return;
    }
}

int main() {
    scanf("target area: x=%d..%d, y=%d..%d", &x1, &x2, &y1, &y2);
    if (x1 <= 0 && 0 <= x2) {
        for (int y = -300; y <= (-1 - y1); ++y)
            for (int x = -1; x >= -100; --x)
                simulate(0, -x1, -x, y);
        for (int y = -300; y <= (-1 - y1); ++y)
            for (int x = 0; x <= 100; ++x)
                simulate(0, x2, x, y);
    } else if (x2 <= 0) {
        for (int y = -300; y <= (-1 - y1); ++y)
            for (int x = 0; x >= -100; --x)
                simulate(-x2, -x1, -x, y);
    } else {
        for (int y = -300; y <= (-1 - y1); ++y)
            for (int x = 0; x <= 100; ++x)
                simulate(x1, x2, x, y);
    }
    printf("%d\n", ans);
    return 0;
}