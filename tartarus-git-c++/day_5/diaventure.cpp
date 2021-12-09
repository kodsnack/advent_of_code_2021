#include <iostream>
#include <fstream>
#include <vector>

#define WIDTH 1000
#define HEIGHT 1000

struct Line {
	unsigned int x1;
	unsigned int y1;
	unsigned int x2;
	unsigned int y2;

	Line() : x1(0), y1(0), x2(0), y2(0) { }
};

std::vector<Line> lines;

#define ASCII_NUM_START 48
#define ASCII_NUM_END 57

void parse(std::ifstream& input) {
	char character;
	unsigned int counter = 0;
	lines.push_back(Line());
	while (input.get(character)) {
		if (character >= ASCII_NUM_START && character <= ASCII_NUM_END) {
			unsigned int* line = (unsigned int*)&lines[lines.size() - 1];
			line[counter] = line[counter] * 10 + (character - ASCII_NUM_START);
		} else if (character == ',') {
			counter++;
		} else if (character == ' ') {
			counter++;
			for (int i = 0; i < 3; i++) { input.get(character); }
			continue;
		} else {
			counter = 0;
			lines.push_back(Line());
		}
	}
	lines.erase(lines.end());
}

unsigned int field[WIDTH][HEIGHT];

int main() {
	std::ifstream input("input.data");
	
	parse(input);		// Extract all the lines.

	for (int i = 0; i < lines.size(); i++) {
		Line& line = lines[i];
		int dirX = line.x2 - line.x1;
		if (dirX > 0) { dirX = 1; }
		else if (dirX < 0) { dirX = -1; }
		int dirY = line.y2 - line.y1;
		if (dirY > 0) { dirY = 1; }
		else if (dirY < 0) { dirY = -1; }
		int y = line.y1;
		for (int x = line.x1; ;) {
			field[y][x]++;
			if (y != line.y2) { y += dirY; x += dirX; } else {
				if (x != line.x2) { x += dirX; } else { break; } }
		}
	}

	unsigned int pointnum = 0;
	for (int i = 0; i < WIDTH * HEIGHT; i++) {
		if (field[0][i] >= 2) { pointnum++; }
	}

	std::cout << pointnum << std::endl;

	input.close();
}
