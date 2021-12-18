#include "../puzzle.h"

#include <bits/stdc++.h>
#include <iostream>

puzzle::data::Matrix<unsigned long long> field;

unsigned long long fill(size_t x, size_t y) {
	field[x][y] = 9;
	unsigned long long amountFilled = 1;
	if (field.contains(x + 1, y) && field[x + 1][y] != 9) { amountFilled += fill(x + 1, y); }
	if (field.contains(x - 1, y) && field[x - 1][y] != 9) { amountFilled += fill(x - 1, y); }
	if (field.contains(x, y + 1) && field[x][y + 1] != 9) { amountFilled += fill(x, y + 1); }
	if (field.contains(x, y - 1) && field[x][y - 1] != 9) { amountFilled += fill(x, y - 1); }
	return amountFilled;
}

int main() {
	std::string input = puzzle::input::importFile("input.data");
	std::vector<std::string> lines = puzzle::string::removeEmptyStrings(puzzle::string::split(input, '\n'));
	field = puzzle::data::Matrix<unsigned long long>(lines[0].length(), lines.size());
	for (int y = 0; y < field.height(); y++) { for (int x = 0; x < field.width(); x++) { field[x][y] = lines[y][x] - ASCII_NUM_BEGIN; } }

	std::vector<unsigned long long> basins;
	for (int i = 0; i < field.width() * field.height(); i++) { if (field.data()[i] != 9) { basins.push_back(fill(i % field.width(), i / field.width())); } }
	std::sort(basins.begin(), basins.end());

	std::cout << basins[basins.size() - 1] * basins[basins.size() - 2] * basins[basins.size() - 3] << std::endl;
}
