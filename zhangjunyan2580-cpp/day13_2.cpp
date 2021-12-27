#include <stdio.h>
#include <algorithm>
#include <string.h>

int n, m;
char str[105];

struct Point {
	int x, y;
} P[5005];
int cnt;

char buck[105][105];

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
		scanf(" %[^\n]", str);
	}
	memset(buck, '.', sizeof(buck));
	for (int i = 1; i <= cnt; ++i)
		buck[P[i].x][P[i].y] = '#';
	for (int i = 0; i < 100; ++i) buck[i][100] = 0, printf("%s\n", buck[i]);
	return 0;
}
