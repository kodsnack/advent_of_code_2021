#include <utility>

#include <vector>
#include <string>

#include <iostream>
#include <fstream>
#include <sstream>

#define ASCII_NUM_BEGIN 48
#define ASCII_NUM_END 57

#define INVALID_INPUT_CHAR 255

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

		inline std::string importFile(const char* filename) {
			std::ifstream input(filename);
			std::ostringstream stringStream;
			stringStream << input.rdbuf();
			input.close();
			return stringStream.str();
		}

	}

	namespace string {
		inline std::vector<std::string> split(const std::string& string, char delimiter) {
			std::vector<std::string> result;
			size_t sectionStart = 0;
			for (size_t i = 0; i < string.length(); ) {
				if (string[i] == delimiter) { result.push_back(string.substr(sectionStart, i - sectionStart)); sectionStart = ++i; continue; }
				i++;
			}
			result.push_back(string.substr(sectionStart));
			return result;
		}

		inline std::vector<std::string> split(const std::string& string, const std::string& delimiter) {
			std::vector<std::string> result;
			size_t sectionStart = 0;
			while (true) {
				size_t delimIndex = string.find(delimiter, sectionStart);
				if (delimIndex == std::string::npos) { break; }
				result.push_back(string.substr(sectionStart, delimIndex - sectionStart));
				sectionStart = delimIndex + delimiter.size();
			}
			result.push_back(string.substr(sectionStart));
			return result;
		}

		inline std::vector<std::string> removeEmptyStrings(const std::vector<std::string>& strings) {
			std::vector<std::string> result;
			result.reserve(strings.size());
			for (size_t i = 0; i < strings.size(); i++) {
				if (strings[i].length() == 0) { continue; }
				result.push_back(strings[i]);
			}
			result.shrink_to_fit();
			return result;
		}

		bool conversionerr = false;					// Signals conversion error. When handling this, user manually sets it back to true.

		inline unsigned long long convertToUInt64(const std::string& string) {
			unsigned long long result = 0;
			for (size_t i = 0; i < string.length(); i++) {
				switch (string[i]) {
					case '0': result = result * 10; continue;
					case '1': result = result * 10 + 1; continue;
					case '2': result = result * 10 + 2; continue;
					case '3': result = result * 10 + 3; continue;
					case '4': result = result * 10 + 4; continue;
					case '5': result = result * 10 + 5; continue;
					case '6': result = result * 10 + 6; continue;
					case '7': result = result * 10 + 7; continue;
					case '8': result = result * 10 + 8; continue;
					case '9': result = result * 10 + 9; continue;
					default: conversionerr = true; return 0;
				}
			}
			return result;
		}

		inline char convertToByte(char character) {
			if (character >= ASCII_NUM_BEGIN && character <= ASCII_NUM_END) { return character - ASCII_NUM_BEGIN; }
			return INVALID_INPUT_CHAR;
		}
	}

	namespace data {

		template <typename T>
		class Matrix {
		private:
			size_t heightInner;

			void copy(Matrix& other) {
				heightInner = other.heightInner;
				xIndexReturn.data = (T*)new char[width * height * sizeof(T)];
				for (int i = 0; i < xIndexReturn.width * heightInner; i++) { xIndexReturn.data[i] = other.xIndexReturn.data[i]; }
				xIndexReturn.width = other.xIndexReturn.width;
			}
			
			void move(Matrix&& other) {
				heightInner = other.heightInner;
				xIndexReturn.data = other.xIndexReturn.data;
				other.xIndexReturn.data = nullptr;
				xIndexReturn.width = other.xIndexReturn.width;
			}

		public:
			// NOTE: The following note was written when I was still initializing "data" in the constructor of Matrix because it's constructor had params.
			// NOTE: This "data" member variable would get default initialized if it weren't direct initialized by me in the constructor here.
			// That is incredibly stupid and a really dumb feature of C++.
			// How do you avoid that if you don't want to waste processing power on initializing things that don't matter at the moment?
			// You define a default constructor in the data class yourself, which doesn't do anything, allowing the compiler to not do anything at all
			// and also optimize the whole mess out. MatrixData() = default works fine for this.
			// This whole problem doesn't apply if your only types are POD types, which, when getting default initialized, just don't do anything and are
			// left in an indeterminate state.

			// ANOTHER NOTE:
			// Definition of a POD-type:
			// Kind of complicated in modern C++ (like practically everything is), but essentially this:
			// 1. Only contains POD member variables.
			// 2. Doesn't contain constructors or destructors (at least non-trivial ones that is)

			class MatrixColumn {
			private:
				friend class Matrix;		// Gives outer class the ability to access private and protected data in this class.

				T* data;
				size_t width;
				size_t xIndex;

				MatrixColumn() = default;		// This is sort of a POD type because this is trivially constructable. At least I think that's why.
				MatrixColumn(size_t width) : width(width) { }
			public:
				T& operator[](size_t yIndex) const { return data[yIndex * width + xIndex]; }
			} xIndexReturn;

			Matrix() = default;	// NOTE: Doesn't do anything in this case because all member variables are POD-types (almost, triv. ctor = most important)

			// "(T*) new char" is necessary to avoid new calling the constructor of whatever type is being allocated.
			Matrix(size_t width, size_t height) : heightInner(height), xIndexReturn(width) { xIndexReturn.data = (T*)new char[width * height * sizeof(T)]; }
			// NOTE: The stuff after the ":" is the initializer list. Initializer lists are important for this reason:
			// 1. First of all, if you're initializing POD members, then it makes no difference if you do it in init list or in body of ctor.
			// 	Reason: Member vars get initialized before ctor body is executed, which doesn't have any effect on POD's, so constructing them in body
			// 	is fine.
			// 2. This is the important part: If the member var is not a POD, then it should be in init list.
			// 	Reason: As already said, the member gets constructed with default constructor before body gets called.
			// 	If you construct in body, program first default constructs in front of body, only for you to construct again in the body.
			// 	Since theoretically, programs could rely on this behaviour, you cannot at all count on this being optimized out.
			// 	As stated above, members get initialized even without you touching them in init list or body, so this default construction problem
			// 	always exists for non-POD's. Again, this is avoidable by just initializing them in init list, so the compiler knows not to default
			// 	construct them and instead does what you want it to.

			Matrix(Matrix& other) { copy(other); }
			Matrix& operator=(Matrix& other) { copy(other); return *this; }


			Matrix(Matrix&& other) { move(std::move(other)); }
			Matrix& operator=(Matrix&& other) { move(std::move(other)); return *this; }

			T* data() const { return xIndexReturn.data; }
			size_t width() const { return xIndexReturn.width; }
			size_t height() const { return heightInner; }

			// NOTE: This const is good because const-correctness, but also necessary cuz or else you can't call this function on a const instance of class.
			MatrixColumn& operator[](size_t xIndex) { xIndexReturn.xIndex = xIndex; return xIndexReturn; }

			bool contains(size_t x, size_t y) { return x < xIndexReturn.width && x >= 0 && y < heightInner && y >= 0; }

			// Note: This has nothing to do with codebase, putting it in anyway:
			// In the past, you've cached referenced parameters because you assumed the compiler was using pointers behind the scenes.
			// The is valid thinking, but after asking on stackoverflow and understanding a very little amount of assembly on compiler explorer,
			// I've come to the conclusion, that you should definitely let the compiler handle this 100% of the time.
			// The compiler will either use the variables that are already on the stack, preventing the need to copy variables or pointers into params
			// in the first place, or it will make copies of the variables if you read from them a bunch and don't write a bunch, or etc...
			// The latter example I gave actually probably doesn't happen all too often (this is the same mechanic as your caching stuff), because of the
			// following:
			//
			// This is super important in this whole dilemma:
			//
			// This whole time, you've thought that dereferencing was a per operation cost. That every assignment became double as expensive or at least had
			// some amount of expense added onto it.
			// This is wrong.
			// Because of the way assembly and machine code works, the address to a spot in memory is stored in a register and given to an instruction to
			// add/sub/etc... with, that much is clear. A full dereference would be putting a constant address offset into a register, loading a pointer
			// from that address into another register, using that pointer to load a value from another address.
			// The thing with that is, that the address/pointer that you got out of the first load
			// can just be kept in the register (because there are a couple to choose from, and you might not be using all of them) and used to get the
			// actual value over and over and over again.
			// Bottom line is: Often times, the first dereference is costly, but every dereference of the same variable in the same scope after that is free.
			// Obviously, if you do use all the registers, this whole thing becomse a balancing act, which is one of the reasons all of this is best left
			// to the compiler.
			//
			// In conclusion, it is safe to use reference params as if they were values when you need to, because the compiler has your back and you'll be ok.
			
			~Matrix() { delete[] xIndexReturn.data; }
			
			// NOTE: This has nothing to do with the codebase, but I'm putting it here so I don't forget it:
			// The :: operator in front of a variable (or function or something else as well probably) but without a namespace in front of 
			// it finds that variable in global scope. Clarification: Doesn't hop one scope up, goes all the way up to global and finds the variable.
		};
	}
}
