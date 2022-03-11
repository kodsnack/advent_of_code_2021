import 'package:advent_of_code/day21.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  String testInput = '''Player 1 starting position: 4
Player 2 starting position: 8''';

  test('Get input', () {
    final start = GamePart1.fromInputString(testInput);
    expect(start.userPos1, 4);
    expect(start.userPos2, 8);
  });

  test('Deterministic die', () {
    final die = DeterministicDie();
    expect(die.getValue(), 1);
    expect(die.getValue(), 2);
    die.setValue(99);
    expect(die.getValue(), 99);
    expect(die.getValue(), 100);
    expect(die.getValue(), 1);
  });

  test('Play game', () {
    final game = GamePart1.fromInputString(testInput);
    expect(game.play(), 739785);
  });

  test('Big numbers', () {
    int testNum = 444356092776315;
    expect(testNum*10000, 4443560927763150000);
  });

  test('Play game part 2', () {
    final game = GamePart2.fromInputString(testInput);
    expect(game.play(), 444356092776315);

  });


}
