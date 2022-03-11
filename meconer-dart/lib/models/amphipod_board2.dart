import 'dart:math';

import 'package:flutter/foundation.dart';

class AmphipodBoard2 {
  static String emptyPos = '.';
  List<String> positions = List.generate(27, (_) => emptyPos);
  static List<int> hallwayPositions = List.generate(11, (index) => (index));
  static const int homeStart = 11;
  static List<int> homePositions =
      List.generate(16, (index) => (index + homeStart));

  static List<int> permittedHallwayPositions = [
    0,
    1,
    3,
    5,
    7,
    9,
    10
  ];

  String targetState = '...........ABCDABCDABCDABCD';

  static AmphipodBoard2 fromInput(List<String> lines) {
    AmphipodBoard2 board = AmphipodBoard2();

    String hallway = lines[1].trim().replaceAll('#', '');
    for (int i = 0; i < hallway.length; i++) {
      board.positions[i] = hallway[i];
    }
    for (int lineNo = 0; lineNo < 4; lineNo++) {
      for (int col = 0; col < 4; col++) {
        String homeLine = lines[lineNo + 2].trim().replaceAll('#', '');
        board.positions[homeStart + lineNo * 4 + col] = homeLine[col];
      }
    }
    return board;
  }

  List<MoveWithEnergy> getPossibleMoves() {
    // Loop through all positions
    List<MoveWithEnergy> possibleMoves = []; // Possible states after move

    // Check if any amphipods are in the hallway and can move into their
    // destination rooms
    for (final pos in hallwayPositions) {
      final amphiPod = positions[pos];
      if (amphiPod != emptyPos) {
        int destRoomToMoveInto = getDestinationHomePos(pos);
        if (destRoomToMoveInto != 0) {
          // Amphipod home is available. Check if the path is blocked
          int home = getHomeRoom(amphiPod);
          int hallwayAboveHome = getHallwayAboveHomeNo(home);
          if (isFreePath(hallwayAboveHome, pos)) {
            // The move is possible. Add to the list of moves
            possibleMoves.add(getMoveToHome(pos, destRoomToMoveInto, amphiPod));
          }
        }
      }
    }

    // Check the home positions and find all the possible moves into the hallway
    for (int pos in homePositions) {
      if (positions[pos] != emptyPos) {
        if (needToMove(pos)) {
          possibleMoves.addAll(getMovesIntoHallway(pos));
        }
      }
    }

    return possibleMoves;
  }

  bool isUpper(int pos) {
    return pos >= 11 && pos <= 14;
  }

  int getPosBelow(int pos) {
    return pos + 4;
  }

  int getPosAbove(int pos) {
    return pos - 4;
  }

  void print() {
    debugPrint('#############');

    // Print hallway
    String s = '#';
    for (int pos in hallwayPositions) {
      s += positions[pos];
    }
    s += '#';
    debugPrint(s);

    // Print upper and lower homes
    String lineStart = '###';
    String lineEnd = '##';
    for (int lineNo = 0; lineNo < 4; lineNo++) {
      String lineStr = lineStart;
      for (int colNo = 0; colNo < 4; colNo++) {
        lineStr += positions[homeStart + lineNo * 4 + colNo] + '#';
      }
      lineStr += lineEnd;
      debugPrint(lineStr);
      lineStart = '  #';
      lineEnd = '';
    }
    debugPrint('  #########');
    debugPrint(positions.join());
    debugPrint('-------------');
  }

  int getDestinationHomePos(int pos) {
    final amphipodToMove = positions[pos];
    // Check if this amphipods home room is empty or only has amphipods of correct type

    // Start at the lowest home
    var homePos = getLowestHome(getHomeRoom(amphipodToMove));
    var occupant = positions[homePos];
    while (occupant != emptyPos) {
      if (occupant != amphipodToMove) {
        // Lower pos has wrong type of amphipod. Not possible to move here
        return 0;
      }
      // If we get here the lower pos has correct type amphipod so if the upper
      // pos is empty we can move here
      if ( isHighestHome(homePos)) return 0; // we are already at the top so we cannot move here
      homePos = getPosAbove(homePos);
      occupant = positions[homePos];
    }
    // If we get here the pos is empty and we can move here.
    return homePos;
  }

