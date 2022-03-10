
import 'package:flutter/foundation.dart';
import 'package:intl/intl.dart';

class BoardPos {
  int value;
  bool marked;

  BoardPos(this.value, this.marked);
}

class BingoBoard {
  late List<List<BoardPos>> board;

  bool won = false;

  BingoBoard(this.board);

  BingoBoard.fromInts(List<List<int>> numbers) {
    List<List<BoardPos>> boardGrid = [];
    for ( List<int> numberRow in numbers) {
      List<BoardPos> boardPosRow = [];
      for ( int number in numberRow ) {
        boardPosRow.add(BoardPos(number, false));
      }
      boardGrid.add(boardPosRow);
    }
    board = boardGrid;
  }

  void markNumber(int numberToMark) {
    for ( List<BoardPos> boardRow in board ) {
      for (BoardPos boardPos in boardRow) {
        if (boardPos.value == numberToMark) {
          boardPos.marked = true;
        }
      }
    }
  }

  void debugPrintBoard() {
    for ( List<BoardPos> boardRow in board ) {
      String lineToPrint = '';
      for (BoardPos boardPos in boardRow) {
        String numStr = NumberFormat('00').format(boardPos.value);
        if (boardPos.marked) {
          lineToPrint += ' *$numStr* ';
        } else {
          lineToPrint += '  $numStr  ';
        }
      }
      debugPrint(lineToPrint);
    }
    debugPrint('============================');
  }

  bool checkHorizontalWin() {
    for ( List<BoardPos> boardRow in board ) {
      bool win = true;
      for (BoardPos boardPos in boardRow) {
        if (!boardPos.marked) win = false;
      }
      if (win) return true;
    }
    return false;
  }

  bool checkVerticalWin() {
    for ( int column = 0 ; column < board.length; column++ ) {
      bool win = true;
      for ( List<BoardPos> boardRow in board ) {
        if (!boardRow[column].marked) win = false;
      }
      if (win) return true;
    }
    return false;
  }

  bool checkWin() {
    if (checkHorizontalWin()) {
      won = true;
      return true;
    }
    if (checkVerticalWin()) {
      won = true;
      return true;
    }
      return false;
  }

  int getSumOfUnmarked() {
    int sum = 0 ;
    for ( List<BoardPos> boardRow in board ) {
      for (BoardPos boardPos in boardRow) {
        if (!boardPos.marked) sum += boardPos.value;
      }
    }
    return sum;
  }
}
