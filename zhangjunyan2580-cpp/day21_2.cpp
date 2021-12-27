#include <stdio.h>
#include <algorithm>

// dp[i][j][k][l][m]:
// the first player's score = i,
// the second player's score = j,
// the first player's position = k,
// the second player's position = l,
// now is player m's turn
long long dp[35][35][15][15][2], A, B;
constexpr int p[10] = { 0, 0, 0, 1, 3, 6, 7, 6, 3, 1 };

int a, b;

int main() {
    scanf("Player 1 starting position: %d Player 2 starting position: %d", &a, &b);
    dp[0][0][a][b][0] = 1;
    for (int sa = 0; sa < 21; ++sa)
        for (int sb = 0; sb < 21; ++sb)
            for (int posa = 1; posa <= 10; ++posa)
                for (int posb = 1; posb <= 10; ++posb)
                    for (int step = 3; step <= 9; ++step) {
                        int to_pos = (posa + step - 1) % 10 + 1;
                        dp[sa + to_pos][sb][to_pos][posb][1] += dp[sa][sb][posa][posb][0] * p[step];
                        to_pos = (posb + step - 1) % 10 + 1;
                        dp[sa][sb + to_pos][posa][to_pos][0] += dp[sa][sb][posa][posb][1] * p[step];
                    }
    for (int sa = 21; sa <= 30; ++sa)
        for (int sb = 0; sb < 21; ++sb)
            for (int posa = 1; posa <= 10; ++posa)
                for (int posb = 1; posb <= 10; ++posb)
                    A += dp[sa][sb][posa][posb][1];
    for (int sa = 0; sa < 21; ++sa)
        for (int sb = 21; sb <= 30; ++sb)
            for (int posa = 1; posa <= 10; ++posa)
                for (int posb = 1; posb <= 10; ++posb)
                    A += dp[sa][sb][posa][posb][1];
    printf("%lld\n", std::max(A, B));
    return 0;
}