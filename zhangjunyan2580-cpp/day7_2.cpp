#include <stdio.h>
#include <algorithm>

int a[10005];
int n, p;
long long ans = 0x7f7f7f7f7f7f7f7fll, sum, sp;

long long calc(int v) {
	long long ans = 0;
	for (int i = 0; i < n; ++i) {
		int dist = abs(a[i] - v);
		ans += (long long) dist * (dist + 1) >> 1;
	}
	return ans;
}

int main() {
	while (1) {
		char ch;
		scanf("%d%c", a + n, &ch);
		sp += a[n]; ++n;
		if (ch != ',') break;
	}
	printf("%lld\n", std::min(calc(sp / n), calc(sp / n + 1)));
	return 0;
}
