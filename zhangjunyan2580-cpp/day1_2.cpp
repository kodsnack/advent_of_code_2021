#include <stdio.h>

int a, lst1 = 0x3f3f3f3f, lst2 = 0x3f3f3f3f, lst3 = 0x3f3f3f3f, cnt;

int main() {
	while (~scanf("%d", &a)) {
		if (a > lst3) ++cnt;
		lst3 = lst2; lst2 = lst1; lst1 = a;
	}
	printf("%d", cnt); return 0;
}
