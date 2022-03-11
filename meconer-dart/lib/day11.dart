import 'package:flutter/material.dart';


class Day11 extends StatelessWidget {
  const Day11({Key? key}) : super(key: key);
  static String routeName = 'day11';
  final bool isExample = false;
  static String dayTitle = 'Day 11: Dumbo Octopus';

  @override
  Widget build(BuildContext context) {
    final resultPart1 = doPart1();
    final resultPart2 = doPart2();
    return Scaffold(
      appBar: AppBar(
        title: Text(dayTitle),
      ),
      body: Center(
        child: Column(
          children: [
            const SizedBox(
              height: 200,
            ),
            SelectableText('Svar dag 11 del 1: $resultPart1'),
            SelectableText('Svar dag 11 del 2 : $resultPart2'),
          ],
        ),
      ),
    );
  }

  int doPart1() {
    final inputs = getInput(isExample);
    final octopusGrid = OctopusGrid.fromInputs(inputs);
    int flashes = 0;
    for ( int step = 0 ; step < 100; step++) {
      flashes += octopusGrid.doStep();
    }
    return flashes;
  }

  int doPart2() {
    final inputs = getInput(isExample);
    final octopusGrid = OctopusGrid.fromInputs(inputs);
    int step = 0;
    while ( !octopusGrid.syncronizedFlash()) {
      octopusGrid.doStep();
      step++;
    }
    return step;
  }

  List<List<int>> getInput(bool example) {
    List<List<int>> input = [];
    List<String> lines;
    if (example) {
      lines =  exampleInputText.split('\n');
    } else {
      lines = inputText.split('\n');
    }
    for ( String line in lines ) {
      List<int> lineValues = [];
      for ( String value in line.split('')) {
        lineValues.add(int.parse(value));
      }
      input.add(lineValues);
    }
    return input;
  }

  List<List<bool>> getEmptyVisitedList(int width, int height) {
    List<List<bool>> emptyList = [];
    for (int i = 0 ; i < height; i++ ) {
      emptyList.add(List.filled(width, false));
    }
    return emptyList;
  }


}

class OctopusGrid {
  late List<List<Octopus>> grid;

  OctopusGrid(this.grid);

  OctopusGrid.fromInputs(List<List<int>> inputs) {
    grid = [];
    for ( List<int> row in inputs) {
      List<Octopus> octopusRow = [];
      for (int value in  row ) {
        final octopus = Octopus(value, false);
        octopusRow.add(octopus);
      }
      grid.add(octopusRow);
    }
  }

  void printGrid() {
    debugPrint('');
    for (final row in grid) {
      String line = '';
      for (final octopus in row) {
        int level = octopus.energyLevel;
        if (level > 9) {
          line += '#';
        } else {
          line += level.toString();
        }
      }
      debugPrint(line);
    }

  }

  void increaseAll() {
    for (final row in grid) {
      for (final octopus in row) {
        octopus.energyLevel++;
      }
    }
  }

  int doStep() {
    increaseAll();
    List<Location> neighboursToIncrease = [];
    for ( int row = 0; row < grid.length; row++ ) {
      for ( int column = 0 ; column < grid[0].length; column++ ) {
        if ( grid[row][column].energyLevel > 9  ) {
          grid[row][column].flashing = true;
          neighboursToIncrease.addAll(getNeighbours(row: row, column: column, width: grid[0].length, height: grid.length));
        }
      }
    }
    while (neighboursToIncrease.isNotEmpty ) {
      neighboursToIncrease = increaseNeighbours(neighboursToIncrease);
    }
    int flashes = countFlashesAndReset();
    return flashes;
  }

  int countFlashesAndReset() {
    int count = 0;
    for (final row in grid) {
      for (final octopus in row) {
        if (octopus.flashing) {
          octopus.flashing = false;
          octopus.energyLevel = 0;
          count++;
        }
      }
    }
    return count;
  }

  List<Location> increaseNeighbours(List<Location> neighboursToIncrease) {
    List<Location> newNeighbours = [];
    for ( final location in neighboursToIncrease) {
      if ( !grid[location.row][location.column].flashing ) {
        grid[location.row][location.column].energyLevel++;
        if ( grid[location.row][location.column].energyLevel >9) {
          grid[location.row][location.column].flashing = true;
          newNeighbours.addAll( getNeighbours(row: location.row,
              column: location.column,
              width: grid[0].length,
              height: grid.length) );
        }
      }
    }
    return newNeighbours;
  }

  bool syncronizedFlash() {
    for (final row in grid) {
      for (final octopus in row) {
        if (octopus.energyLevel != 0 ) {
          return false;
        }
      }
    }
    return true;
  }

}

class Octopus {
  int energyLevel;
  bool flashing;
  bool isNeighbourToFlashing = false;

  Octopus(this.energyLevel, this.flashing);
}

List<Location> getNeighbours({required int row, required int column, required int width, required int height}) {
  List<Location> locations = [];
  // Neighbour above
  if (row > 0 ) locations.add(Location(row-1, column));
  // Neighbour below
  if ( row < height-1 ) locations.add(Location( row+1, column));
  // Neighbour to the left
  if ( column > 0 ) locations.add(Location(row, column-1));
  // Neighbour to the right
  if ( column < width-1 ) locations.add(Location(row, column+1));

  // Diagonal neighbours
  // Neighbour up left
  if ( row > 0 && column > 0 ) locations.add(Location(row-1, column-1));
  // Neighbour up right
  if ( row > 0 && column < width-1 ) locations.add(Location(row-1, column + 1));
  // Neighbour down right
  if ( row < height - 1 && column < width-1 ) locations.add(Location(row+1, column + 1));
  // Neighbour down left
  if ( row < height - 1 && column > 0 ) locations.add(Location(row+1, column - 1));
  return locations;
}


class Location {
  int row;
  int column;

  Location(this.row, this.column);
}
String exampleInputText =
'''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526''';

String inputText =
'''4525436417
1851242553
5421435521
8431325447
4517438332
3521262111
3331541734
4351836641
2753881442
7717616863''';
