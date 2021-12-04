#include <iostream>
#include <fstream>
#include <vector>

std::vector<int> numbers;

struct Board {
	int values[5][5];

	Board() {
		for (int i = 0; i < 25; i++) {
			values[0][i] = 0;
		}
	}

	int sumUnmarked() {
		int sum = 0;
		for (int i = 0; i < 25; i++) {
			if (values[0][i] != -1) { sum += values[0][i]; }
		}
		return sum;
	}

	int checkBoard(int num) {
		for (int i = 0; i < 25; i++) {
			if (values[0][i] == num) { values[0][i] = -1; }
		}

		for (int y = 0; y < 5; y++) {
			bool failed = false;
			for (int x = 0; x < 5; x++) {
				if (values[y][x] != -1) {
					failed = true;
				}
			}
			if (!failed) { return sumUnmarked() * num; }
		}


		for (int x = 0; x < 5; x++) {
			bool failed = false;
			for (int y = 0; y < 5; y++) {
				if (values[y][x] != -1) {
					failed = true;
				}
			}
			if (!failed) { return sumUnmarked() * num; }
		}
		return -1;
	}
};

std::vector<Board> boards;

#define ASCII_NUM_START 48
#define ASCII_NUM_END   57

bool parseBoard(std::ifstream& filein) {
	boards.push_back(Board());
	char character;
	int valueindex = 0;
	while (filein.get(character)) {
label:
		if (character >= ASCII_NUM_START && character <= ASCII_NUM_END) { boards[boards.size() - 1].values[0][valueindex] = 10 * boards[boards.size() - 1].values[0][valueindex] + (character - ASCII_NUM_START); }
		else if (character == ' ') { filein.get(character); valueindex++; if (character == ' ') { continue; } else { goto label; } }
		else { valueindex++; if (valueindex == 25) { filein.get(character); if (filein.peek() == ' ') { filein.get(character); } return true; } else { if (filein.peek() == ' ') { filein.get(character); continue; } } }
	}
	return false;
}

int main() {
	std::ifstream filein("input.data");
	numbers.push_back(0);
	char character;
	while (filein.get(character)) {
		if (character >= ASCII_NUM_START && character <= ASCII_NUM_END) { numbers[numbers.size() - 1] = 10 * numbers[numbers.size() - 1] + (character - ASCII_NUM_START); }
		else if (character == ',') { numbers.push_back(0); }
		else { filein.get(character); break; }
	}

	while (parseBoard(filein)) { }

	filein.close();

	for (int i = 0; i < numbers.size(); i++) {
		for (int j = 0; j < boards.size(); j++) {
			if (boards.size() == 1) {
				int result = boards[0].checkBoard(numbers[i]);
				if (result != -1) { std::cout << result << std::endl; return 0; }
				continue;
			}
			int result = boards[j].checkBoard(numbers[i]); 
			if (result != -1) { boards.erase(boards.begin() + j); i--; }
		}
	}
}
