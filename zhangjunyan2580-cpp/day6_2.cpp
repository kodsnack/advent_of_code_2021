#include <stdio.h>
#include <string.h>

struct Matrix {
	
	int n, m;
	long long a[9][9];
	
	Matrix operator*(const Matrix &M) const {
		Matrix ans;
		ans.n = n; ans.m = M.m;
		memset(ans.a, 0, sizeof(ans.a));
		for (int i = 0; i < 9; ++i)
			for (int j = 0; j < 9; ++j)
				for (int k = 0; k < 9; ++k)
					ans.a[i][k] += a[i][j] * M.a[j][k];
		return ans;
	}
	
} E, A, B;

inline Matrix power(const Matrix &a, int p) {
	Matrix v = a, ans = E;
	while (p) {
		if (p & 1) ans = ans * v;
		v = v * v; p >>= 1;
	}
	return ans;
}

long long ans;

int main() {
	E.n = 9; E.m = 9;
	for (int i = 0; i < 9; ++i) E.a[i][i] = 1;
	A.n = 9; A.m = 9;
	for (int i = 1; i < 9; ++i) A.a[i - 1][i] = 1;
	A.a[6][0] = 1; A.a[8][0] = 1;
	B.n = 9; B.m = 1;
	while (1) {
		int x; char ch;
		scanf("%d%c", &x, &ch);
		++B.a[x][0];
		if (ch != ',') break;
	}
	B = power(A, 256) * B;
	for (int i = 0; i < 9; ++i)
		ans += B.a[i][0];
	printf("%lld\n", ans);
	return 0;
} 
