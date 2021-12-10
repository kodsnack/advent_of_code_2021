#include <iostream>
#include <fstream>
#include <vector>

#include "../puzzle.h"

int main() {
	std::ifstream input("input.data");
	std::vector<unsigned long long> crabs = puzzle::input::parseList(input);
	unsigned long long shortestFuel = 100000000;
	unsigned long long bestCrab = 0;
	for (int i = 0; i < crabs.size(); i++) {
		unsigned long long currentFuel = 0;
		for (int j = 0; j < crabs.size(); j++) {
			if (crabs[i] > crabs[j]) { currentFuel += crabs[i] - crabs[j]; }
			else { currentFuel += crabs[j] - crabs[i]; }
		}
		if (currentFuel < shortestFuel) { shortestFuel = currentFuel; bestCrab = i; }
	}
	std::cout << shortestFuel << std::endl;
	input.close();
}
