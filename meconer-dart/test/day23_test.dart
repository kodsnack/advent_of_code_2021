import 'package:advent_of_code/models/amphipod_board.dart';
import 'package:advent_of_code/models/amphipod_board2.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  String exampleInputText = '''#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########''';
  test('Input', () {
    AmphipodBoard board = AmphipodBoard.fromInput(exampleInputText.split('\n'));
    board.print();
    expect(board.getState(), '...........BCBDADCA');

  });

  test('Possible moves', () {
    String input = '''#############
#.B.........#
###A#.#C#D###
  #A#C#D#B#
  #########''';
    AmphipodBoard board = AmphipodBoard.fromInput(input.split('\n'));
    board.print();
    final moves = board.getPossibleMoves();
    for ( final move in moves) {
      AmphipodBoard.fromState(move.state).print();
    }
    expect(moves.length, 12);
  });

  test('Dijkstra', () {
    String inputText = '''#############
#...........#
###C#A#B#C###
  #D#D#B#A#
  #########''';
    AmphipodBoard board = AmphipodBoard.fromInput(inputText.split('\n'));
    board.print();
    var energy = board.findMovesToTargetWithLeastEnergy();
    expect(energy, 18300);
  });

  test('Input part 2', () {
    String inputText = '''#############
    #...........#
    ###B#C#B#D###
    #D#C#B#A#
    #D#B#A#C#
    #A#D#C#A#
    #########''';
    AmphipodBoard2 board = AmphipodBoard2.fromInput(inputText.split('\n'));
    board.print();
    expect(board.getState(), '...........BCBDDCBADBACADCA');

  });

  test('Possible moves part 2', () {
    String inputText = '''#############
    #.B.........#
    ###B#C#.#D###
    #D#C#B#A#
    #D#B#A#C#
    #A#D#C#A#
    #########''';
    AmphipodBoard2 board = AmphipodBoard2.fromInput(inputText.split('\n'));
    board.print();
    final moves = board.getPossibleMoves();
    for ( final move in moves) {
      AmphipodBoard2.fromState(move.state).print();
      debugPrint('Energy : ${move.energy}');
    }
    expect(moves.length, 20);
  });

  test('Dijkstra part 2', () {
    String inputText = '''#############
    #...........#
    ###B#C#B#D###
    #D#C#B#A#
    #D#B#A#C#
    #A#D#C#A#
    #########''';
    AmphipodBoard2 board = AmphipodBoard2.fromInput(inputText.split('\n'));
    board.print();
    var energy = board.findMovesToTargetWithLeastEnergy();
    expect(energy, 44169);
  });


  test('Dijkstra part 2 with real input', () {
    String inputText = '''#############
#...........#
###C#A#B#C###
  #D#C#B#A#
  #D#B#A#C#
  #D#D#B#A#
  #########''';

    AmphipodBoard2 board = AmphipodBoard2.fromInput(inputText.split('\n'));
    board.print();
    var energy = board.findMovesToTargetWithLeastEnergy();
    expect(energy, 50190);
  });

}
