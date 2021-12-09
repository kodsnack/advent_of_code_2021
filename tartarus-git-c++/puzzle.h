#include <vector>

namespace puzzle {
	namespace input {
		inline std::vector<unsigned long long> parseList(std::istream& source) {
			std::vector<unsigned long long> result(1, 0);
			char character;
			while (source.get(character)) {
skipread:			switch (character) {
					case '0': result.back() = result.back() * 10; continue;
					case '1': result.back() = result.back() * 10 + 1; continue;
					case '2': result.back() = result.back() * 10 + 2; continue;
					case '3': result.back() = result.back() * 10 + 3; continue;
					case '4': result.back() = result.back() * 10 + 4; continue;
					case '5': result.back() = result.back() * 10 + 5; continue;
					case '6': result.back() = result.back() * 10 + 6; continue;
					case '7': result.back() = result.back() * 10 + 7; continue;
					case '8': result.back() = result.back() * 10 + 8; continue;
					case '9': result.back() = result.back() * 10 + 9; continue;
					case ',': result.push_back(0); continue;
					case '\n': if (source.get(character)) { result.push_back(0); goto skipread; } else { return result; }
					case ' ': continue;
				}
			}
			return result;
		}
	}
}
