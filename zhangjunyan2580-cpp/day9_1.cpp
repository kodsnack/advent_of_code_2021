#include <stdio.h>
#include <string.h>

int n, m;
char str[1005];
int map[1005][1005];
int ans;

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
				(j == m || map[i][j] < map[i][j + 1]))
				ans += map[i][j] + 1;
	printf("%d\n", ans);
	return 0;
}
