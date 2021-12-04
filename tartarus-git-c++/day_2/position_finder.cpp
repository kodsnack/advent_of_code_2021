#include <iostream>
#include <fstream>
#include <cstdlib>

int main() {
	std::ifstream filein("input.data");
	std::string line;
	int horizontal = 0;
	int depth = 0;
	while (std::getline(filein, line)) {
		if (line[0] == 'f') {
			// forward
			std::string number = line.substr(8);	// start of number
			horizontal += atoi(number.c_str());
		} else if (line[0] == 'd') {
			// down
			std::string number = line.substr(5);	// start of number
			depth += atoi(number.c_str());
		} else {
			// up
			std::string number = line.substr(3);
			depth -= atoi(number.c_str());
		}
	}
	std::cout << horizontal * depth << std::endl;
	filein.close();
}
