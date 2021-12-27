#include <stdio.h>
#include <string.h>
#include <queue>

struct Node {
    int x, y, d;
    bool operator<(const Node &n) const { return d > n.d; }
};
std::priority_queue<Node> Q;

int w[1005][1005], dis[1005][1005];
char str[205];

constexpr int dx[4] = { 0, 1, 0, -1 }, dy[4] = { 1, 0, -1, 0 };

int n, m;

int main() {
    while (~scanf(" %s", str)) {
        m = strlen(str);
        for (int i = 0; i < m; ++i)
            w[n][i] = str[i] ^ '0';
        ++n;
    }
    for (int i = 0; i < 5 * n; ++i)
        for (int j = 0; j < 5 * m; ++j)
            w[i][j] = (w[i % n][j % m] + (i / n) + (j / m) - 1) % 9 + 1;
    memset(dis, 0x3f, sizeof(dis));
    dis[0][0] = 0; Q.push((Node) { 0, 0, 0 });
    while (!Q.empty()) {
        Node u = Q.top(); Q.pop();
        for (int i = 0; i < 4; ++i) {
            int nx = u.x + dx[i], ny = u.y + dy[i];
            if (nx < 0 || nx >= 5 * n || ny < 0 || ny >= 5 * m || u.d + w[nx][ny] >= dis[nx][ny]) continue;
            dis[nx][ny] = u.d + w[nx][ny]; Q.push((Node) { nx, ny, u.d + w[nx][ny] });
        }
    }
    printf("%d\n", dis[5 * n - 1][5 * m - 1]);
    return 0;
}