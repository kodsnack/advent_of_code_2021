#include <stdio.h>
#include <string.h>

int state[205][205], new_state[205][205];
int n, m;

char str[205];

void print() {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j)
            putchar(state[i][j] == 1 ? '>' : (state[i][j] == 2 ? 'v' : '.'));
        putchar(10);
    }
    putchar(10);
}

bool simulate() {
    // print();
    bool M = false;
    memset(new_state, 0, sizeof(new_state));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (state[i][j] == 1 && !state[i][(j + 1) % m]) new_state[i][(j + 1) % m] = 1, M = true;
            else if (state[i][j]) new_state[i][j] = state[i][j];
    memcpy(state, new_state, sizeof(state));
    memset(new_state, 0, sizeof(new_state));
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (state[i][j] == 2 && !state[(i + 1) % n][j]) new_state[(i + 1) % n][j] = 2, M = true;
            else if (state[i][j]) new_state[i][j] = state[i][j];
    memcpy(state, new_state, sizeof(state));
    return M;
}

int main() {
    while (~scanf(" %s", str)) {
        m = strlen(str);
        for (int i = 0; i < m; ++i) state[n][i] = str[i] == '>' ? 1 : (str[i] == 'v' ? 2 : 0);
        ++n;
    }
    for (int i = 1; ; ++i)
        if (!simulate()) { printf("%d\n", i); break; }
    return 0;
}