  int getHallwayAboveHomeNo(int home) {
    return home * 2 + 2;
  }

  bool isFreePath(int pos1, int pos2) {
    int left = min(pos1, pos2);
    int right = max(pos1, pos2);
    if (right - left <= 1) return true;
    for (int p = left + 1; p < right; p++) {
      if (positions[p] != emptyPos) return false;
    }
    return true;
  }

  // Returns 0 for A, 1 for B, 2 for C and so on
  int getHomeRoom(String amphiPod) {
    int homeRoom = amphiPod.codeUnitAt(0) - 'A'.codeUnitAt(0);
    return homeRoom;
  }

  int getStepEnergy(String amphiPod) {
    switch (amphiPod) {
      case 'A':
        return 1;
      case 'B':
        return 10;
      case 'C':
        return 100;
      case 'D':
        return 1000;
    }
    return -1;
  }

  int getDepthOfHomePos(int pos) {
    return ((pos - homeStart) / 4).floor();
  }

  MoveWithEnergy getMoveToHome(
      int pos, int destPosToMoveInto, String amphiPodToMove) {
    // Calculate energy needed for this move
    int p1 = getHallwayAboveHomeNo(getHomeRoom(amphiPodToMove));
    int hallwaySteps = (p1 - pos).abs();
    int homeSteps = getDepthOfHomePos(destPosToMoveInto) + 1;
    int energy = (hallwaySteps + homeSteps) * getStepEnergy(amphiPodToMove);

    if (energy < 0) {
      debugPrint('!!!');
    }

    // Make the new state
    List<String> newPositions = List.from(positions);
    newPositions[pos] = emptyPos;
    newPositions[destPosToMoveInto] = amphiPodToMove;
    String newState = newPositions.join();
    return MoveWithEnergy(newState, energy);
  }

  int getLowestHome(int homeRoom) {
    int lowestHome = homeRoom + 23;
    return lowestHome;
  }

  int getHighestHome(int homeRoom) {
    int upperHome = homeRoom + 11;
    return upperHome;
  }

  String getState() {
    return positions.join();
  }

  bool isLowestHome(int room) {
    return room >= 27;
  }

  bool isHighestHome(int room) {
    return room >= 11 && room < 15;
  }

  List<MoveWithEnergy> getMovesIntoHallway(int pos) {
    List<MoveWithEnergy> moves = [];

    // Check if pos above is free. If it is not, we cant move

    // First check if this is lower home pos. If it is blocked we cannot move and return the empty list.
    if (!isHighestHome(pos) && positions[getPosAbove(pos)] != emptyPos) {
      return moves;
    }

    // Check all possible hallway positions
    for (int hPos in permittedHallwayPositions) {
      if (positions[hPos] == emptyPos) {
        // This pos is empty. If the path is not blocked it is possible to move here
        if (isFreePath(hPos, getHallwayAboveHomePos(pos))) {
          moves.add(getMoveToHallway(hPos, pos));
        }
      }
    }
    return moves;
  }

  MoveWithEnergy getMoveToHallway(int hallwayPos, int startPos) {
    // Calculate energy needed for this move
    int p1 = getHallwayAboveHomePos(startPos);
    int hallwaySteps = (p1 - hallwayPos).abs();
    int homeSteps = getDepthOfHomePos(startPos) + 1;
    String amphiPodToMove = positions[startPos];
    int energy = (hallwaySteps + homeSteps) * getStepEnergy(amphiPodToMove);

    if (energy < 0) {
      debugPrint('!!!');
    }
    // Make the new state
    List<String> newPositions = List.from(positions);
    newPositions[startPos] = emptyPos;
    newPositions[hallwayPos] = amphiPodToMove;
    String newState = newPositions.join();
    return MoveWithEnergy(newState, energy);
  }

  // Returns the hallway position above pos. Must be in a home room
  int getHallwayAboveHomePos(int pos) {
    return (pos - AmphipodBoard2.homeStart) % 4 * 2 + 2;
  }

  // Returns true if the apod is in correct home "corridor"
  bool isInHome(String amphipod, pos) {
    int homeRoom = getHomeRoom(amphipod);
    List<int> homePositions =
        List.generate(4, (index) => index * 4 + homeStart + homeRoom);
    return homePositions.contains(pos);
  }

