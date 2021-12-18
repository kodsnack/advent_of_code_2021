#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>

int main() {
	std::ifstream filein("input.data");
	std::string line;
	unsigned int numOfIncreased = 0;
	std::getline(filein, line);
	int previousNum = atoi(line.c_str());
	while (std::getline(filein, line)) {
		int num = atoi(line.c_str());
		if (num > previousNum) { numOfIncreased++; }
		previousNum = num;
	}
	filein.close();
	std::cout << numOfIncreased << std::endl;
}
