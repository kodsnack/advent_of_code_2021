#include <stdio.h>
#include <set>
#include <string.h>

int len;
char str[32];
std::set<int> so, sc;

inline int common(std::set<int> &S, int k) {
	int c[2] = { 0, 0 };
	for (int v : S) ++c[(v >> k) & 1];
	return c[0] > c[1] ? 0 : 1;
}
inline void filter(std::set<int> &S, int k, int b) {
	int c[2] = { 0, 0 };
	for (auto it = S.begin(); it != S.end(); ) {
		auto nx = it;
		++nx;
		if (((*it >> k) & 1) != b)
			S.erase(it);
		it = nx;
	}
}

int main() {
	while (~scanf(" %s", str)) {
		len = strlen(str);
		int x = 0;
		for (int i = 0; i < len; ++i)
			x = (x << 1) | (str[i] & 1);
		so.insert(x); sc.insert(x);
	}
	for (int i = len - 1; i >= 0; --i) {
		int o = common(so, i);
		filter(so, i, o);
		if (so.size() == 1) break;
	}
	for (int i = len - 1; i >= 0; --i) {
		int c = common(sc, i) ^ 1;
		filter(sc, i, c);
		if (sc.size() == 1) break;
	}
	printf("%d\n", *so.begin() * *sc.begin());
	return 0;
} 
