#include <stdio.h>
#include <vector>

struct Board {
	
	int number[5][5];
	int x[100], y[100];
	bool _mark[5][5];
	
	void init(int val[5][5]) {
		for (int i = 0; i < 100; ++i)
			x[i] = -1, y[i] = -1;
		for (int i = 0; i < 5; ++i)
			for (int j = 0; j < 5; ++j) {
				number[i][j] = val[i][j];
				_mark[i][j] = false;
				x[number[i][j]] = i;
				y[number[i][j]] = j;
			}
	}
	
	void mark(int val) {
		if (x[val] == -1 && y[val] == -1)
			return;
		_mark[x[val]][y[val]] = true;
	}
	
	int sum_unmark() {
		int sum = 0;
		for (int i = 0; i < 5; ++i)
			for (int j = 0; j < 5; ++j)
				if (!_mark[i][j])
					sum += number[i][j];
		return sum;
	}
	
	bool win() {
		bool won = false;
		for (int i = 0; i < 5; ++i)
			won = won || (_mark[i][0] && _mark[i][1] && _mark[i][2] && _mark[i][3] && _mark[i][4])
			          || (_mark[0][i] && _mark[1][i] && _mark[2][i] && _mark[3][i] && _mark[4][i]);
		return won;
	}
	
} B[1000];
int bcnt;

int win_time[1000], win_score[1000];

std::vector<int> num_list;
int nums[5][5];

int wi = -1;

int main() {
	while (true) {
		int val;
		char ch;
		scanf("%d%c", &val, &ch);
		num_list.push_back(val);
		if (ch != ',')
			break;
	}
	while (true) {
		bool Eof = false;
		for (int i = 0; i < 5; ++i) {
			for (int j = 0; j < 5; ++j) {
				scanf("%d", nums[i] + j);
				if (feof(stdin)) {
					Eof = true;
					break;
				}
			}
			if (Eof) break;
		}
		if (Eof) break;
		B[++bcnt].init(nums);
	}
	for (int i = 1; i <= bcnt; ++i) {
		for (int j = 0; j < (int) num_list.size(); ++j) {
			B[i].mark(num_list[j]);
			if (B[i].win()) {
				win_score[i] = B[i].sum_unmark() * num_list[j];
				win_time[i] = j;
				break;
			}
		}
		if (wi == -1 || win_time[i] < win_time[wi])
			wi = i;
	}
	printf("%d\n", win_score[wi]);
	return 0;
}
