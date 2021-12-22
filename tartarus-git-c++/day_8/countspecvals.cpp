#include <iostream>
#include <fstream>

#include "../puzzle.h"

struct Line {
	std::vector<std::string> signals;
	std::vector<std::string> outputs;
};

std::vector<Line> displays;

int main() {
	// Parse input.
	std::string input = puzzle::input::importFile("input.data");
	std::vector<std::string> lines = puzzle::string::split(input, '\n');
	if (lines.back().size() == 0) { lines.erase(lines.end()); }
	for (size_t i = 0; i < lines.size(); i++) {
		std::vector<std::string> parts = puzzle::string::split(lines[i], " | ");
		std::vector<std::string> signals = puzzle::string::split(parts[0], ' ');
		std::vector<std::string> outputs = puzzle::string::split(parts[1], ' ');
		displays.push_back({ signals, outputs });
	}

	// Working with input.
	unsigned long long counter = 0;
	for (int i = 0; i < displays.size(); i++) {
		for (int j = 0; j < displays[i].outputs.size(); j++) {
			size_t len = displays[i].outputs[j].length();
			if (len == 2 || len == 4 || len == 7 || len == 3) { counter++; }
		}
	}
	std::cout << counter << std::endl;
}
