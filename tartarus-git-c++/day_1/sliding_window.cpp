#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>

int main() {
	std::vector<std::string> data;
	std::ifstream filein("input.data");
	std::string line;
	while (std::getline(filein, line)) {
		data.push_back(line);
	}
	filein.close();
	int prevSlidingWindow = atoi(data[0].c_str());
	unsigned int increaseAmount = 0;
	for (int i = 1; i < data.size(); i++) {
		int value;
		if (i == data.size() - 2) {
			value = atoi(data[i].c_str()) + atoi(data[i + 1].c_str());
		} else if (i == data.size() - 1) {
			value = atoi(data[i].c_str());
		} else {
			value = atoi(data[i].c_str()) + atoi(data[i + 1].c_str()) + atoi(data[i + 2].c_str());
		}
		if (value > prevSlidingWindow) { increaseAmount++; }
		prevSlidingWindow = value;
	}
	std::cout << increaseAmount << std::endl;
}
