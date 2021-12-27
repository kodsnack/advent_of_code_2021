#include <stdio.h>

int x1, x2, y1, y2;

int main() {
    scanf("target area: x=%d..%d, y=%d..%d", &x1, &x2, &y1, &y2);
    printf("%d\n", (-y1 * (-1 - y1)) >> 1);
    return 0;
}