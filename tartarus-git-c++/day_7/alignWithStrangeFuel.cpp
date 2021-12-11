#include <iostream>
#include <fstream>
#include <vector>

#include "../puzzle.h"

int main() {
	std::ifstream input("input.data");
	std::vector<unsigned long long> crabs = puzzle::input::parseList(input);
	unsigned long long shortestFuel = 100000000;
	unsigned long long bestCrab = 0;
	for (int i = 0; i < 2000; i++) {
		unsigned long long currentFuel = 0;
		for (int j = 0; j < crabs.size(); j++) {
			unsigned long long temp;
			if (i > crabs[j]) { temp = i - crabs[j]; }
			else { temp = crabs[j] - i; }
			currentFuel += (temp * temp + temp) / 2;
		}
		if (currentFuel < shortestFuel) { shortestFuel = currentFuel; bestCrab = i; }
	}
	std::cout << shortestFuel << std::endl;
	input.close();
}
