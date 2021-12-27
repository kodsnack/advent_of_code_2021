#include <stdio.h>

char str[1005];
int x, y, v;

int main() {
	while (~scanf(" %[^\n]", str)) {
		if (*str == 'f') {
			sscanf(str, "forward %d", &v);
			x += v;
		} else if (*str == 'd') {
			sscanf(str, "down %d", &v);
			y += v;
		} else if (*str == 'u') {
			sscanf(str, "up %d", &v);
			y -= v;
		}
	}
	printf("%d\n", x * y);
	return 0;
}
