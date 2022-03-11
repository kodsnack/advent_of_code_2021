import 'package:flutter/material.dart';

class Day24 extends StatelessWidget {
  const Day24({Key? key}) : super(key: key);
  static const String routeName = 'day24';
  static const String dayTitle = 'Day 24: Trench Map';

  @override
  Widget build(BuildContext context) {
    final resultPart1 = doPart1();
    final resultPart2 = doPart2();
    return Scaffold(
      appBar: AppBar(
        title: const Text(dayTitle),
      ),
      body: Center(
        child: Column(
          children: [
            const SizedBox(
              height: 200,
            ),
            SelectableText('Svar dag 24 del 1: $resultPart1'),
            SelectableText('Svar dag 24 del 2 : $resultPart2'),
          ],
        ),
      ),
    );
  }

  int doPart1() {
    final alu = getInput();
    ALU.inputList = [];
    alu.executeCode();
    return 0;
  }

  int doPart2() {

    return 0;
  }

  ALU getInput() {
    ALU alu = ALU.fromInput(inputText);
    return alu;
  }
}

class ALU {
  int x = 0, y = 0, z = 0, w = 0;
  static List<int> inputList = [];
  List<ALUInstr> code = [];

  ALU.fromInput(String inputText) {
    for ( final codeLine in inputText.split('\n')) {
      List<String> splitLine = codeLine.trim().split(' ');
      String instr = splitLine[0];
      List<String> args = splitLine.sublist(1);
      ALUInstr aluInstr = ALUInstr(instr, args);
      code.add(aluInstr);
    }
  }
  executeCode() {
    for ( final instr in code) {
      instr.execute(this);
    }
  }

  void print() {
    debugPrint('x : $x , y: $y , z : $z , w : $w');
  }

  void reset() {
    x = 0;
    y = 0;
    z = 0;
    w = 0;
  }
}

enum instr {inp, add, mul, div, mod, eql, inv} // inv is an invalid instruction and should not happen

abstract class ALUInstr {
  void execute(ALU alu);

  factory ALUInstr(String instr, List<String> args) {
    switch (instr) {
      case 'inp' : return Inp(args[0]);
      case 'add' : return Add(args[0],args[1]);
      case 'mul' : return Mul(args[0],args[1]);
      case 'div' : return Div(args[0],args[1]);
      case 'mod' : return Mod(args[0],args[1]);
      case 'eql' : return Eql(args[0],args[1]);
      default : throw('Instr error');
    }
  }

}

int getValue(String arg, ALU alu) {
  try {
    return int.parse(arg);
  } catch (ex) {
    switch (arg) {
      case 'x' : return alu.x;
      case 'y' : return alu.y;
      case 'z' : return alu.z;
      case 'w' : return alu.w;
    }
  }
  return 0;
}

class Inp implements ALUInstr {
  late String arg;

  Inp(this.arg);

  @override
  void execute(ALU alu) {
    int inputDigit = ALU.inputList[0];
    ALU.inputList = ALU.inputList.sublist(1);
    switch (arg) {
      case 'x' : {
        alu.x = inputDigit;
        break;
      }
      case 'y' : {
        alu.y = inputDigit;
        break;
      }
      case 'z' : {
        alu.z = inputDigit;
        break;
      }
      case 'w' : {
        alu.w = inputDigit;
        break;
      }
    }
  }
}

class Add implements ALUInstr {
  late String arg1;
  late String arg2;

  Add(this.arg1, this.arg2);

  @override
  void execute(ALU alu) {
    int arg2Value = getValue(arg2,alu);
    switch (arg1) {
      case 'x' : {
        alu.x += arg2Value;
        break;
      }
      case 'y' : {
        alu.y += arg2Value;
        break;
      }
      case 'z' : {
        alu.z += arg2Value;
        break;
      }
      case 'w' : {
        alu.w += arg2Value;
        break;
      }
    }
  }

}

class Mul implements ALUInstr {
  late String arg1;
  late String arg2;

  Mul(this.arg1, this.arg2);

  @override
  void execute(ALU alu) {
    int arg2Value = getValue(arg2,alu);
    switch (arg1) {
      case 'x' : {
        alu.x *= arg2Value;
        break;
      }
      case 'y' : {
        alu.y *= arg2Value;
        break;
      }
      case 'z' : {
        alu.z *= arg2Value;
        break;
      }
      case 'w' : {
        alu.w *= arg2Value;
        break;
      }
    }
  }
}

class Div implements ALUInstr {
  late String arg1;
  late String arg2;

  Div(this.arg1, this.arg2);

  @override
  void execute(ALU alu) {
    int arg2Value = getValue(arg2,alu);
    switch (arg1) {
      case 'x' : {
        int value = (alu.x / arg2Value).floor();
        alu.x = value;
        break;
      }
      case 'y' : {
        int value = (alu.y / arg2Value).floor();
        alu.y = value;
        break;
      }
      case 'z' : {
        int value = (alu.z / arg2Value).floor();
        alu.z = value;
        break;
      }
      case 'w' : {
        int value = (alu.w / arg2Value).floor();
        alu.w = value;
        break;
      }
    }
  }
}

class Mod implements ALUInstr {
  late String arg1;
  late String arg2;

  Mod(this.arg1, this.arg2);

  @override
  void execute(ALU alu) {
    int arg2Value = getValue(arg2,alu);
    switch (arg1) {
      case 'x' : {
        alu.x = alu.x % arg2Value;
        break;
      }
      case 'y' : {
        alu.y = alu.y % arg2Value;
        break;
      }
      case 'z' : {
        alu.z = alu.z % arg2Value;
        break;
      }
      case 'w' : {
        alu.w = alu.w % arg2Value;
        break;
      }
    }
  }
}

class Eql implements ALUInstr {
  late String arg1;
  late String arg2;

  Eql(this.arg1, this.arg2);

  @override
  void execute(ALU alu) {
    int arg2Value = getValue(arg2,alu);
    switch (arg1) {
      case 'x' : {
        alu.x = alu.x == arg2Value ? 1 : 0;
        break;
      }
      case 'y' : {
        alu.y = alu.y == arg2Value ? 1 : 0;
        break;
      }
      case 'z' : {
        alu.z = alu.z == arg2Value ? 1 : 0;
        break;
      }
      case 'w' : {
        alu.w = alu.w == arg2Value ? 1 : 0;
        break;
      }
    }
  }
}



String inputText = '''inp w
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
