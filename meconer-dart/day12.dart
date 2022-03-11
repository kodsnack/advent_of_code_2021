import 'package:flutter/material.dart';


class Day12 extends StatelessWidget {
  const Day12({Key? key}) : super(key: key);
  static String routeName = 'day12';
  final bool isExample = true;
  static String dayTitle = 'Day 12: Passage Pathing';

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
            SelectableText('Svar dag 12 del 1: $resultPart1'),
            SelectableText('Svar dag 12 del 2 : $resultPart2'),
          ],
        ),
      ),
    );
  }



  int doPart1() {
    final caveSystem = getInput(isExample);
    caveSystem.findPaths();
    return caveSystem.solutions.length;
  }

  int doPart2() {
    final caveSystem = getInput(isExample);
    caveSystem.findPathsPart2();
    return caveSystem.solutions.length;
  }

  CaveSystem getInput(bool example) {
    CaveSystem caveSystem = CaveSystem();
    late List<String> lines;
    if (example) {
      lines =  exampleInputText.split('\n');
    } else {
      lines = inputText.split('\n');
    }
    for ( String line in lines ) {
      final caveNames = line.split('-');
      caveSystem.addCaves(caveNames[0], caveNames[1]);
      caveSystem.addCaves(caveNames[1], caveNames[0]);
    }
    return caveSystem;
  }
}

class VisitCounter {
  late final Map<Cave,int> visitCount;

  VisitCounter() {
    visitCount = {};
  }

  VisitCounter.from(VisitCounter visitCounter) {
    visitCount = {};
    for (final key in visitCounter.visitCount.keys) {
      visitCount[key] = visitCounter.visitCount[key]!;
    }
  }

  bool isLegalVisit(Cave cave) {
    if (cave.isLarge()) return true;
    int maxValue = 0;
    for ( int value in visitCount.values ) {
      if ( value > maxValue) maxValue = value;
    }
    if (visitCount.containsKey(cave )) {

      if (['start','end'].contains(cave.name)) return false;
      if (maxValue < 2) {
        visitCount[cave] = visitCount[cave]! + 1;
        return true;
      }
      return false;
    } else {
      visitCount[cave] = 1;
    }
    return true;
  }

}

class Cave {
  String name;
  Set<Cave> connections = {};

  Cave(this.name);

  bool isSmall() {
    if (name.toLowerCase() == name) return true;
    return false;
  }

  bool isLarge() {
    return !isSmall();
  }
}


class CaveSystem {
  Set<Cave> caveSet = {};
  List<String> solutions = [];

  void addCaves(String caveName, String connectedToCaveName) {
    final cave = getCaveIfExists(caveName) ?? Cave(caveName);
    final connectedCave = getCaveIfExists(connectedToCaveName) ?? Cave(connectedToCaveName);
    cave.connections.add(connectedCave);
    connectedCave.connections.add(cave);
    caveSet.add(cave);
    caveSet.add(connectedCave);
  }

  Cave? getCaveIfExists(String nameToCheck) {
    for (final cave in caveSet) {
      if (cave.name == nameToCheck) return cave;
    }
    return null;
  }

  void printConnections() {
    for (var cave in caveSet) {
      debugPrint('Cave ${cave.name}');
      for (var connection in cave.connections ) {
        debugPrint(' - ${connection.name}');
      }
    }
  }

  void findPaths() {
    String pathStr = '';
    final startCave = locateCaveByName('start')!;
    Set<Cave> visitedSmallCaves = {startCave};

    findAllPaths(startCave, Set.from(visitedSmallCaves), '', pathStr);
  }

  void findPathsPart2() {
    String pathStr = '';
    final startCave = locateCaveByName('start')!;
    VisitCounter visitCounter = VisitCounter();
    findAllPathsPart2(startCave, visitCounter, '', pathStr);
  }

  void printVisited(Set<Cave> visited) {
    String s = '';
    for (final cave in visited) {
      s += cave.name + ', ';
    }
    debugPrint('Visited : $s');
  }

  void findAllPaths(Cave cave, Set<Cave> visitedSmallCaves, String indent, String pathStr) {
    if (cave.name == 'end') {
      // Path ends here. Return it
      pathStr += ', ' + cave.name;
      solutions.add(pathStr);
    }
    pathStr += ', ' + cave.name;
    for (Cave nextCave in cave.connections) {
      //debugPrint(' $indent - ${nextCave.name}');
      if (nextCave.isSmall()) {
        if ( !visitedSmallCaves.contains(nextCave)) {
          final newVisitedSet = Set<Cave>.from(visitedSmallCaves);
          newVisitedSet.add(nextCave);
          findAllPaths(nextCave, newVisitedSet, indent + '  ', pathStr);
        }
      } else {
        findAllPaths(nextCave, Set.from(visitedSmallCaves), indent + '  ', pathStr);
      }
    }
  }

  void findAllPathsPart2(Cave cave, VisitCounter visitCounter, String indent, String pathStr) {
    if (cave.name == 'end') {
      // Path ends here. Return it
      pathStr += ', ' + cave.name;
      solutions.add(pathStr);
      return;
    }
    if (cave.isSmall()) {
      if (!visitCounter.isLegalVisit(cave)) return;
    }
    pathStr += ', ' + cave.name;
    for (Cave nextCave in cave.connections) {
      //debugPrint(' $indent - ${nextCave.name}');
      final newVisitCounter = VisitCounter.from(visitCounter);
      findAllPathsPart2(nextCave, newVisitCounter, indent + '  ', pathStr);
    }
  }

  Cave? locateCaveByName(String nameToFind) {
    for (final node in caveSet ) {
      if (node.name == nameToFind) return node;
    }
    return null;
  }
}

String exampleInputText =
'''start-A
start-b
A-c
A-b
b-d
A-end
b-end''';

String inputText =
'''mj-TZ
start-LY
TX-ez
uw-ez
ez-TZ
TH-vn
sb-uw
uw-LY
LY-mj
sb-TX
TH-end
end-LY
mj-start
TZ-sb
uw-RR
start-TZ
mj-TH
ez-TH
sb-end
LY-ez
TX-mt
vn-sb
uw-vn
uw-TZ''';
