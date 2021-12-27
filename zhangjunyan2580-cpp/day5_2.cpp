#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

int pcnt[1005][1005];
int ans;

int x1, y1, x2, y2;

int main() {
	while (~scanf("%d,%d -> %d,%d", &x1, &y1, &x2, &y2)) {
		if (x1 == x2) {
			if (y1 > y2) std::swap(y1, y2);
			for (int i = y1; i <= y2; ++i)
				++pcnt[x1][i];
		} else if (y1 == y2) {
			if (x1 > x2) std::swap(x1, x2);
			for (int i = x1; i <= x2; ++i)
				++pcnt[i][y1];
		} else {
			if (x1 > x2) std::swap(x1, x2), std::swap(y1, y2);
			if (y1 < y2)
				for (int i = x1, j = y1; i <= x2; ++i, ++j)
					++pcnt[i][j];
			else
				for (int i = x1, j = y1; i <= x2; ++i, --j)
					++pcnt[i][j];
		}
	}
	for (int i = 0; i < 1000; ++i)
		for (int j = 0; j < 1000; ++j)
			if (pcnt[i][j] >= 2) ++ans;
	printf("%d\n", ans);
	return 0;
}
