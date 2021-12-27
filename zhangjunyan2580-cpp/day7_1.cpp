#include <stdio.h>
#include <algorithm>

int a[10005];
int n, ans;

int main() {
	while (1) {
		char ch;
		scanf("%d%c", a + n, &ch);
		++n;
		if (ch != ',') break;
	}
	std::sort(a, a + n);
	for (int i = 0; i < n; ++i)
		ans += std::abs(a[i] - a[n >> 1]);
	printf("%d\n", ans);
	return 0;
}
