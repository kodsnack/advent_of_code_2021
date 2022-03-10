import 'dart:math';

import 'package:flutter/foundation.dart';

class AmphipodBoard {
  static String emptyPos = '.';
  List<String> positions = List.generate(19, (_) => emptyPos);
  static List<int> hallwayPositions = List.generate(11, (index) => (index));
  static List<int> homePositions = List.generate(8, (index) => (index + 11));
  static List<int> homeUpperPositions =
  List.generate(4, (index) => (index + 11));
  static List<int> homeLowerPositions =
  List.generate(4, (index) => (index + 15));

  static List<int> permittedHallwayPositions = [0,1,3,5,7,9,10]; // We don't need to use pos 0 and 10.
  // This shortens calculations significantly

  String targetState = '...........ABCDABCD';

  static AmphipodBoard fromInput(List<String> lines) {
    AmphipodBoard board = AmphipodBoard();

    String hallway = lines[1].substring(1,11);
    for (int i = 0; i < hallway.length; i++) {
      board.positions[i] = hallway[i];
    }

    String homeUpper = lines[2].replaceAll('#', '');
    String homeLower = lines[3].trim().replaceAll('#', '');
    for ( int i = 0 ; i < 4; i++) {
      board.positions[homeUpperPositions[i]] = homeUpper[i];
      board.positions[homeLowerPositions[i]] = homeLower[i];
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
        int destRoomToMoveInto = getDestinationRoomPos(pos);
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

    // Check the upper home positions and find all the possible moves into the hallway
    for (int pos in homeUpperPositions) {
      if ( positions[pos] != emptyPos) {
        if (needToMove(pos)) {
          possibleMoves.addAll(getMovesIntoHallway(pos));
        }
      }
    }

    // Last, check the lower home positions and find the possible moves into hallway
    for (int pos in homeLowerPositions) {
      if ( positions[pos] != emptyPos) {
        if (needToMove(pos)) {
          possibleMoves.addAll(getMovesIntoHallway(pos));
        }
      }
    }
    return possibleMoves;
  }

  bool isUpper(int pos) {
    return homeUpperPositions.contains(pos);
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
    String upper = '###';
    for (int pos in homeUpperPositions) {
      upper += positions[pos] + '#';
    }

    String lower = '  #';
    for (int pos in homeLowerPositions) {
      lower += positions[pos] + '#';
    }
    upper += '##';
    debugPrint(upper);
    debugPrint(lower);
    debugPrint('  #########');
    debugPrint(positions.join());
  }

  int getDestinationRoomPos(int pos) {
    final amphipodToMove = positions[pos];
    // Check if this amphipods home room is empty or only has amphipods of correct type
    final homeLowerPos = getLowerHome( getHomeRoom(amphipodToMove) );
    final occupantOfLowerPos = positions[homeLowerPos];
    if (occupantOfLowerPos != emptyPos) {
      if (occupantOfLowerPos != amphipodToMove) {
        // Lower pos has wrong type of amphipod. Not possible to move here
        return 0;
      }
      // If we get here the lower pos has correct type amphipod so if the upper
      // pos is empty we can move here
      final homeUpperPos = getUpperHome( getHomeRoom(amphipodToMove));
      final occupantOfUpperPos = positions[homeUpperPos];
      if (occupantOfUpperPos == emptyPos) {
        return homeUpperPos;
      } else {
        // not empty
        return 0;
      }
    } else {
      // lower pos is empty so it is possible to move here.
      return homeLowerPos;
    }
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
      case 'A' : return 1;
      case 'B' : return 10;
      case 'C' : return 100;
      case 'D' : return 1000;
    }
    return -1;
  }

  MoveWithEnergy getMoveToHome(int pos, int destRoomToMoveInto, String amphiPodToMove) {
    // Calculate energy needed for this move
    int p1 = getHallwayAboveHomeNo(getHomeRoom(amphiPodToMove));
    int hallwaySteps = (p1 - pos).abs();
    int homeSteps = 1;
    if ( isLower(destRoomToMoveInto)) homeSteps = 2;
    int energy = (hallwaySteps + homeSteps) * getStepEnergy(amphiPodToMove);

    if ( energy < 0 ) {
      debugPrint('!!!');
    }

    // Make the new state
    List<String> newPositions = List.from(positions);
    newPositions[pos] = emptyPos;
    newPositions[destRoomToMoveInto] = amphiPodToMove;
    String newState = newPositions.join();
    return MoveWithEnergy(newState, energy);
  }

