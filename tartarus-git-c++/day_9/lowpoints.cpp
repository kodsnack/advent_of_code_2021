#include "../puzzle.h"

#include <iostream>
#include <tuple>

int main() {
	std::string input = puzzle::input::importFile("input.data");
	std::vector<std::string> lines = puzzle::string::removeEmptyStrings(puzzle::string::split(input, '\n'));
	size_t width = lines[0].length();
	size_t height = lines.size();
	size_t map_len = height * width;
	char* map = new char[map_len];
	for (int x = 0; x < width; x++) { for (int y = 0; y < height; y++) { map[y * width + x] = lines[y][x] - ASCII_NUM_BEGIN; } }

	// Go through the map and see where the low points are:
	std::vector<std::tuple<int, int>> lowpoints;
	for (int y = 0; y < height; y++) {
		for (int x = 0; x < width; x++) {
			char value = map[y * width + x];
			if (x > 0) {
				if (map[y * width + x - 1] <= value) { continue; }
			}
			if (x < width - 1) {
				if (map[y * width + x + 1] <= value) { continue; }
			}
			if (y > 0) {
				if (map[(y - 1) * width + x] <= value) { continue; }
			}
			if (y < height - 1) {
				if (map[(y + 1) * width + x] <= value) { continue; }
			}
			lowpoints.push_back(std::make_tuple(x, y));
		}
	}

	// Use calculated lowpoints:
	unsigned long long riskSum = 0;
	for (int i = 0; i < lowpoints.size(); i++) {
		riskSum += map[std::get<1>(lowpoints[i]) * width + std::get<0>(lowpoints[i])] + 1;
	}

	delete[] map;

	std::cout << riskSum << std::endl;
}
