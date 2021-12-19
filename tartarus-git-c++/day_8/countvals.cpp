#include <iostream>
#include <fstream>

#include "../puzzle.h"

struct Line {
	std::vector<std::string> signals;
	std::vector<std::string> outputs;
};

std::vector<Line> displays;

std::string addSigs(const std::string& a, const std::string& b) {
	std::string result = b;
	for (int i = 0; i < a.size(); i++) {
		char character = a[i];
		bool found = false;
		for (int j = 0; j < b.size(); j++) { if (character == b[j]) { found = true; break; } }
		if (found) { continue; }
		result += character;
	}
	return result;
}

std::string subSigs(const std::string& a, const std::string& b) {
	std::string result;
	for (int i = 0; i < a.size(); i++) {
		char character = a[i];
		bool found = false;
		for (int j = 0; j < b.size(); j++) { if (character == b[j]) { found = true; break; } }
		if (found) { continue; }
		result += character;
	}
	return result;
}

bool sigContains(const std::string& b, const std::string& a) {
	unsigned int found = 0;
	for (int i = 0; i < a.size(); i++) {
		for (int j = 0; j < b.size(); j++) {
			if (a[i] == b[j]) { found++; }
		}
	}
	if (found == a.size()) { return true; }
	return false;
}

int main() {
	// Parse input.
	std::string input = puzzle::input::importFile("input.data");
	std::vector<std::string> lines = puzzle::string::split(input, '\n');
	if (lines.back().size() == 0) { lines.erase(lines.end()); }
	for (size_t i = 0; i < lines.size(); i++) {
		std::vector<std::string> parts = puzzle::string::split(lines[i], " | ");
		std::vector<std::string> signals = puzzle::string::split(parts[0], ' ');
		std::vector<std::string> outputs = puzzle::string::split(parts[1], ' ');
		displays.push_back({ signals, outputs });
	}

	// Working with input.
	unsigned long long totalNum = 0;
	for (int i = 0; i < displays.size(); i++) {
		unsigned int num = 0;
		std::vector<std::string>& outputs = displays[i].outputs;
		for (int j = 0; j < outputs.size(); j++) {
			bool thing = false;
			switch (outputs[j].size()) {
				case 2:
					num = num * 10 + 1;
					continue;
				case 4:
					num = num * 10 + 4;
					continue;
				case 3:
					num = num * 10 + 7;
					continue;
				case 7:
					num = num * 10 + 8;
					continue;
				case 6:
					thing = true;
				case 5:
					std::vector<std::string>& signals = displays[i].signals;
					std::string one;
					std::string seven;
					std::string four;
					std::string eight;
					for (int k = 0; k < signals.size(); k++) {
						switch (signals[k].size()) {
							case 2: one = signals[k]; continue;
							case 3: seven = signals[k]; continue;
							case 4: four = signals[k]; continue;
							case 7: eight = signals[k]; continue;
						}
					}
					if (thing) {
						if (!sigContains(outputs[j], one)) { num = num * 10 + 6; }
						else if (sigContains(outputs[j], four)) { num = num * 10 + 9; }
						else { num *= 10; }
						continue;
					}
					if (sigContains(outputs[j], subSigs(eight, addSigs(subSigs(seven, one), four))))
					{ num = num * 10 + 2; }
					else if (sigContains(outputs[j], one)) { num = num * 10 + 3; }
					else { num = num * 10 + 5; }
					continue;
			}
		}
		std::cout << num << std::endl;
		totalNum += num;
	}

	std::cout << totalNum << std::endl;
}