  int getLowerHome(int homeRoom) {
    int lowerHome = homeRoom + 15;
    return lowerHome;
  }

  int getUpperHome(int homeRoom) {
    int upperHome = homeRoom + 11;
    return upperHome;
  }

  String getState() {
    return positions.join();
  }

  bool isLower(int room) {
    return homeLowerPositions.contains(room);
  }

  List<MoveWithEnergy> getMovesIntoHallway(int pos) {
    List<MoveWithEnergy> moves = [];

    // First check if this is lower home pos. If it is blocked we cannot move.
    if ( isLower(pos) && positions[getPosAbove(pos)] != emptyPos) return moves;
    // Check all possible hallway positions
    for ( int hPos in permittedHallwayPositions) {
      if ( positions[hPos] == emptyPos ) {
        // This pos is empty. If the path is not blocked it is possible to move here
        if ( isFreePath(hPos, getHallwayAboveHomePos(pos))) {
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
    int homeSteps = 1;
    if ( isLower(startPos)) homeSteps = 2;
    String amphiPodToMove = positions[startPos];
    int energy = (hallwaySteps + homeSteps) * getStepEnergy(amphiPodToMove);

    if ( energy < 0 ) {
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
    int posToCheck = pos;
    if ( isLower(pos)) posToCheck -= 4;
    int hallwayPos = (posToCheck - 11) * 2 + 2;
    return hallwayPos;
  }

  bool needToMove(int pos) {
    String amphiPod = positions[pos];
    if ( amphiPod != emptyPos) {
      int homeRoom = getHomeRoom(amphiPod);
      // If we are in our lower home we don't need to move
      if ( getLowerHome(homeRoom) == pos) return false;
      // If we are in our upper home and we have same kind of amphipod below we don't need to move
      if ( getUpperHome(homeRoom) == pos && positions[getLowerHome(homeRoom)] == amphiPod) return false;
    }
    return true;
  }

  int findMovesToTargetWithLeastEnergy() {
    List<DijkstraNode> unVisited = [];
    Set<String> visited = {};
    // Start state has energy 0
    bool finished = false;
    int energy = 0;
    final startNode = DijkstraNode(getState(),0);
    startNode.energyUsedToGetHere = 0;
    unVisited.add(startNode);
    while ( !finished && unVisited.isNotEmpty) {
      DijkstraNode thisNode = getUnvisitedWithLowestEnergy(unVisited)!;

      final neighbourNodes = getPossibleDijkstraNodes(thisNode.state, visited);

      for ( var node in neighbourNodes ) {
        int energy  = thisNode.energyUsedToGetHere + node.cost;
        final sameNodeFromUnvisited = findNode(unVisited, node);
        if (sameNodeFromUnvisited != null ) {
          if ( energy > sameNodeFromUnvisited.energyUsedToGetHere) {
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
      if ( thisNode.state == targetState) {
        debugPrint('Finished');
        finished = true;
        AmphipodBoard.fromState(thisNode.state).print();
        debugPrint('Energy : ${thisNode.energyUsedToGetHere}');
        var prevNode = thisNode.previousNode;
        while (prevNode != null ) {
          AmphipodBoard.fromState(prevNode.state).print();
          debugPrint('Energy : ${prevNode.energyUsedToGetHere}');
          prevNode = prevNode.previousNode;
        }
      }
    }
    return energy;
  }

  List<DijkstraNode> getPossibleDijkstraNodes(String state, Set<String> visitedNodes) {
    AmphipodBoard board = AmphipodBoard.fromState(state);
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

  static AmphipodBoard fromState(String state) {
    AmphipodBoard board = AmphipodBoard();
    board.positions = state.split('');
    return board;
  }

  DijkstraNode? getUnvisitedWithLowestEnergy(List<DijkstraNode> unVisited) {
    int energy = 999999999;
    DijkstraNode? toReturn;
    for ( final node in unVisited ) {
      if ( node.energyUsedToGetHere < energy ) {
        energy = node.energyUsedToGetHere;
        toReturn = node;
      }
    }
    if ( toReturn != null ) unVisited.remove(toReturn);
    return toReturn;
  }

}

DijkstraNode? findNode(List<DijkstraNode> unVisited, DijkstraNode nodeToFind) {
  DijkstraNode? toReturn;
  for ( final node in unVisited ) {
    if ( node.state == nodeToFind.state) {
      toReturn = node;
    }
  }
  if ( toReturn != null ) unVisited.remove(toReturn);
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
