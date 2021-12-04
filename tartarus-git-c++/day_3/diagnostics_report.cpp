#include <iostream>
#include <fstream>
#include <vector>

struct dianum {
	bool data[12];
};

int main() {
	std::vector<dianum> data;
	std::ifstream filein("input.data");
	int counter = 0;
	dianum tempdia;
	data.push_back(tempdia);
	while (true) {
		char buffer;
		if (!filein.get(buffer)) { break; }
		if (buffer == '0') {
			data[data.size() - 1].data[counter] = 0;
		} else if (buffer == '1') {
			data[data.size() - 1].data[counter] = 1;
		} else {
			data.push_back(tempdia);
			counter = 0;
			continue;
		}
		counter++;
	}
	filein.close();

	int gamma = 0;
	int onescounter = 0;
	for (int i = 0; i < 12; i++) {
		for (int j = 0; j < data.size(); j++) {
			if (data[j].data[i] == true) {
				onescounter++;
			}
		}
		if (onescounter > data.size() - onescounter) {
			gamma |= 0b100000000000 >> i;
		}
		onescounter = 0;
	}
	int epsilon = (~gamma) & 0b000000000000000000000000111111111111;
	std::cout << gamma * epsilon << std::endl;
}
