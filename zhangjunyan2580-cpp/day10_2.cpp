#include <stdio.h>
#include <algorithm>
#include <stdint.h>

char str[205], stk[205];
int head, cnt;

long long ans[1005];

int main() {
	while (~scanf(" %s", str)) {
		bool legal = true;
		head = 0;
		for (char *s = str; *s; ++s) {
			if (*s == ')') {
				if (!head || stk[head] != '(') { legal = false; break; }
				--head;
			} else if (*s == ']') {
				if (!head || stk[head] != '[') { legal = false; break; }
				--head;
			} else if (*s == '}') {
				if (!head || stk[head] != '{') { legal = false; break; }
				--head;
			} else if (*s == '>') {
				if (!head || stk[head] != '<') { legal = false; break; }
				--head;
			} else stk[++head] = *s;
		}
		if (!legal) continue;
		long long sum = 0;
		while (head) {
			if (stk[head] == '(') sum = sum * 5 + 1;
			else if (stk[head] == '[') sum = sum * 5 + 2;
			else if (stk[head] == '{') sum = sum * 5 + 3;
			else sum = sum * 5 + 4;
			--head;
		}
		ans[++cnt] = sum;
	}
	std::sort(ans + 1, ans + cnt + 1);
	printf("%lld\n", ans[(cnt >> 1) + 1]);
	return 0;
}
