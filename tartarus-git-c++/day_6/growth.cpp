#define ITERATIONS 80

#include <iostream>
#include <fstream>
#include <vector>

std::vector<unsigned int> fish;
int prevSize;

#define ASCII_NUM_START 48
#define ASCII_NUM_END 57

void parse(std::ifstream& input) {
	fish.push_back(0);
	char character;
	while (input.get(character)) {
		if (character >= ASCII_NUM_START && character <= ASCII_NUM_END) { fish[fish.size() - 1] = fish[fish.size() - 1] * 10 + (character - ASCII_NUM_START); continue; }
		if (character == ',') { fish.push_back(0); }
	}
	prevSize = fish.size();
}

int main() {
	std::ifstream input("input.data");

	parse(input);

	for (int loops = 0; loops < ITERATIONS; loops++) {
	for (int i = 0; i < prevSize; i++) {
		if (fish[i] == 0) { fish[i] = 6; fish.push_back(8); continue; }
		fish[i]--;
	}
	prevSize = fish.size();
	}

	std::cout << fish.size() << std::endl;

	input.close();
}
