#include <stdio.h>
#include <string.h>

#include <queue>

int energy[10][10];
int n, m, ans;
char str[15];

bool vis[10][10];

const int dx[8] = { 1, 1, 1, 0, 0, -1, -1, -1 }, dy[8] = { 1, 0, -1, 1, -1, 1, 0, -1 };

void flash(int x, int y) {
	std::queue<int> X, Y;
	X.push(x); Y.push(y);
	vis[x][y] = 1; ++ans;
	while (X.size()) {
		int nx = X.front(), ny = Y.front(); X.pop(); Y.pop();
		for (int i = 0; i < 8; ++i) {
			int px = nx + dx[i], py = ny + dy[i];
			if (px < 0 || px >= n || py < 0 || py >= m) continue;
			++energy[px][py];
			if (vis[px][py] || energy[px][py] < 10) continue;
			vis[px][py] = 1; ++ans;
			X.push(px); Y.push(py);
		}
	}
}

void step() {
	memset(vis, 0, sizeof(vis));
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			++energy[i][j];
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (energy[i][j] > 9 && !vis[i][j])
				flash(i, j);
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			if (vis[i][j])
				energy[i][j] = 0;
}

int main() {
	while (~scanf(" %s", str)) {
		m = strlen(str);
		for (int i = 0; i < m; ++i) energy[n][i] = str[i] ^ '0';
		++n;
	}
	for (int i = 0; i < 100; ++i) step();
	printf("%d\n", ans);
	return 0;
}
