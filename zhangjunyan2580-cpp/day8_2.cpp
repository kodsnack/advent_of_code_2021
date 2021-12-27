#include <stdio.h>
#include <algorithm>

struct Connect {
	int to[7];
	int transform(int v) {
		int new_v = 0;
		for (int i = 0; i < 7; ++i)
			if ((v >> i) & 1)
				new_v |= 1 << to[i];
		return new_v;
	}
} pattern;

const int digits[10] = { 0x77, 0x24, 0x5d, 0x6d, 0x2e, 0x6b, 0x7b, 0x25, 0x7f, 0x6f };

int ans;
int display[10], four[4];
char temp[10];

int digit(int v) {
	for (int i = 0; i < 10; ++i)
		if (v == digits[i]) return i;
	return -1;
}

int main() {
	while (1) {
		for (int i = 0; i < 10; ++i) {
			scanf(" %s", temp);
			if (feof(stdin)) {
				printf("%d\n", ans);
				return 0;
			} 
			display[i] = 0;
			for (char *s = temp; *s; ++s)
				display[i] |= 1 << (*s - 'a');
		}
		scanf(" %*c");
		for (int i = 0; i < 4; ++i) {
			scanf(" %s", temp);
			four[i] = 0;
			for (char *s = temp; *s; ++s)
				four[i] |= 1 << (*s - 'a');
		}
		for (int i = 0; i < 7; ++i)
			pattern.to[i] = i;
		do {
			bool legal = true;
			for (int i = 0; i < 10; ++i)
				if (digit(pattern.transform(display[i])) == -1) {
					legal = false;
					break;
				}
			if (legal) {
				ans += digit(pattern.transform(four[0])) * 1000 +
				       digit(pattern.transform(four[1])) * 100  +
				       digit(pattern.transform(four[2])) * 10   +
				       digit(pattern.transform(four[3]));
				break;
			}
		} while (std::next_permutation(pattern.to, pattern.to + 7));
	}
	return 0;
}
