#include <stdio.h>
#include <string.h>
#include <algorithm>

int n, m;
char str[1005];
int map[1005][1005];
bool p[1005][1005];
int ans;

int qx[100005], qy[100005], head = 1, tail;
int sl[100005], cnt;

int main() {
	while (~scanf(" %s", str + 1)) {
		++n;
		m = strlen(str + 1);
		for (int i = 1; i <= m; ++i) map[n][i] = str[i] - '0';
	}
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= m; ++j)
			if ((i == 1 || map[i][j] < map[i - 1][j]) &&
			    (i == n || map[i][j] < map[i + 1][j]) &&
				(j == 1 || map[i][j] < map[i][j - 1]) &&
				(j == m || map[i][j] < map[i][j + 1])) {
					qx[++tail] = i; qy[tail] = j;
					int nc = 0;
					while (head <= tail) {
						int nx = qx[head], ny = qy[head]; ++head;
						if (p[nx][ny] || map[nx][ny] == 9) continue;
						++nc; p[nx][ny] = 1;
						if (nx != 1 && map[nx - 1][ny] > map[nx][ny]) qx[++tail] = nx - 1, qy[tail] = ny;
						if (nx != n && map[nx + 1][ny] > map[nx][ny]) qx[++tail] = nx + 1, qy[tail] = ny;
						if (ny != 1 && map[nx][ny - 1] > map[nx][ny]) qx[++tail] = nx, qy[tail] = ny - 1;
						if (ny != m && map[nx][ny + 1] > map[nx][ny]) qx[++tail] = nx, qy[tail] = ny + 1;
					}
					sl[++cnt] = nc;
				}
	std::sort(sl + 1, sl + cnt + 1);
	printf("%d\n", sl[cnt] * sl[cnt - 1] * sl[cnt - 2]);
	return 0;
}
