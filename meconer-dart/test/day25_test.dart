import 'package:advent_of_code/day25.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  String example3 = '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>''';

  String example1 = '''..........
.>v....v..
.......>..
..........''';

  String example2 = '''...>...
.......
......>
v.....>
......>
.......
..vvv..''';

  test('Example 1, day24', () {
    final grid = CucumberGrid.fromInput(inputText.split('\n'));
    //grid.gridPrint();
    int stepCounter = 0 ;
    bool finished = false;
    while (!finished) {
      finished = !grid.doStep();
      stepCounter++;
      //grid.gridPrint();
    }
    debugPrint('Count : $stepCounter');
    expect(stepCounter, 498);
  });

}

