import 'package:flutter/material.dart';

class Day25 extends StatelessWidget {
  const Day25({Key? key}) : super(key: key);
  static const String routeName = 'day25';
  static const String dayTitle = 'Day 25: Sea Cucumber ';

  @override
  Widget build(BuildContext context) {
    //final resultPart1 = doPart1();
    final resultPart2 = doPart2();
    return Scaffold(
      appBar: AppBar(
        title: const Text(dayTitle),
      ),
      body: const Center(
        child: CucumberGridWidget()
      ),
    );
  }

  int doPart1() {
    CucumberGrid grid = CucumberGrid.fromInput(inputText.split('\n'));
    grid.gridPrint();
    int stepCounter = 0 ;
    while (grid.doStep()) {
      stepCounter++;
      grid.gridPrint();
      print('Count : $stepCounter');
    }    return 0;
  }

  int doPart2() {
    return 0;
  }

}
class CucumberGridWidget extends StatefulWidget {
  const CucumberGridWidget({Key? key}) : super(key: key);

  @override
  _CucumberGridWidgetState createState() => _CucumberGridWidgetState();
}

class _CucumberGridWidgetState extends State<CucumberGridWidget> {
  CucumberGrid cucumberGrid = CucumberGrid.fromInput(inputText.split('\n'));
  @override
  Widget build(BuildContext context) {
    int width = cucumberGrid.grid[0].length;
    int height = cucumberGrid.grid.length;
    return GridView.builder(
      itemCount: height * width,
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: width,
      ),
      itemBuilder: (BuildContext context, int index) {
        int row = (index / width).floor();
        int col = index % width;
        String char = cucumberGrid.grid[ row ][ col ];
        return FittedBox( child:  Text( char));
      },
    );
  }
}



class CucumberGrid {
  late List<List<String>> grid;
  late int width;
  late int height;

  CucumberGrid.fromInput(List<String> lines) {
    grid = [];
    for ( final line in lines) {
      List<String> gridLine = [];
      for ( final char in line.trim().split('')) {
        gridLine.add(char);
      }
      grid.add(gridLine);
    }
    width = grid[0].length;
    height = grid.length;
  }

  gridPrint() {
    for ( final line in grid) {
      debugPrint( line.join());
    }
    debugPrint('----------------');
  }

  // Do 1 step. Return true if any cucumber moved
  bool doStep() {
    bool didMove = false;
    // From left to right, move east facing cucumbers 1 step east if the spot to
    // the right of them is empty
    for (final line in grid) {
      List<bool> isMovable = List.filled(width, false);
      for ( int col = 0 ; col < width; col++) {
        // If it is an east facing cucumber here
        if ( line[col] == '>') {
          // Check the spot to the right and set the movable flag
          // if it is empty there
          int colToTheRight = (col + 1 ) % width;
          if ( line[colToTheRight] == '.') {
            isMovable[col] = true;
          }
        }
      }
      // Now do the move
      for ( int col = 0 ; col < width; col++) {
        if ( isMovable[col] ) {
          line[col] = '.';
          int colToTheRight = (col + 1) % width;
          line[colToTheRight] = '>';
          didMove = true;
        }
      }
    }

    // From top to bottom, move south facing cucumbers 1 step south if the spot
    // below them is empty
    for ( int col = 0 ; col < width; col++) {
      List<bool> isMovable = List.filled(height, false);
      for (int row = 0 ; row < height; row++) {
        // If it is an east facing cucumber here
        if ( grid[row][col] == 'v') {
          // Move it south if it is empty there
          int rowBelow = (row + 1) % height;
          if ( grid[rowBelow][col] == '.') {
            isMovable[row] = true;
          }
        }
      }
      // Now do the move
      for ( int row = 0 ; row < height; row++) {
        if ( isMovable[row] ) {
          grid[row][col] = '.';
          int rowBelow = (row + 1) % height;
          grid[rowBelow][col] = 'v';
          didMove = true;
        }
      }
    }
    return didMove;
  }
}

String example3 = '''v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>''';

