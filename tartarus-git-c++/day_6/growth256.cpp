#define ITERATIONS 256

#include <iostream>
#include <fstream>
#include <vector>

std::vector<unsigned int> fish;

#define ASCII_NUM_START 48
#define ASCII_NUM_END 57

void parse(std::ifstream& input) {
	fish.push_back(0);
	char character;
	while (input.get(character)) {
		if (character >= ASCII_NUM_START && character <= ASCII_NUM_END) { fish[fish.size() - 1] = fish[fish.size() - 1] * 10 + (character - ASCII_NUM_START); continue; }
		if (character == ',') { fish.push_back(0); }
	}
}

// SIDE-NOTE FOR ME: C++ isn't allowed to reorder structs because C wasn't allowed to reorder structs. Access modifiers(public, private, etc...) are new in C++ and the order of variables with different access modifiers isn't garanteed to be the same, so thats the only type of reordering C++ is allowed to do.
struct Bucket {
	unsigned long long fish;
	unsigned char stage;
};

Bucket buckets[9];

int main() {
	std::ifstream input("input.data");

	parse(input);

	for (int i = 0; i < 9; i++) { buckets[i].stage = i; buckets[i].fish = 0; }
	for (int i = 0; i < fish.size(); i++) { buckets[fish[i]].fish++; }

	for (int loops = 0; loops < ITERATIONS; loops++) {
		int num8;
		for (int i = 0; i < 9; i++) {
			if (buckets[i].stage != 0) { buckets[i].stage--; continue; }
			buckets[i].stage = 8;
			num8 = i;
		}
		for (int j = 0; j < 9; j++) {
			if (buckets[j].stage == 6) { buckets[j].fish += buckets[num8].fish; break; }
		}
		std::cout << loops << std::endl;
	}

	unsigned long long totalAmount = 0;
	for (int i = 0; i < 9; i++) { totalAmount += buckets[i].fish; }
	std::cout << totalAmount << std::endl;

	input.close();
}
