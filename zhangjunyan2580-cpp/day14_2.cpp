#include <stdio.h>
#include <string.h>

long long buck[30][30], new_buck[30][30], cnt[30], aa = 0x3f3f3f3f3f3f3f3fll, ai;
int to[30][30];
char pa[30], f[30], t[30];

int L;

void simulate() {
	for (int i = 0; i < 26; ++i)
		for (int j = 0; j < 26; ++j)
			if (to[i][j] != -1) new_buck[i][to[i][j]] += buck[i][j], new_buck[to[i][j]][j] += buck[i][j];
			else new_buck[i][j] += buck[i][j];
	memcpy(buck, new_buck, sizeof(buck));
	memset(new_buck, 0, sizeof(new_buck));
}

int main() {
	memset(to, -1, sizeof(to));
	scanf("%s", pa);
	while (~scanf(" %s -> %s", f, t)) to[*f - 'A'][*(f + 1) - 'A'] = *t - 'A';
	for (char *s = pa + 1; *s; ++s) ++buck[*(s - 1) - 'A'][*s - 'A'], ++L;
	for (int i = 0; i < 40; ++i) simulate();
	for (int i = 0; i < 26; ++i)
		for (int j = 0; j < 26; ++j)
			cnt[i] += buck[i][j], cnt[j] += buck[i][j];
	++cnt[*pa - 'A']; ++cnt[*(pa + L) - 'A'];
	for (int i = 0; i < 26; ++i) {
		if (!cnt[i]) continue;
		cnt[i] >>= 1;
		if (cnt[i] < aa) aa = cnt[i];
		if (cnt[i] > ai) ai = cnt[i];
	}
	printf("%lld", ai - aa);
	return 0;
}
