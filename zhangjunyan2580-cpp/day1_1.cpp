#include <stdio.h>

int a, lst = 0x3f3f3f3f, cnt;

int main() {
	while (~scanf("%d", &a)) {
		if (a > lst) ++cnt;
		lst = a;
	}
	printf("%d", cnt); return 0;
}
