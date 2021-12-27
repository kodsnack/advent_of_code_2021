#include <stdio.h>
#include <vector>
#include <string.h>

int c[32][2], len, g;
char str[32];

int main() {
	while (~scanf(" %s", str)) {
		len = strlen(str);
		for (int i = 1; i <= len; ++i)
			++c[i - 1][str[len - i] & 1];
	}
	for (int i = 0; i < len; ++i)
		g |= (c[i][0] > c[i][1] ? 0 : 1) << i;
	printf("%d\n", g * (((1 << len) - 1) ^ g));
	return 0;
} 