String inputText = '''v.....>..v...vv>v>.v>v.....>v.v>.>..v>>>.>>..vvv>.vvvvvvvv..vv....>..>>vv..........>>...v>.>...v>vvvv>>..v>vv..v>.v..>>...>v>....>>>......v
>>>>.v....v>.....>.v..>.v>v.v..>..>>>.v....v.v>.>>.v>..v>>v...v>..v..>.>v>>.>vv.>..v..vv.>v>v.>v..v.v>v>>vv..>..>.v.vv.>v.v..vvv..>...>>...
.>>>...v.>.vv.>.vv.v>v>.v..v>>.>..v>.>....>>...>v.....v..v>..v>...v>v.>.v..>vvv..>v..vvvvvv......>>v.v.v.>..>.v...>v..vv.v.v>.v...>vv.>....
>>>vv.v.>...v.....>>v..>>vv..vvv.v..>v>.>.>>..vv>..>.v>v.v.v>.v.vv>>v....>.>.v>>.>vvv.>>..vvvv>v.....>.v...>.>vv.v.>>.>...v.vv.>.vvv.v>>...
.>>v.v>....>vv.>v>.v>...>>>.v>>.>vv.>>....vv....>v...>..>..>.v..>.>.>>vv>>..v>...v>>v.v>.v.vvv..>..v.>v.>>>>...v...vv>.>vv...>>.>..>>>vv>.v
>....>>>>v>.>>v>.>>..v..v....v...>>v.vvv..>..>vvv.v.v.>....vv.v>v..v.vv.v..vv>..>>..>v.>.....v.>>v.>>.>......v.>.v>>>>>...vv...v.......v.>v
.>..>>>.>>>v...vvv.>..>.>v..v.v>..>.>v.>......v>vvv.>v>..>v.vv.v...v.v.vv...vv.>.>....>.vv...vvv>..v>vv>v.>...>..>.vv.....v........>v..v>.v
.>v>...>v.>..>v.>.>..>.>>.>.v...>.v.vv>....v.v..v...v>v.>vv>>.>>...>>vv>>v>v>...v.>...>>.v>>v>>....>>v.v..v.v..v...>....>..>>.vv..v>.v>v>..
.v....>v>.....>v.v>v.>...>.vv....v..>....>..>.>v..v.>.>>>.>v>>v...>..>....>>v.vv.v>.v.>.vv>..>...>v.v>.>.>..v.v.v>vv....>...v.v.v.v...>.>..
v>>..v>>...vvv..vv..>.>>>...>.v.>v>>...v.v>>vvv>>>....v...>v>.>...vv>>v..>.vvv..>.>.v.>v>v....v.v>>.v.>v.v.....>vv>.......v..v.v>.v..>v>.>.
....v.>.v..v.>>v.vv.>.v>vv.v.>>v.vv>v...>>>v>.>vvv>..v.>.v..>v..>>vv...vvvv..>>....v.vv>>>vv.>.v..>...>>v...>..>..v..v>vv.vv..v>vvv>v.v...>
.v>>v..>>v.>.v.>v.vv>...>...v>..v>vvv.vvv...v..>..>v>.>...v.>>.v>>vv.v...v..v.>v.v>.v>v.>.v..vvvv.>.>v>.......>>.>v>>>....>>v.>.v>vv..>>>.v
.v.>.>>v.>v>vv...>.....v>.vv.>>.v>v.vv...v>.>v..vvvvv......>v.v..>.......>v.>.....>v.v>.>v>.v>..v.>vv.v....>.vvv.>vv..vv.v>v>.......>>..vvv
vvvv>..>v.v......>vv.vv..>v.>...>.v.v.>.>>>..v>.>.vvv...v..v>.>v.>v>...>..>.>>.v.>v...>v>..>.v.>.>>>>>.v>.v.>v...v.>.vv>..v...vv.......>.>v
>>.>.>.v.>.vv>v.v>>v>>v.>>.>..v...>.>>..vv>.>>v>.>v..>.......v.....v....v.>>...>.vv.>>...vv>.>>.>v.>>vv>.v>v.>>.vvv>>>v>.>>..>>..v....v>>.>
v..>>.v...>..>....>v>.>>.......>..>v>..>..>vv.>vv.v......>v.v>v.......vv.>...v..v>>v..>.>>v...v>>.vv.>>..v.>>.......>.v...>....>>>..>v.....
...>.v..>>.>>>>>..vvv.v>vv>.>....v>vv>..vv.vv...>v>v...>>v..>...v..>vv.v.vv...v.>.>...>>....>.v...>vvvvv..v>.vv.>..v.>...v.>.v...v.>>.v.v>v
>>>..>.>v.vv>>...>>..>v>.>v>v.v..>...>>vv>..>v.>vv.>>.>.....v>>vv.>.>.............>>.vv..vv.>.>v>vv>...>...>.v>v.v>.>v.....>.>>>.>v>.>..vv.
.vv>....v.v.v...>v>.vv>v.....v.v>...>>>>>v>...v..>>v.>>>v.......>vv...v>..v..v.....v...>v....v.v>v>>.....v...v.>.>...>v..>>..>>.>.v...v>>>.
.v.vv..v>v>v>.v....>..v>>..>.v....v>vv.vv..>...v>..v....>..>>v........>.>...v..>....>vv..>.v..>>.>..v>.vv..v>.>.>.v.v.....v.>..>v..v>>.vv>v
>>v>.>>....v.v>.>>>.v...>>v.>.>.v.>...vv.>.......>>.v..>.>>>..v.v.v.......v.>.>>..vv.>...>>......v....v..v>...>v...>.v>.v..>.vv.....>>.vv>v
.vv.>.>>...v.v.vv>..>v>..>vvv>>>.vv...>>.vv.v.v>>.>>v.v.v..>..>v...vv..vv....>v>v..>vvv.....>v>v..>...>>v.>.>>>>..>.>>.v>...>...>..v..>..>.
.>>.v.v...>..>..>vv.v>v.>v>v.v.v>>..vvvvv...v.vvvvvv>>v........v.v..v>v.>>>.>v...v.>..>>v...v...>>.v....v...>.>....>v.v>>>.....>...v.v.vv..
>.vvv>v.v>..v>.>vv.........>.......>>.vv>v.>...v>>.v>.v.v.>.>......>........v.v..>.v>>>.v......>>.>..v>v..>.vv.....v>..v>vv>..>..v..>vv>>..
.v>..v..>.v....v>....>.vvv>.>.>v>vv>v>>..........vvvv>vvvv..v>vv......>>v..>>>v>>.>..>vvv..>..>>v>v.vv>>..>.>v.>>.vv>.>....vv.v...>....>v.v
>vvvv>>v.v..v.>>..v>...v.v.v>..>>..>..>.>>vv.v.v...vv>...v.v>v...v.>.>vv...v.>.v>..v>..v>>>.v>.vv>..v>>....>....>...v>.v......vv.v.>.>>>>v.
v..>......v.v>>.>>..v.v>v...>>.v...>....vv>....>.>.>>..v.vvv>>vvv.v>......v>>...vv>...v.>>vv...>v.>>vv.vv......>.v.>.v>>..>v.>>>..>v.v>.vv.
>..>v..v>vv>.v>>..vv.v>.>>..v.>vv.>v..>v>..>...>...v........v...>vv....>.>...>.>..v....v.v>.v.v....v.v>..v>>.>>.>..v>..>>vvv.>>..v..v.>v...
>.>.v>>....v>>v>.vv..v>.v>....vv>.......>v>..>v>>v.>vv.>v.v>>v.vv..>.v.>.>..v.>...>.v..>.v..>.>.>v.vv>..>.>>..v...>>...v..v>>>.>>.v>.>.>.v>
....v.v.>.>>.>.....v...v>>>.>v..v..v....>>>..vv>.>>>>>.......>...>...>..........>.v>...>...v.v....>.v>>>v.>..vv.....vv>v..>v.>v>>.v......v.
.>.v>>v>>v>>...>v..v.v>.>>.>v.>v.>.vv.v>>>>vvvv>.>>v..vv>>.vv.>>v..v.>>...>v>>>....v.v>v>v>>>........v.v>v>>>v....>...vv>>>>v>v.>>v>>vv....
>.>>..v..vv.>....>.v.>.v.v>>.>..vv..>.v...>.>vv...>...>....v.v...v>>.v.v>>..>...v...vv>>.>vvvv....>.....>......>.vv.>..>vv>>v>v....v......v
v..>v.vv.v.v>>v>..v..v>>...>>.vvv>.v..vv>.v>>.>..>v.v>.>.vv.v.>....v.>>.>>.v>v>.v..vv.v>.v...>...vv>v>v..>>.>.v..>.>v>...>...>vv.>..v..v>vv
>>.>.....>v..>vvvvv.>>..v..v>..>v...>.v..vv>>>......>...v..>v>..vvvvvv...vv>.>...vv>v..v..>.......>.>v.>...v.>>.v...>...>...>v...v.>vv..v.v
.>>v>...vv.>.v>.v.>v..>v..>v.>v>v.v.>.........v.>v..v.v.>..v>....v....>v.>>>..>>v>.v...vvv.>.....v.>>>>v>v>..>..v.vv>>..>>.....>v...v>.....
>.>.>v>>>vv>>...>...>>>vv......v...>.>vv.>>v>.v.vv...v.>.>..v....v.v.>v>.>....>>.v...>>.v..>.v...v.v>vv...v.vv...vv.........>....v.....v...
..>>.v...>..vvv.>....v>.>v.>>.>..>>.>.....vvv..>......>>>.>.....>.>>v...v..>.v.v.>.v>>..>>>....>...v>>vv>v..>vv>..vv>.>>>>.vv.v.>>>v...>>vv
.>vv>.v>.>.>.v>......>.v>v......>......>>v..>v..v.v...vvv>>....v...v>v.v>>v.>v.v.>>>>vv.vv....>.>.v>.vv.v..>.>v>>.vv.v>..>v>.....>..v.>.>v.
>v.v..>.>.vv>.v>v>....>..v....>.vvv..>>>>..>v..>>..v>...v>....>>.v..>v...>.>..v>..v.v.v>>.vv...>v.>...v.v..>v....v.v..vvv.>.v>v..>vv>......
...v.v.v..>..vv>v>v>>v..>>>>v.....v>v.>>...v..v..>vvv>v>v.>vv>..>vv...>.....>..vv..>>.....>.v.....>.v.>>..>..>.v..>v.v>>..>.>v>v>.v>.>>v.>v
vv>..>v.vv>>>v.....vv>...v>v>.>..>.v..v>v......>.>v.....v>.>.v.v..>>....vv>......>>v.>v.v..v..>v.v.>>.>vv....>.>>>.vv.v.vv>..>..v...>.vvv.v
vv>>>v..v.v..vv.>>>.>..v>vv..>v>..>vvv.v.v..v.>.>v.v.v.>.>v..v..>.>v..v.v.v>.v...>v.>.>..v..>..v..v.>vvv>>.v..v..>v..>.v...v.v.v.v>.>.v>.>.
.>>.>.v....>..v.v..>.v>.>>>.>v.>>v...v...>v>v.>..>.......>>..v..v>.>...vv.>...>>.>....>...>>..v....v>..>v.v>vv>.>.v>v.>.>......v..v.v>.vv>.
...>v.v>v.vv.>.>...v..v....>v.v>.v.>.>v>v>>.v..vv.>>.vvv.>>.vv>>>..>v.v.v..>.>>.....>>...>v.>vv.>>...>...>.....>.>>.>.....vv>.>v>v..>..>vv.
.....>..v...v.vv.....vv..>>vvv>.>..vv...>..>>..>..>.>..>......v.>.v.>.>.v>.>>v.....v.v...v..>.......>>v>>>...vv>v.....v..>v..>.>...>v...>>v
..v.vv...>.>>..>...>..>>>..v.vv.v>>vv>v.>.v...v....>>.>.>vv.v.vv>v..>..vv.>>>.........>..>.>v..v>.v>.v..>>v..vvv.vv...v>>vv..v.>..>v..v.v..
>.v>.>.>v.v..v>>.v.v..v>v>>v.v.>v>..>..>vv.vvv..v>>....v..v>>vv>......>...>>.v..v..>..v...>..>v..>v...v.v.v.>vv.vv.>>...>>..>....v>v>>>v..v
.>.>..v.>v.>....>....>>v...v>..>.>v.v>>>.>.>........>v.>v.>..>>...>.>..>..v>.>..v>..v>.vv.v...v.>v..>v.vv>..v>>v.v.>>v...v>v...>.v...vvv>..
..>>>.vvv.vv..vvvvvv.v.>v.v.>...vv....>v.v>>..v.>>.......>.v.>vvv..>v..>.v....>vv.>...>>...v....>.....>.v.>>>>>...>..>..>>v.vv.>vvv>vvv....
.v>v>>v.v.....>..>>..>>>>..v>...v..v>..>v.vv...v>...>...v>..v..>..v>.>v>....>>vv>vv.v..v>v...vv>v>v>>.v..>v.>>..>.v>>>v.v>v>..v....v...>>..
v>......v..v.>vv.vv>..vv...v...>v..v.>>vvv.v>...>.>...>>..v....v..v.>.>>v......v.v.vv.>...v.>>.>>......v..>v>>v>>...v>>......>..>..v..>...>
vv.>..>.v.>...>>>..>.v..vv>......>>..vvv..v.>.>.>.........>>....v....>v>>.....v.v.v.v..>v.....>......vv.v..>>>>>>..>..v..v>v>...>v>>.>....v
.>v.v>v>>v..v..v.v...v.v....v..vv>.v>.>.v.>>>>.v.>.vvvvvv>v>>......>vv.>>.........>.v.>.....>>..>.>.vv.v.>.>.....v.>>v.....v.v..>v>..v.vv..
>....>>>>v.v>.>..v>..v>vv.>>..>v>.>>..v>v.>..vvvvv....v>>..>.v>>.>.v.>v>...>.>.v>...v.....v...v.vv>v>..v.......>.>.v>>>...>........vv...>vv
v>v.vv.>>>v>.....v....>....>.......>..>...v.>v.v.v.....>v>>>...v.......>v...>>v.>v.v.v..v.>..>.>v..vv.v.v.>v..v...v..v>.vv>>..v...v.>.v..v.
v..v....>v.>.>...>..v.>v.vv.....>.v>....>..>>vv..v...>>..>.vv>v>.>v..>vv...v>vvv>v>.>v>v>>>.vv.v>>v.vv.>.v.>........>v......>.>.v..v>vv....
>vvv>..>..>.v>>v..........v>.>.>>.>.v>.....vv>...>...v..>v>.>v>>.vvvv.>>.v......v....v....vv..v..vvv.>...>...v>vv....>>>v>vv.v>>>.>.v.>>v.v
v..>vv>>vv.v.v..v.>>..vv.>>v.>v>v...v.>..>.>v......v....vvv.>..>....v..>..v>.>v..>.>v.>.......>.>v...vv>>.v....>.>v.>>>v.>v...>..v>v>..>>>v
vv.vv.v.vvvvv>...vv..........v>vv.v.v...>v.>>..>>vv>..vv>v.v.>.v..vv>>...vv.v.v.>.vv.>vv>.v>>.....v...>>.>v.....>..>>..>>..v...>vv>.v...v>>
.v.v..>v..>...v.>.v.....>>..>.>>vv>>>v>.......>.>>...>..>.>>..v...vvv.>..vv..>v>v..>>..>.....>..v..v....v>>v.v.>>>.v>.vv.v..v..>v.>.>>...>>
.>..v>>v....v.>v..>vv.v.>..>..>>v.v>>.....v.>>..>>.>..>>>>.v>vv..>.v.>.>...>>>.>......vv...v.v.v...v>.>.>.v..vv..v...>v.....>.v>...>..>..v.
.....vv>..v.vv>.>>>.....>.>v.......v>vvv..v.>>.v....v..v.>v.>v>.v>vvv...>>>>>>.vv.>.v.>...>v..v....>..>v.>>>vv.v>.>.>.vv>...>>v.>>.vv.>.>v.
..>>v...>..vvv>>.>v>vv....v..>v..v..>v>...>.v...>>.>>.vv...v>v.v..>.>>.v...>v....>>>>.v.v.vv.v.>>.vv...vv>.>.vv..>>.>.>vv.>..v>..>.>.v...v>
vv>>v>v.v>v>>v>v>>v>v..v....>..>.>.....v>>.>>v.v.>>>v>.vv.>vvvv>..>>>...>....v>..>vvv.>.vvv>>v.v>..>.v.v.>.v.v...vvvv.>>......>..>v.....>>v
>.v>.v>v..>.>..>.....>.>>.>.>..v.v..v.vvv>.>>.v..>.v.>.>v>v>.v>>>v.v...v>v..>..>>.v.v>.>.>..>.>v...>.v..v>v>v...v..>>...v.>>....v.>v.vvvv>.
..v..v>.v.>v..>..>.vv.v....v.v..v..>>.>>.v..v.vv>v.>.vv..v.>.v....v......vv....>>>v..v...v..v>>>.>...>>v.v>vv>vvvv>.vvvv.>v>..v.>>....>.vv>
v..vv.vv.v.>...>.v..>v.v.......>...>>.>.>..>>.>.>>.....v..vv>.v.>v..>...v>.v>.v>>v...vv>v..v...v.>.>...v...vv..v>v....>.>v>>>v..v>.>v>.>...
..>..vv..v..vvv>v>v..>>.>....vv>...v...v..>.v.v>......>>..v...vv>>...v>v.v...v....v>v>..>v>.......>>.>v..v.....vv.v..>.>..>v>.>.>.v>..>vv>.
v>>v.......>.vv....>>.....v>>v.....vv...>vv>vv>...v...v>>.>.v...v.v.....v>....v>.>.vv.vv...vv>>v..>v...>.v....v>v>..vv>..>....v>v>.v.v.>...
v.v.v>.>>.v>>vvv..v>>.>...>.....v.>.vv>v.vvv.>>>v.v...>..vv..>..>.>v.....>...>..v.....>....>.>>.>>v.v>...vv.....>.>.>v..v.>vv...v>>>>.>.v..
.vvv>>>>.v.v.vv.v.v.v.>....>v>....>.v>.v>...v.>.v.>..>.v..>>..v>.vv.v......v...v>>..vv>>.>.vvv>.>>..v.>>>..>.>>>.>>v...v.>.>..>>v>>>v>>.vv>
>.>v...v.>>v.>v..vv.>.>.vvv....>.v>v..>v.>..vv>.>v....>>.>>....v.v>>>.>vv>>.vv......>v...v.>.....>..>..>.>.v...>v...v...v...>v.v.vv.....>v.
...>.vvv>.v.v.v.>..>...>..>>>.>..>.>..>..v..>vv.v.v.>.....>.v>....>.>.>....>v.v>.>.>.v..>...>..>>..>>...>.v.v.>..>.>vv....>>>..>>.>.>..>...
>>......>vv....v.....>..>>.>...vvvvv>......vvv.v>.v>.>....>>v.>>vvv...vv.>...>>.v>..>........>>vv>v....>.>..v.>v.>..>......vvv>>......>>.v>
v.>....>.v.v>>..>.v.>>v>vv>>>>.v..>v>v>.>..>>.v>>.v.v..v>v.>v.v>vvvvv...>.v..v.v.....>.......v..vv...vv.........>..v....vvv...>..vv>.v.>>.v
....>v.>.....>....>v.>...v.>v.v>.v>.v.>.>v>>v>>>v..>>v..>v.>....v.>>>...vvv.>....v..>.>...>.v>...v>v.vvv.>v.v.v>>>>..>..vv.>..v.vv.v..v.v.>
v...v...vvv.>>>v.>....vv>..v..v.>v.>v..>.>v.v.....v>...>...vv>..>.v.v>>vvvv>.v>>>...v>.v>>...v>vv..vvv>.v........>v>.vvv.vvv...v>.v.....v.>
>....>v>>..v.v..vv>.v>.v...vvvvvv..v.>.>...vv..>>.vv.>..>v>v..>>...>....v>v.>.>>vv.vvv>v.v>>..vv.>..>...vvv....>..vvv..>v>v..>.v.>>vv.>vv>v
vvv>...vvvvv>>v....>..>.v>v.>.>..v.>v.v>...>>..>v>.>v>..vvv.....v>..>.>>vv.>>>>>....vv.>>v.v.v...v>>.v....v.>v...>..>..>.>.v.v>.>.>.>v..vvv
..>>>>>.v>v..>v.v>v>>>v..v>>.>vv...>.....v>>v....vvv..>...>.>.>>..>.v....v..v>v....>>vv..>v>>..>...>>..>.v.v.v>.v.>.vv>v.v.>......>>.v....v
.>v..>..v.v.>v.>.....>vv>..v>v.>.........v>.>v....>..>>..>>..>>.....>v>vv..>.....v.>...>.>>.>v....>>>.>....vv>.>>>>.>..>>.>v>>vv.vvvv>v.v.>
.v.>.>>.>.>v>v>v>vv>.vv>.>>v.vvv>v..>.>v>v.v..>..>.>>>>>..v..v.>.vv...>.vv..>>v>>v..>v>....>>....v>v.vv>>v.v.v..>..>v..vv.v.v>v>.>...>..>..
vv>...v>>.....>>>v..>..v.>v.>v.v>vv...>........v..vv.>..>>>>..>>v..>...>v.>>>>vv.>vv>....>.vv.>>.v....v.vv.v>.v>>.v...v.v>.>.....v>....v.>.
v..>>.v....v..>.v.v..vv..vv>>vvv.v..>>.>.v>.>v>...>.>>>>>vv>>...>v>.>>>v..vv>>vv.>v.v>.v...v.....v>>v..v..v.v>v>>....>.vvvv.>vv>>v>>>>>v...
v.>v.v..>v>..vv>....v.vvv.vv.v>.vvv.vv.v>..v.v.>>>>..>.>v...v.....>>..v..>..>vv.>..>v>.v>......>...v.vvv.....v..>.>v>.....>.>>..>>..>>.>vv.
.vv.>v....v>>v.>...>v..v>vv>.>.....>v>......v>..v.v>.vv>.v>.v.>.v..v.>...vv..v.v.>>v>vv>v..v.>.v.>>>>..>.>>..>......v.>...>v>.vv.>>.>..v>v>
vv>>>v..v..v..>.v.v>.>vv>v..v>>>>.>.v..>vv.>.....>v>vv.>vv.....vv.>.v...v.>>...>.v>v>..v...>v.v>>.>>.>v.v>>v..>.>>.>v.v>.>.>vv.>..v>>v>..>.
v.vvv>......v...>..>vv...>.>.>..>>....v>>..>.vv..>..v.v.v.>>.vv...>..v>.v....>v.v>.vv>v.>.>.v.>.>v.v.....v.v.v>.>..vvvv..>v.>v>.>...v>>>...
........>>v..v.v..>.>>.vv.>...>.v.>v...v....v.vv.>v>>.>.v...>>>>.>...v.>>...>>v.v.v>.v..>>vv...v.....>..v....>vv>.v>....v.>..v>...>..vvv>.v
vv.v...>......>.....vv>..vv...>.v>>>>.>v.v>..v.v..v>.>vv.>>.v.>..>>.......v..>>...v>>.>.>...v>>>.vv>..>.>.>v>..v>...v.v..v>.>......v>v..>vv
..v.>..>vvv........v..v.....v...>.v..>.v>>>.v...v..>v...>>>>...>....>v..>.>..v.v..>.v..>..>>.>>..v..>>v.>v..v.....vv.>>>.>....vv>.v.>v.....
v..v..v.>.>..>..vv>.>>.>>.v>...v...v>vv>>.vv.>....>.v.....v..>.vv.v..vvv.v>>v..v.vv..v....v.v..v>..vvvvv.v..>v>.v>v.>>v>..>v.vv.>>..>>.....
.>....>..v..v.v.>.>..v>.>>vv>vv...v>>...>v..v..vv.v>v>.>>>.v.>.>v>.vv.v...>>.vv.>..>.....v.>v>v...vv.....vvv>vvv>vvv..vv...v...>v.v.vvv..>v
>.vvv..>.>.>..v>v.>....>v.>>.>....>v>...v.>..>...>.v...>v..>....vv....vv..v.>..>.v.>..>v>...>>..v.>..>>..>v..vv>>>..v..v>......>>>v..v...>.
v>>..>>v..>....>vv.....v>.v>..>v>..>v..>...>..>v..v>.v>...>v.>.v.>.>..>v...v>vv>v..>>.>v...v>>v>v.v.>vv...>>v..v>.vv...v..v>.vvv>.vvv..v.v>
..>.....v>.v........v>....v.>>...>>.v>>>>>vvv......>>..v.>v>v.vv..>..>>.>.v>.vv.>...>v....v.....>>..v..v>.>v..>>......v.....>..v.v......>v.
>.>.>vv....v>....>....>v.v.>..>>........v.v...vv..v.>..vv.>......>.v.v.vv...>>>..v>v..v.v>.vv>>...>....v..v.>v.v>v..>>..vvv.vv...>.>.v..v.>
..>.>.>v.v.>vv.v>.v.>v.>>..>..>v>vv.v.vv>.>>>...>v......vvv.vv..v.v.v.v...>.>>v..v.v.v>.v.v....>>.v.v.>>v.v.>..>..>..v.>....>>v>..v.v.vv..v
..vvv..v>..vv>..>vv..>.>...v>.......v.>>..v.>>.>..v.>>>..>v..>.vv.>vv.v>v......v.v.....>..>.v....>.v....>v.v>..>>.>>>vv.>v.vv.>vv.v.>..>...
.>>vv>.........>.v>..>.>....vvvvv.v....v...v....>..>.v.v...vvv...v>v>.v.>v..>v>v..>.v..vv>...>vvv...v>..v....>vv.>.v.>.>v..>..vvv..vv...>.>
>.v>.v..vv>>.>...v>.>...vv.>.v.vvv>..>...>v..>.>>v.vv..v.v...>>...>.>v..v.>v.>.vv.>>v.v.vv.>v>.>>.....>.....>>>.>..>.>..>..>.>.>..v...v...>
vv..v.>>>..>>...>vv>.>>.>v>v...>.v>..>..>v.>.>.v>>..v>...v>..v>v....vv>....v>v.>.v.>..v....>v.>>v.......v.>>>..>..v.vv>>.>>>..>v>>v.v..v.>v
>.>..>...v.v>v.v..>.......>..>.vv>...>>vv..vv....>.....>....v.vv.>>>>v>>>.>vv...>>....>v...vv.v>.>.....vv...>>v.>v>>..v.vvv.vv.v...>.>>..v.
>>....v.v.v...v.v>.>v>...>.v>v.>..>v>>v.vv...>....>......>..>vv....v.v.>....v>>...v.v.v.>>..v...>....v>..>.v>v..vv.v.>..>>vvv....>>..>.>>>.
......v..>>>>>.>..v..>>>.....v.v..>..>v>...v.>..vv>>>>...v..v>...>.v>..>.vv....>>.>v....>...>.....v....vv...v..>.>v>.>>.>>.>>...v.>.>.v..>.
v>vv.v.v.v>.>v>v.>...v.>>..v.v>.>.>vv>>.v>.vv.v..vv..v.v.v>vvvv.>v>v..>v>vv>.>.v.>.>>.>v.>.v.>>>.>.v.......v>>v...>.v..vvvv.vvv>.v.v>>>>.v.
>v>....>>>.>v.>..>.v.>>..v....>....>...>..>>vv....vvv>v...vv>>.....>..vvv>.vv.....vv.v>>.v...>v.>v>.>..v.v.v>v>>.v>....>>v..v..vvvv..>>v..v
>v....vv.v.>.>..>v.vv....v>v...>v...>.v.>>....>.v>.>.v.>.v...>.>..vv.vv>...v.v>.....>...>>..>vvv>.v..>>vv>.>.>v.v>>vvv.>v.>.>>>>vv....vv>.>
.v>vv..>vv>vv.>.>..v..>...>.v>>v..v>>v..>......>..>..>>v>>.>.....v..vvv.....v...>>.....>>>>.>>...>>>..v.v....v.vv>>...>.>.>vv.>...>.>.>>v.>
..v.v>v..v>..>..v...v..v......>.>.>...>>.>v..v>..>v...v...>>v........>.v>..v.v.....>v....vv>>....vv..v>>.>.>.>>vv...>.v>.v....v..vv........
.v>>...>v..>v...>>.>....>>v>vv>v..v..v..>...>>vv...>..v>v..v>v.>v..>....>.v.>v..v>>>v.v.>>>v.v>v.v>..>>v>v....>v..>>.....v.v....v>v..>...>.
v.>.>.....v.v.>>v>>...vv.v.vvvv.>>....v..v.v>.>.v>.vv.>>v..>..>...vv>.>v>..v>.v.>v>v..v.v>v>vvv.>>.>.vv.vvv.v...v....v..v..>>....>vv...v.v.
.>..>>>..>..>>..v..vv>.>.v>.>v..>>>..v...>..v.v..>...v...v....>>.v......v..v..>>v.>vvv>..v.>..v...v..v..v..>>>.....>...v.v.>>....v.>v.>.>>v
v..v.>..vv....>v...vv..>..>>..vv>>v.v.vv>.>.v.v.v>.v.v>>v.v>..vv.v..v>>>>v.v>..vv....>>v....>.v..v.>>.>vv>.>v>...>>>vv.v..>v.v>.>........>.
v.>>>....v...v>..v.v.>.v...>.>.v>v.v.vvv.>v.>>.v>vv....v.v.v.>..vv>...>>..v...>.v>.>.>v.>>>>..>>>>>>v.v.v..>v.>>.v>.....>..v...v..>>...v>>.
.vvvv..v.>.>.>v>v.v>.>.v.vv>.>v.v.....>...>>vv.v..vv..>...>v...>vv.vv.v...v..vv>>..v>.>.>.v.>..>..>.>.>.....v..vv..>.....vvv>>....>v.....v.
v.>>.>..>.>v>>>vvv>.>.vvv>...v........>...vv..v..>>.v>.>.vv..>>vv>....>>vvvv..v.....>vv.v.>>v>>.>>v..>.>...v>...>.>v.v..>.v....>>....>>v..v
..vv.v.>v>v...>.vv.vvvv>....vv....>.>.vv>...>..>..>.>.>.....>v>.....>...>v..>v>>..>>>.....>......>.>v>>..v..v.vv.>>..>..>>vvv>>vvv>...>...v
>..v..>>>.>>v.>.v>>>>..>....vv>>...v>....>.v>v..>>.>..>v>.>>.v..vvv.>v...vvv>..>>v.v>>v.>v.>...>vv>..v.v>..>.>......>......>>..>>..>>...>v>
..>>....v.>>....v...>.v.v.>v..v....>.>.>.>>...v>..>.v.>.v>.vv>>>v.>.>>>vv..>>v>.vv.v>......vvv.....vv>.vv...>..v...>>.>>..v>.>>v>.v>>.vv>..
.v......vv.>.v..v..>........v>.>.v...v>vvv>.vv...>..>....v>.v..>v>.>>.>v...vv.>>......>vv..vv>.vvv>>>..>..>v.v..v.....>.....vv>.>vv....>>.v
..>>v>.vv>v.>....v>>>vvv>>vv.v.>..vv.>.v....v>>...v....>.>vv...>...v.v>..>.vv.>.v...>....v.v>>......vv.vv..>>vv>.....>v...>>...>..v.v.v.vv.
v..v.>.v.vv.>v.>...v>.........>>v.v.>>..........>vv.>>......>v.vv..>..v.v>v.>.v...>v.v...>.>...>>vv>.v..>vv.v>>..v.v...v...v.>.v.vvv>>.....
....>....v>.>.>v.>v..v.v>>v>>v..vvv...>.>..>vv>>>..v.v..v..v....>>.>........>.>>vvv..v>>..>.v>>v.>.v>>v.vv...>.>v....>v>..v.>vvv..v..>vv>.v
..>v.>..........v.>.v.>.>.>..v..v.>...>.v........vv.>vv..v>.>..>..>v...vv..>v>>...v>..v..v..>vvvv.>v....vv...>.>....v.>.>.>...>.v.>>.v.vv..
..v>vv..>.v.>.>vv>v..vv.>.vvvv..v>v..v>.v>v.....vvvv.v>.>.>v.>.>....>.>.v.>.v.v>>..v>v.>vvv..>>..>..>>..vv.v...>.v...>v..>.>>.v..v>...v>..>
>v.v.......v..>>v>v.>v.....>v.>.vv....>.v>>v...>v.v>>>.>v>>...>v.vv.vv.v>.vv>..v.vv>v.>..>.v.>........>.>....>.>.v...>...v>....v.v>>v>..>v.
v>vv.v>.v...>..>..>..v.>v>..>v.>..v>>v.>>.v.vvv...>.v>.....>.>>..v>v..>>v>.>..>..>...>vvv....>.>.vv>>>.v...v.v>.>>v>...>...>.>vv.vv>.v.>v.v
..>v..v>v.>>.vvv..v>>v..vv..v>vvv.>..>>>.v>.......>..vvv.>v...vvvv.v...>v>>>..>.v...>.>>v..v..>v.>......v....v>v>>>..v.v.......>.vv.v.v..>.
v...>>......v>>......>>v.....>....v.>v.>>v>>>>v>v..v>.v....>...vv..>>.v>v>..vv>.vvvv.>>.>>>v>.vv.>>.v.v......v>>v.v>.>...>.>..>.>>.vv......
>..v..>>>v>>.v.vv.....>>>..vv..>vv..v.v>..>v.>v..>v..v....>..>>>vv>>.v>>..>v...v....>>>vv.v.vvv.vv..>vv.>.vvv..>>>>.>>.>v.v>>>..>v..vv....v
.v..>v.>v..vvv.>.>v..>..>vv...v..>vvv...>v.v...>.v....>vv.v.v>v...v>>v.v.vvv..>.v>v>>.>..>>....>>.>..vvv.vv...v...v.v..v....v...v.vv>>vvv>>
..>.>.v.v.>v>.vv..v.v.>.vv..vv.v...>..>.....v.>.......>vv>>>....v...>.....>.v..vvv>.>>v..>.>.......>.>v>.v....>v>>.v>>.v...>.v>.v>..v>>.v>.
..>.v.>.>>.>v>.v..v>...v>.v.>>.v>.>.>>..v....vvv>>...v>v.v>...v....>..>v.....>>.>vv.>>>..>..>.v.>>..>v>>>.vv>..vv.v..>.>...........v>.v....
..v>v..>......v>v..>.vv.vv>....>...vv.v>>.>.....>>..>>>v.vv.v....vvv>v..v..v>vv.>....>v.v...>v.v>v.>..>>..>>....>...v..>.v>.vvv>.>>.vv.v>v.
v.v>..>.vv.>>>..vv.>.>>>v...>v>v.>.>>..>>...v.v>v>>>vv.>>.>v.v.>.>vv>..v.v..>.v..v......>v>v.v..>...>.......>v>.>.>.>..v.v..v>.>>....>.>>>.
.....>....>v...v....>...>..>v..v.vv>v>....>...v>v.>.v>>..v>>v>vv.....v.>..>>v>>....v.>.>..>.v...>.>vv>...vv>>.vv>v>.v.>v..>>vv>v..>...>..v.''';
