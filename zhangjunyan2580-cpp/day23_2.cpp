#include <stdio.h>
#include <queue>
#include <set>

struct State {
    int x[7], room[4][4];
    bool operator<(const State &s) const {
        for (int i = 0; i < 7; ++i) {
            if (x[i] < s.x[i]) return 1;
            if (x[i] > s.x[i]) return 0;
        }
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j) {
                if (room[i][j] < s.room[i][j]) return 1;
                if (room[i][j] > s.room[i][j]) return 0;
            }
        return 0;
    }
    bool operator==(const State &s) const {
        for (int i = 0; i < 7; ++i)
            if (x[i] != s.x[i]) return 0;
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                if (room[i][j] != s.room[i][j]) return 0;
        return 1;
    }
};

State start, end;

struct Node {
    State s;
    int d;
    bool operator<(const Node &n) const { return d > n.d; } 
};

constexpr int x_to_room[7][4][4] = {
    { { 3, 4, 5, 6 }, { 5, 6, 7, 8 }, { 7, 8, 9, 10 }, { 9, 10, 11, 12 } },
    { { 2, 3, 4, 5 }, { 4, 5, 6, 7 }, { 6, 7, 8, 9 }, { 8, 9, 10, 11 } },
    { { 2, 3, 4, 5 }, { 2, 3, 4, 5 }, { 4, 5, 6, 7 }, { 6, 7, 8, 9 } },
    { { 4, 5, 6, 7 }, { 2, 3, 4, 5 }, { 2, 3, 4, 5 }, { 4, 5, 6, 7 } },
    { { 6, 7, 8, 9 }, { 4, 5, 6, 7 }, { 2, 3, 4, 5 }, { 2, 3, 4, 5 } },
    { { 8, 9, 10, 11 }, { 6, 7, 8, 9 }, { 4, 5, 6, 7 }, { 2, 3, 4, 5 } },
    { { 9, 10, 11, 12 }, { 7, 8, 9 ,10 }, { 5, 6, 7, 8 }, { 3, 4, 5, 6 } }
};
constexpr int multi[5] = { 0, 1, 10, 100, 1000 };

int bfs(State start) {
    std::priority_queue<Node> Q;
    std::set<State> vis;
    Q.push((Node) { start, 0 });
    while (!Q.empty()) {
        Node state = Q.top(); State new_s = state.s; Q.pop();
        if (vis.count(state.s)) continue;
        vis.insert(state.s);
        if (state.s == end) return state.d;
        for (int i = 0; i < 7; ++i)
            if (state.s.x[i]) {
                for (int j = i - 1; j >= 0; --j) {
                    if (j >= 1 && j <= 4 && state.s.x[i] == j && !state.s.room[j - 1][0])
                        for (int k = 3; k >= 0; --k)
                            if (!state.s.room[j - 1][k]) {
                                new_s.room[j - 1][k] = state.s.x[i];
                                new_s.x[i] = 0;
                                Q.push((Node) { new_s, state.d + x_to_room[i][j - 1][k] * multi[state.s.x[i]] });
                                new_s.room[j - 1][k] = 0;
                                new_s.x[i] = state.s.x[i];
                                break;
                            } else if (state.s.room[j - 1][k] != j) break;
                    if (state.s.x[j]) break;
                }
                for (int j = i + 1; j < 7; ++j) {
                    if (j <= 5 && j >= 2 && state.s.x[i] == j - 1 && !state.s.room[j - 2][0])
                        for (int k = 3; k >= 0; --k)
                            if (!state.s.room[j - 2][k]) {
                                new_s.room[j - 2][k] = state.s.x[i];
                                new_s.x[i] = 0;
                                Q.push((Node) { new_s, state.d + x_to_room[i][j - 2][k] * multi[state.s.x[i]] });
                                new_s.room[j - 2][k] = 0;
                                new_s.x[i] = state.s.x[i];
                                break;
                            } else if (state.s.room[j - 2][k] != j - 1) break;
                    if (state.s.x[j]) break;
                }
            }
        for (int i = 0; i < 4; ++i)
            for (int j = 0; j < 4; ++j)
                if (state.s.room[i][j]) {
                    for (int k = i + 1; k >= 0; --k) {
                        if (state.s.x[k]) break;
                        new_s.x[k] = state.s.room[i][j];
                        new_s.room[i][j] = 0;
                        Q.push((Node) { new_s, state.d + x_to_room[k][i][j] * multi[state.s.room[i][j]] });
                        new_s.x[k] = 0;
                        new_s.room[i][j] = state.s.room[i][j];
                    }
                    for (int k = i + 2; k < 7; ++k) {
                        if (state.s.x[k]) break;
                        new_s.x[k] = state.s.room[i][j];
                        new_s.room[i][j] = 0;
                        Q.push((Node) { new_s, state.d + x_to_room[k][i][j] * multi[state.s.room[i][j]] });
                        new_s.x[k] = 0;
                        new_s.room[i][j] = state.s.room[i][j];
                    }
                    break;
                }
    }
    return -1;
}

int main() {
    char ch = '#';
    for (int i = 0; i < 2; ++i)
        for (int j = 0; j < 4; ++j) {
            while (ch == '.' || ch == '#' || ch == ' ' || ch == '\r' || ch == '\n') ch = getchar();
            start.room[j][i ? 3 : 0] = ch - 64; ch = getchar();
        }
    start.room[0][1] = 4; start.room[1][1] = 3; start.room[2][1] = 2; start.room[3][1] = 1;
    start.room[0][2] = 4; start.room[1][2] = 2; start.room[2][2] = 1; start.room[3][2] = 3;
    for (int j = 0; j < 4; ++j)
        for (int i = 0; i < 4; ++i)
            end.room[j][i] = j + 1;
    printf("%d\n", bfs(start));
    return 0;
}