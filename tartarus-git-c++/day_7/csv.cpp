#include <iostream>
#include <fstream>
#include <vector>

#include "../puzzle.h"

int main() {
	std::ifstream input("input.data");
	std::ofstream output("output.csv");
	std::vector<unsigned long long> thing = puzzle::input::parseList(input);
	output << "spaceships\n";
	for (int i = 0; i < thing.size(); i++) {
		output << thing[i] << "\n";
	}
	output.close();
	input.close();
}
