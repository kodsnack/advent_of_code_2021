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

	int oxy = 0;
	{
	std::vector<dianum> selected = data;
	int onecount = 0;
	for (int round = 0; round < 12; round++) {
		for (int i = 0; i < selected.size(); i++) {
			if (selected[i].data[round] == true) { onecount++; }
		}
		bool mask = false;
		if (onecount >= selected.size() - onecount) { mask = true; }
		for (int i = 0; i < selected.size(); i++) {
			if (selected[i].data[round] != mask) { selected.erase(selected.begin() + i); i--; }
		}
		onecount = 0;
		if (selected.size() == 1) {
			break;
		}
	}
	if (selected.size() == 1) {
		for (int i = 0; i < 12; i++) {
			if (selected[0].data[i]) { oxy |= 0b100000000000 >> i; };
		}
		std::cout << oxy << std::endl;
	}
	else { std::cout << "couldn't find a single value for oxy" << std::endl; }
	}

	{
	std::vector<dianum> selected = data;
	int onecount = 0;
	for (int round = 0; round < 12; round++) {
		for (int i = 0; i < selected.size(); i++) {
			if (selected[i].data[round] == true) { onecount++; }
		}
		bool mask = true;
		if (onecount >= selected.size() - onecount) { mask = false; }
		for (int i = 0; i < selected.size(); i++) {
			if (selected[i].data[round] != mask) { selected.erase(selected.begin() + i); i--; }
		}
		onecount = 0;
		if (selected.size() == 1) {
			break;
		}
	}
	if (selected.size() == 1) {
		int co = 0;
		for (int i = 0; i < 12; i++) {
			if (selected[0].data[i]) { co |= 0b100000000000 >> i; };
		}
		std::cout << co << std::endl;
		std::cout << "final answer: " << co * oxy << std::endl;
	}
	else { std::cout << "couldn't find a single value for co2" << std::endl; }
	}

}
