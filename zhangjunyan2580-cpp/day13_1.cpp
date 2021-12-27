#include <stdio.h>
#include <algorithm>

int n, m;
char str[105];

struct Point {
	int x, y;
} P[5005];
int cnt;

void fold_y(int y) {
	for (int i = 1; i <= cnt; ++i)
		if (P[i].y > y) P[i].y = 2 * y - P[i].y;
}
void fold_x(int x) {
	for (int i = 1; i <= cnt; ++i)
		if (P[i].x > x) P[i].x = 2 * x - P[i].x;
}

int main() {
	while (1) {
		scanf(" %[^\n]", str);
		if (*str == 'f') break;
		int x, y;
		sscanf(str, "%d,%d", &x, &y);
		P[++cnt].x = x; P[cnt].y = y;
	}
	while (1) {
		if (*str != 'f') break;
		int u; char t;
		sscanf(str, "fold along %c=%d", &t, &u);
		if (t == 'x') fold_x(u);
		else fold_y(u);
		break;
		scanf(" %[^\n]", str);
	}
	std::sort(P + 1, P + cnt + 1, [](const Point &a, const Point &b) { return a.x == b.x ? a.y < b.y : a.x < b.x; });
	cnt = std::unique(P + 1, P + cnt + 1, [](const Point &a, const Point &b) { return a.x == b.x && a.y == b.y; }) - P - 1;
	printf("%d\n", cnt);
	return 0;
}
