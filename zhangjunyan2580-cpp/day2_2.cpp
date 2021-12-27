#include <stdio.h>

char str[1005];
int x, y, v, aim;

int main() {
	while (~scanf(" %[^\n]", str)) {
		if (*str == 'f') {
			sscanf(str, "forward %d", &v);
			x += v;
			y += aim * v;
		} else if (*str == 'd') {
			sscanf(str, "down %d", &v);
			aim += v;
		} else if (*str == 'u') {
			sscanf(str, "up %d", &v);
			aim -= v;
		}
	}
	printf("%lld\n", (long long) x * y);
	return 0;
}
