#include <stdio.h>
#include <algorithm>

struct Dice {
    int state;
    Dice() { state = 99; }
    int operator()() { return (++state %= 100) + 1; }
} D;

int a, b, sa, sb;

int main() {
    scanf("Player 1 starting position: %d Player 2 starting position: %d", &a, &b);
    --a; --b;
    for (int i = 1; ; ++i) {
        (a += D() + D() + D()) %= 10;
        sa += a + 1;
        if (sa >= 1000) {
            printf("%d\n", sb * i * 3);
            return 0;
        }
        std::swap(sa, sb); std::swap(a, b);
    }
}