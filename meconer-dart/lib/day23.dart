import 'package:flutter/material.dart';

import 'models/amphipod_board.dart';
import 'models/amphipod_board2.dart';

class Day23 extends StatelessWidget {
  const Day23({Key? key}) : super(key: key);
  static const String routeName = 'day23';
  static const String dayTitle = 'Day 23: Amphipod ';

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
            SelectableText('Svar dag 23 del 1: $resultPart1'),
            SelectableText('Svar dag 23 del 2 : $resultPart2'),
          ],
        ),
      ),
    );
  }

  int doPart1() {
    final lines = getInput(example: false);
    AmphipodBoard board = AmphipodBoard.fromInput(lines);
    return board.findMovesToTargetWithLeastEnergy();
  }

  int doPart2() {
    final lines = getInput(example: false);
    AmphipodBoard2 board = AmphipodBoard2.fromInput(lines);
    return board.findMovesToTargetWithLeastEnergy();
  }

  List<String> getInput({required bool example}) {
    String input = example ? exampleInputText : inputText;
    return input.split('\n');
  }
}

abstract class Amphipod {
  int stepEnergy = 0;
  int home = 0;
  late List<int> homePositions;
  String name = '.';
  bool isAlreadyHome = false;
  static Amphipod? fromName(String name) {
    if (name == 'A') return Amber();
    if (name == 'B') return Bronze();
    if (name == 'C') return Copper();
    if (name == 'D') return Desert();
    return null;
  }

  String getName() {
    return name;
  }

  bool isInCorrectHome(int posInBoard) {
    return false;
  }
}

class Amber extends Amphipod {
  Amber() {
    stepEnergy = 1;
    homePositions = [11, 15];
    home = 0;
    name = 'A';
  }

  @override
  bool isInCorrectHome(int posInBoard) {
    return homePositions.contains(posInBoard);
  }
}

class Bronze extends Amphipod {
  Bronze() {
    stepEnergy = 10;
    homePositions = [12, 16];
    home = 1;
    name = 'B';
  }

  @override
  bool isInCorrectHome(int posInBoard) {
    return homePositions.contains(posInBoard);
  }
}

class Copper extends Amphipod {
  Copper() {
    stepEnergy = 100;
    homePositions = [13, 17];
    home = 2;
    name = 'C';
  }

  @override
  bool isInCorrectHome(int posInBoard) {
    return homePositions.contains(posInBoard);
  }
}

class Desert extends Amphipod {
  Desert() {
    stepEnergy = 1000;
    homePositions = [14, 18];
    home = 3;
    name = 'D';
  }

  @override
  bool isInCorrectHome(int posInBoard) {
    return homePositions.contains(posInBoard);
  }
}

String exampleInputText = '''#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########''';

String inputText = '''#############
#...........#
###C#A#B#C###
  #D#D#B#A#
  #########''';

String inputTextPart2 = '''#############
#...........#
###C#A#B#C###
  #D#C#B#A#
  #D#B#A#C#
  #D#D#B#A#
  #########''';

