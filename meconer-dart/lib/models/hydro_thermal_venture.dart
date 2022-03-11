import 'package:flutter/foundation.dart';

class GridLine {
  late int x1,y1,x2,y2;

  GridLine(this.x1, this.x2, this.y1, this.y2);

  GridLine.fromLine(String line) {
    final regex = RegExp(r'^(\d+),(\d+) +-> (\d+),(\d+)$');
    final match = regex.firstMatch(line);
    x1 = int.parse(match!.group(1)!);
    y1 = int.parse(match.group(2)!);
    x2 = int.parse(match.group(3)!);
    y2 = int.parse(match.group(4)!);
  }

  int getMaxX() {
    if (x1 > x2) {
      return x1;
    } else {
      return x2;
    }
  }

  int getMinX() {
    if (x1 < x2) {
      return x1;
    } else {
      return x2;
    }
  }

  int getMaxY() {
    if (y1 > y2) {
      return y1;
    } else {
      return y2;
    }
  }

  int getMinY() {
    if (y1 < y2) {
      return y1;
    } else {
      return y2;
    }
  }

}

class HydroThermalVenture {
  List<List<int>> hydroThermalGrid = [];
  int gridSizeY = 0;
  int gridSizeX = 0;

  HydroThermalVenture(this.hydroThermalGrid);

  HydroThermalVenture.fromLines(List<String> lines, {bool enableDiagonal = false}) {
    List<GridLine> gridLines = [];
    for (String line in lines) {
      GridLine gridLine = GridLine.fromLine(line);
      gridLines.add(gridLine);
      if ( gridLine.getMaxX() + 1 > gridSizeX) gridSizeX = gridLine.getMaxX() + 1;
      if ( gridLine.getMaxY() + 1 > gridSizeY) gridSizeY = gridLine.getMaxY() + 1;
    }

    for ( int y = 0 ; y < gridSizeY; y++) {
      hydroThermalGrid.add(List.filled(gridSizeX, 0));
    }

    //drawGrid();
    for (GridLine gridLine in gridLines ) {
      if (gridLine.y1 == gridLine.y2) {
        // horizontal line
        for (int x = gridLine.getMinX(); x <= gridLine.getMaxX(); x++) {
          hydroThermalGrid[gridLine.y1][x]++;
        }
      } else if (gridLine.x1 == gridLine.x2) {
        // Vertical line
        for (int y = gridLine.getMinY(); y <= gridLine.getMaxY(); y++) {
          hydroThermalGrid[y][gridLine.x1]++;
        }
      } else if (enableDiagonal) {
        // Do this only if diagonal checking is enabled
        int dx = gridLine.x2 - gridLine.x1;
        int dy = gridLine.y2 - gridLine.y1;
        int dirx = dx.sign;
        int diry = dy.sign;
        for (int i = 0; i <= dx.abs(); i++) {
          hydroThermalGrid[gridLine.y1 + diry * i][gridLine.x1 + dirx * i]++;
        }
      }
      //drawGrid();
    }
  }

  int countNoOfDangerousPoints() {
    int count = 0;
    for ( var lines in hydroThermalGrid) {
      for (var point in lines) {
        if (point >=2) count++;
      }
    }
    return count;
  }

  void drawGrid() {
    for ( List<int> line in hydroThermalGrid) {
      String lineToPrint = '';
      for (int value in line ) {
        if (value == 0) {
          lineToPrint += '.';
        } else {
          lineToPrint += '$value';
        }
      }
      debugPrint(lineToPrint);
    }
    debugPrint('');
  }

}