  // Returns false if we are in one of our home positions
  // and all of the lower positions also are at home.
  bool needToMove(int pos) {
    String amphiPod = positions[pos];
    if (amphiPod != emptyPos) {
      if (isInHome(amphiPod, pos)) {
        // This apod is in correct corridor. Check recursively if any of the lower apods
        // needs to move.
        int posBelow = getPosBelow(pos);
        if (posBelow >= positions.length) return false; // We are at lowest pos
        return needToMove(
            posBelow); // If the one below needs to move we also needs to
      } else {
        return true;
      }
    }
    return false; // No need to move an empty slot
  }

  int findMovesToTargetWithLeastEnergy() {
    List<DijkstraNode> unVisited = [];
    Set<String> visited = {};
    // Start state has energy 0
    bool finished = false;
    int energy = 0;
    final startNode = DijkstraNode(getState(), 0);
    startNode.energyUsedToGetHere = 0;
    unVisited.add(startNode);
    while (!finished && unVisited.isNotEmpty) {
      DijkstraNode thisNode = getUnvisitedWithLowestEnergy(unVisited)!;

      final neighbourNodes = getPossibleDijkstraNodes(thisNode.state, visited);

      for (var node in neighbourNodes) {
        int energy = thisNode.energyUsedToGetHere + node.cost;
        final sameNodeFromUnvisited = findNode(unVisited, node);
        if (sameNodeFromUnvisited != null) {
          if (energy > sameNodeFromUnvisited.energyUsedToGetHere) {
            node = sameNodeFromUnvisited;
            energy = node.energyUsedToGetHere;
          }
          unVisited.remove(sameNodeFromUnvisited);
        }
        if (energy < node.energyUsedToGetHere) {
          node.energyUsedToGetHere = energy;
          node.previousNode = thisNode;
        }
        unVisited.add(node);
      }
      visited.add(thisNode.state);
      energy = thisNode.energyUsedToGetHere;
      if (thisNode.state == targetState) {
        debugPrint('Finished');
        finished = true;
        AmphipodBoard2.fromState(thisNode.state).print();
        debugPrint('Energy : ${thisNode.energyUsedToGetHere}');
        var prevNode = thisNode.previousNode;
        while (prevNode != null) {
          AmphipodBoard2.fromState(prevNode.state).print();
          debugPrint('Energy : ${prevNode.energyUsedToGetHere}');
          prevNode = prevNode.previousNode;
        }
      }
    }
    return energy;
  }

  List<DijkstraNode> getPossibleDijkstraNodes(
      String state, Set<String> visitedNodes) {
    AmphipodBoard2 board = AmphipodBoard2.fromState(state);
    List<DijkstraNode> nodes = [];
    final moves = board.getPossibleMoves();
    for (final move in moves) {
      bool alreadyVisited = false;
      if (visitedNodes.contains(move.state)) {
        alreadyVisited = true;
        break;
      }
      if (!alreadyVisited) nodes.add(DijkstraNode(move.state, move.energy));
    }
    return nodes;
  }

  static AmphipodBoard2 fromState(String state) {
    AmphipodBoard2 board = AmphipodBoard2();
    board.positions = state.split('');
    return board;
  }

  DijkstraNode? getUnvisitedWithLowestEnergy(List<DijkstraNode> unVisited) {
    int energy = 999999999;
    DijkstraNode? toReturn;
    for (final node in unVisited) {
      if (node.energyUsedToGetHere < energy) {
        energy = node.energyUsedToGetHere;
        toReturn = node;
      }
    }
    if (toReturn != null) unVisited.remove(toReturn);
    return toReturn;
  }
}

DijkstraNode? findNode(List<DijkstraNode> unVisited, DijkstraNode nodeToFind) {
  DijkstraNode? toReturn;
  for (final node in unVisited) {
    if (node.state == nodeToFind.state) {
      toReturn = node;
    }
  }
  if (toReturn != null) unVisited.remove(toReturn);
  return toReturn;
}

class MoveWithEnergy {
  String state;
  int energy;

  MoveWithEnergy(this.state, this.energy);
}

class DijkstraNode {
  String state;
  int energyUsedToGetHere = 99999999999999;
  int cost;
  DijkstraNode? previousNode;

  DijkstraNode(this.state, this.cost);
}
