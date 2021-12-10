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
		if (lines[i].x1 != lines[i].x2) {
			if (lines[i].y1 != lines[i].y2) {
				lines.erase(lines.begin() + i); i--;
			}
		}
	}

	for (int i = 0; i < lines.size(); i++) {
		Line& line = lines[i];
		if (line.x1 == line.x2) {
			for (int y = line.y1; (line.y2 > line.y1 && y <= line.y2) || (line.y2 <= line.y1 && y >= line.y2); line.y2 > line.y1 ? y++ : y--) {
				field[y][line.x1]++;
			}
			continue;
		}
		for (int x = line.x1; (line.x2 > line.x1 && x <= line.x2) || (line.x2 <= line.x1 && x >= line.x2); line.x2 > line.x1 ? x++ : x--) {
			field[line.y1][x]++;
		}
	}

	unsigned int pointnum = 0;
	for (int i = 0; i < WIDTH * HEIGHT; i++) {
		if (field[0][i] >= 2) { pointnum++; }
	}

	std::cout << pointnum << std::endl;

	input.close();
}
