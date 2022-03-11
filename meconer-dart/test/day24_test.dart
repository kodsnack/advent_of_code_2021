import 'package:advent_of_code/day24.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('Example 1, day24', () {
    String program = '''inp x
mul x -1''';
    ALU alu = ALU.fromInput(program);
    ALU.inputList = [5];
    alu.executeCode();
    expect(alu.x, -5);
  });

  test('Example 2, day24', () {
    String program = '''inp z
inp x
mul z 3
eql z x''';
    ALU alu = ALU.fromInput(program);
    ALU.inputList = [5, 15];
    alu.executeCode();
    expect(alu.z, 1);
    ALU.inputList = [5, 14];
    alu.executeCode();
    expect(alu.z, 0);
  });

  test('Example 3, day24', () {
    String program = '''inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2''';
    ALU alu = ALU.fromInput(program);
    ALU.inputList = [15];
    alu.executeCode();
    expect(alu.x, 1);
    expect(alu.y, 1);
    expect(alu.z, 1);
    expect(alu.w, 1);
  });


String puzzleProgram = '''inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 16
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -5
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -3
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -16
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 4
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 14
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 12
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -7
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 10
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -6
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y''';
  test('Example 4, day24', () {
    List<int> testNumber1 = [1,2,3,4,5,6,7,8,9];
    List<int> testNumber2 = [1,2,3,4,5,6,7,8,9];
    ALU alu = ALU.fromInput(puzzleProgram);
      ALU.inputList = List.generate(14, (index) => (index % 9 ) + 1 );
      alu.reset();
      alu.executeCode();
      alu.print();
      // Finished this day in python. See day24.py

  });



}

