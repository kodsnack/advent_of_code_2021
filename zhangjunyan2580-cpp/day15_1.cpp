#include <stdio.h>
#include <string.h>
#include <queue>

struct Node {
    int x, y, d;
    bool operator<(const Node &n) const { return d > n.d; }
};
std::priority_queue<Node> Q;

int w[205][205], dis[205][205];
char str[205];

constexpr int dx[4] = { 0, 1, 0, -1 }, dy[4] = { 1, 0, -1, 0 };

int n, m;

int main() {
    while (~scanf(" %s", str + 1)) {
        m = strlen(str + 1); ++n;
        for (int i = 1; i <= m; ++i)
            w[n][i] = str[i] ^ '0';
    }
    memset(dis, 0x3f, sizeof(dis));
    dis[1][1] = 0; Q.push((Node) { 1, 1, 0 });
    while (!Q.empty()) {
        Node u = Q.top(); Q.pop();
        for (int i = 0; i < 4; ++i) {
            int nx = u.x + dx[i], ny = u.y + dy[i];
            if (nx < 1 || nx > n || ny < 1 || ny > m || u.d + w[nx][ny] >= dis[nx][ny]) continue;
            dis[nx][ny] = u.d + w[nx][ny]; Q.push((Node) { nx, ny, u.d + w[nx][ny] });
        }
    }
    printf("%d\n", dis[n][m]);
    return 0;
}