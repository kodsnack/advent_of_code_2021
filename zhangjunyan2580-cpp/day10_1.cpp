#include <stdio.h>

char str[205], stk[205];
int head, ans;

int main() {
	while (~scanf(" %s", str)) {
		for (char *s = str; *s; ++s) {
			if (*s == ')') {
				if (!head || stk[head] != '(') { ans += 3; break; }
				--head;
			} else if (*s == ']') {
				if (!head || stk[head] != '[') { ans += 57; break; }
				--head;
			} else if (*s == '}') {
				if (!head || stk[head] != '{') { ans += 1197; break; }
				--head;
			} else if (*s == '>') {
				if (!head || stk[head] != '<') { ans += 25137; break; }
				--head;
			} else stk[++head] = *s;
		}
		head = 0;
	}
	printf("%d\n", ans);
	return 0;
}
