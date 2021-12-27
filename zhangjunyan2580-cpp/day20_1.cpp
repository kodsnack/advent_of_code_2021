#include <string.h>
#include <stdio.h>
#include <vector>

bool cv[512];
char str[600];

struct Image {
    std::vector< std::vector<bool> > P;
    bool inf_state;
    void trans() {
        std::vector< std::vector<bool> > N(P.size() + 2, std::vector<bool>(P.size() + 2));
        for (int i = 0; i < (int) N.size(); ++i)
            for (int j = 0; j < (int) N.size(); ++j) {
                int num = 0;
                for (int k = i - 2; k <= i; ++k)
                    for (int l = j - 2; l <= j; ++l)
                        num = (num << 1) | ((k < 0 || k >= (int) P.size() || l < 0 || l >= (int) P.size()) ? inf_state : bool(P[k][l]));
                N[i][j] = cv[num];
            }
        P = N;
        inf_state = cv[inf_state ? 511 : 0];
    }
    void _debug() {
        for (const auto& i : P) {
            for (const auto &j : i)
                putchar(j ? '#' : '.');
            putchar('\n');
        }
        printf("inf_state=%c\n", inf_state ? '#' : '.');
    }
} I;

int n;

int main() {
    scanf("%s ", str);
    for (char *s = str; *s; ++s) cv[s - str] = *s == '#';
    while (fgets(str, 200, stdin)) {
        n = strlen(str);
        if (*(str + n - 1) == '\n') str[--n] = 0;
        I.P.push_back(std::vector<bool>(n));
        for (char *s = str; *s; ++s) I.P.back()[s - str] = *s == '#';
    }
    for (int i = 0; i < 2; ++i) I.trans(), I._debug();
    int ans = 0;
    for (const auto& i : I.P)
        for (const auto &j : i)
            ans += j;
    printf("%d\n", ans);
    return 0;
}