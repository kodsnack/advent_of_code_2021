#include "../puzzle.h"

#include <iostream>
#include <bits/stdc++.h>

unsigned long long a = 0;

unsigned int parse(char type, std::string& string) {
lat:	if (string[0] == '(' || string[0] == '[' || string[0] == '{' || string[0] == '<') { if (unsigned int t = parse(string[0], string = string.substr(1))) { return t; } goto lat; }
	if (string[0] == type + 2 || string[0] == type + 1) { string = string.substr(1); return 0; }
	if (string[0] == ')') { return 3; } if (string[0] == ']') { return 57; } if (string[0] == '}') { return 1197; } if (string[0] == '>') { return 25137; }
	if (type == 'n') { return 0; } a *= 5; if (type == '(') { a += 1; } if (type == '[') { a += 2; } if (type == '{') { a += 3; } if (type == '<') { a += 4; } return 0;
}

int main() {
	std::vector<std::string> input = puzzle::string::removeEmptyStrings(puzzle::string::split(puzzle::input::importFile("input.data"), '\n'));
	unsigned long long sum = 0;
	std::vector<unsigned long long> autocompleteScores;
	// NOTE-TO-SELF: 0 values of basic types map to false, other values of basic types map to true. That means casting to bool (in if statement for example) isn't just bit redefinition. Logic is involved.
	for (int i = 0; i < input.size(); i++) { sum += parse('n', input[i]); if (a) { autocompleteScores.push_back(a); a = 0; } }
	std::cout << "Sum for part 1: " << sum << std::endl;
	sort(autocompleteScores.begin(), autocompleteScores.end()); std::cout << "Median for part 2: " << autocompleteScores[autocompleteScores.size() / 2] << std::endl;
}
