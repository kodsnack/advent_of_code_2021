import 'package:flutter/material.dart';

class Day18 extends StatelessWidget {
  const Day18({Key? key}) : super(key: key);
  static const String routeName = 'day18';
  final bool isExample = false;
  static const String dayTitle = 'Day 18: Snailfish';

  @override
  Widget build(BuildContext context) {
    final resultPart1 = doPart1();
    final resultPart2 = doPart2();
    return Scaffold(
      appBar: AppBar(
        title: const Text(dayTitle),
      ),
      body: Center(
        child: Column(
          children: [
            const SizedBox(
              height: 200,
            ),
            SelectableText('Svar dag 18 del 1: $resultPart1'),
            SelectableText('Svar dag 18 del 2 : $resultPart2'),
          ],
        ),
      ),
    );
  }

  int doPart1() {
    final inputList = getInput(isExample);
    bool first = true;
    SnailfishNumber? sfn;
    for ( String s in inputList) {
      final tokenProvider = TokenProvider( s );
      if ( first ) {
        sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
        first = false;
      } else {
        sfn = sfn!.add(SnailfishNumber.fromTokenProvider(tokenProvider));
        sfn.reduce();
      }
    }

    return sfn!.getMagnitude();
  }

  int doPart2() {
    final inputList = getInput(isExample);
    int maxMagnitude = 0;
    for ( int i = 0; i < inputList.length-1; i++) {
      for ( int j = i+1 ; j < inputList.length; j++ ) {
        var sfn1 = SnailfishNumber.fromTokenProvider(TokenProvider(inputList[i]));
        var sfn2 = SnailfishNumber.fromTokenProvider(TokenProvider(inputList[j]));

        var sfn3 = sfn1!.add(sfn2);
        sfn3.reduce();
        int magnitude = sfn3.getMagnitude();
        if ( magnitude > maxMagnitude ) maxMagnitude = magnitude;

        sfn1 = SnailfishNumber.fromTokenProvider(TokenProvider(inputList[i]));
        sfn2 = SnailfishNumber.fromTokenProvider(TokenProvider(inputList[j]));
        var sfn4 = sfn2!.add(sfn1);
        sfn4.reduce();
        magnitude = sfn4.getMagnitude();
        if ( magnitude > maxMagnitude ) maxMagnitude = magnitude;
      }
    }

    return maxMagnitude;
  }

  List<String> getInput(bool example) {
    String s = isExample ? exampleInputText : inputText;
    return s.split('\n');
  }
}

class SnailfishNumber {
  bool? isSingleNumber = false;
  int? number;
  int? orderNumber;
  SnailfishNumber? left, right;

  static SnailfishNumber? fromTokenProvider(TokenProvider tokenProvider) {
    SnailfishNumber snailfishNumber = SnailfishNumber();
    String token = tokenProvider.getToken();
    if ( token == '[') {
      snailfishNumber.left = SnailfishNumber.fromTokenProvider(tokenProvider);
      token = tokenProvider.getToken();
    }
    if ( token == ',') {
      snailfishNumber.right = SnailfishNumber.fromTokenProvider(tokenProvider);
      token = tokenProvider.getToken();
    }
    if ( token == ']') return snailfishNumber;
    if (isDigit(token)) {
      snailfishNumber.isSingleNumber = true;
      snailfishNumber.number = int.parse(token);
      return snailfishNumber;
    }
  }

  int getDepth() {
    if ( isSingleNumber!) return 0 ;
    int leftDepth = left!.getDepth();
    int rightDepth = right!.getDepth();
    if (leftDepth > rightDepth )  return 1 + leftDepth;
    return 1 + rightDepth;
  }

  static int orderNo = 0;
  static int maxOrderNo = 0;

  calcOrderNumbersPrepare() {
    orderNo = 0;
    maxOrderNo = 0;
  }

  calcOrderNumbers() {
    if ( isSingleNumber!) {
      maxOrderNo = orderNo;
      orderNumber = orderNo++;
    } else {
      left!.calcOrderNumbers();
      right!.calcOrderNumbers();
    }
  }

  String toSnailfishString() {
    if (isSingleNumber!) return number.toString();
    String s = '[' + left!.toSnailfishString() + ',' + right!.toSnailfishString() + ']';
    return s;
  }

  int getMagnitude() {
    if ( isSingleNumber! ) {
      return number!;
    }
    return 3 * left!.getMagnitude() + 2 * right!.getMagnitude();
  }

  SnailfishNumber getLeft() {
    return left!;
  }

  int? getValue() {
    if ( isSingleNumber! ) {
      return number!;
    }
  }

  SnailfishNumber getRight() {
      return right!;
  }

  int? getLeftAtLevel(int levelToFind, int currentLevel) {
    if (levelToFind == currentLevel) {
      if (isSingleNumber!) {
        return number;
      } else {
        throw('This is wrong');
      }
    } else {
      if ( isSingleNumber!) return null;
      int? value = left!.getLeftAtLevel(levelToFind, currentLevel + 1 );
      value ??= right!.getLeftAtLevel(levelToFind, currentLevel +1);
      return value;
    }
  }

  int? getRightAtLevel(int levelToFind, int currentLevel) {
    if (levelToFind == currentLevel) {
      if (isSingleNumber!) {
        return number;
      } else {
        throw('This is wrong');
      }
    } else {
      if ( isSingleNumber!) return null;
      int? value = right!.getRightAtLevel(levelToFind, currentLevel + 1 );
      value ??= left!.getRightAtLevel(levelToFind, currentLevel +1);
      return value;
    }
  }

  SnailfishNumber add(SnailfishNumber? sfn2) {
    SnailfishNumber snailfishNumber = SnailfishNumber();
    snailfishNumber.isSingleNumber = false;
    snailfishNumber.left = this;
    snailfishNumber.right = sfn2;
    return snailfishNumber;
  }

  String toSnailfishStringWithOrderNumbers() {
    if (isSingleNumber!) return orderNumber!.toString() +'|' + number.toString();
    String s = '[' + left!.toSnailfishStringWithOrderNumbers() + ',' + right!.toSnailfishStringWithOrderNumbers() + ']';
    return s;
  }

  static bool splitDone = false;

  split() {
    if ( !splitDone ) {
      if (isSingleNumber!) {
        if (number! > 9) {
          // Needs split. Build a new node
          int numberToLeft = (number! / 2).floor();
          SnailfishNumber newLeftNode = SnailfishNumber();
          newLeftNode.isSingleNumber = true;
          newLeftNode.number = numberToLeft;

          int numberToRight = (number! / 2).ceil();
          SnailfishNumber newRightNode = SnailfishNumber();
          newRightNode.isSingleNumber = true;
          newRightNode.number = numberToRight;

          isSingleNumber = false;
          left = newLeftNode;
          right = newRightNode;
          splitDone = true;
        }
      } else {
        left!.split();
        right!.split();
      }
    }
  }

  bool needsSplit() {
    if ( isSingleNumber! ) {
      return  number! > 9;
    } else {
      if ( left!.needsSplit() ) return true;
      if ( right!.needsSplit() ) return true;
      return false;
    }
  }

  bool needsExplode() {
    if (getDepth() > 4) return true;
    return false;
  }

  reduce() {
    bool notFinished = needsSplit() || needsExplode();
    while ( notFinished ) {
      while ( needsExplode()) {
        explode();
      }
      if ( needsSplit()) {
        splitDone = false;
        split();
      }
      notFinished = needsSplit() || needsExplode();
    }
  }

  explode() {
    calcOrderNumbersPrepare();
    calcOrderNumbers();
    SnailfishNumber? nodeToReduce = getNodeAtLevel(5, 0);

    // Add left value to the number to left if it exists
    int? nodeNoAtLeft = nodeToReduce!.left!.orderNumber;
    if ( nodeNoAtLeft! > 0 ) {
      // There are nodes to the left. Add the left number to the node with order number 1 less than this
      SnailfishNumber? nodeToLeft = getNodeWithOrderNumber(nodeNoAtLeft -1);
      nodeToLeft!.number = nodeToLeft.number! + nodeToReduce.left!.number!;
    }

    // Add right value to the number to right if it exists
    int? nodeNoAtRight = nodeToReduce.right!.orderNumber;
    if ( nodeNoAtRight! < maxOrderNo ) {
      SnailfishNumber? nodeToRight = getNodeWithOrderNumber(nodeNoAtRight + 1);
      nodeToRight!.number = nodeToRight.number! + nodeToReduce.right!.number!;
    }

    nodeToReduce.isSingleNumber = true;
    nodeToReduce.number = 0;
    nodeToReduce.left = null;
    nodeToReduce.right = null;
  }

  SnailfishNumber? getNodeAtLevel(int levelToFind, int currentLevel) {
    if ( isSingleNumber!) return null;
    if ( currentLevel == levelToFind - 1 ) {
      return this;
    } else {
      SnailfishNumber? nextNode = left!.getNodeAtLevel(levelToFind, currentLevel+1);
      nextNode ??= right!.getNodeAtLevel(levelToFind, currentLevel+1);
      return nextNode;
    }
  }

  SnailfishNumber? getNodeWithOrderNumber(int orderNoToFind) {
    if ( isSingleNumber! ) {
      if (orderNumber == orderNoToFind) {
        return this;
      } else {
        return null;
      }
    }
    SnailfishNumber? nodeToFind = left!.getNodeWithOrderNumber(orderNoToFind);
    nodeToFind ??= right!.getNodeWithOrderNumber(orderNoToFind);
    return nodeToFind;
  }


}

bool isDigit(String char) {
    final digitRegex = RegExp(r'\d');
    if ( digitRegex.hasMatch(char) ) {
      return true;
    }
    return false;
}

class TokenProvider {
  String tokenStr;

  TokenProvider(this.tokenStr);

  String getToken() {
    String nextChar = getNextChar();
    if ( '[],'.contains(nextChar) ) return nextChar;

    String s = nextChar;
    while ( nextIsDigit() ) {
      s += getNextChar();
    }
    return s;
  }

  bool nextIsDigit() {
    final digitRegex = RegExp(r'\d');
    if ( digitRegex.hasMatch(tokenStr[0])) {
      return true;
    }
    return false;
  }

  bool hasTokens() {
    return tokenStr.isNotEmpty;
  }

  String getNextChar() {
    String s = tokenStr[0];
    tokenStr = tokenStr.substring(1);
    return s;
  }
}

String exampleInputText ='''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]''';

String inputText = '''[3,[5,[7,[3,9]]]]
[[[[7,0],0],[2,[2,8]]],[[[7,8],1],3]]
[[[[2,7],0],7],4]
[[2,1],[9,0]]
[[[[7,1],[3,2]],[[9,8],5]],[2,7]]
[[[8,9],[[8,7],0]],[[[8,7],[6,3]],[[1,7],[8,9]]]]
[[8,6],[[9,[1,7]],[6,[3,9]]]]
[[2,[[5,6],6]],[[4,[5,9]],[3,[4,5]]]]
[[[[2,0],[1,1]],[6,6]],[[1,9],[[2,7],[6,8]]]]
[[[4,6],[[6,3],[3,9]]],[[[2,6],[6,1]],[[9,9],[1,5]]]]
[[[4,[3,1]],3],6]
[[0,[[5,2],8]],[1,[9,[4,3]]]]
[[[[8,6],[2,1]],[2,[8,6]]],[[[7,1],[3,9]],0]]
[[[[4,7],[2,7]],[[8,9],2]],[[[2,4],[7,2]],[3,7]]]
[[5,[2,2]],[[1,6],[[9,1],[5,0]]]]
[[5,[[1,2],[6,4]]],[6,8]]
[[[5,[1,7]],7],[7,[8,1]]]
[[1,9],[[0,3],[[6,7],[2,4]]]]
[1,[7,[[0,6],0]]]
[[[[5,7],9],[[3,2],7]],[[5,1],[9,9]]]
[[[[0,4],[9,6]],[[8,3],[7,4]]],[7,[6,2]]]
[[[[1,6],0],[[8,0],[3,4]]],[[3,[0,3]],4]]
[4,[[7,8],[4,[9,7]]]]
[[[2,[3,7]],5],[0,[9,9]]]
[[[2,0],[[5,8],[7,6]]],[[9,[6,2]],[3,2]]]
[[[3,1],3],[[[3,7],6],[9,8]]]
[[7,[[2,5],5]],[5,[3,[4,5]]]]
[[[6,7],6],[2,[[9,3],9]]]
[[[[5,6],7],[[3,2],5]],[[9,[4,3]],[3,8]]]
[0,7]
[[[4,6],[2,9]],[[[7,6],[5,1]],7]]
[[0,5],[[1,[4,1]],[[7,3],9]]]
[[[2,[3,8]],5],[[[5,9],8],[7,0]]]
[[[6,[8,6]],[[3,6],7]],[[2,1],[6,[7,5]]]]
[[2,[[6,3],[8,9]]],[[[5,6],4],[[7,0],1]]]
[[[[7,1],[5,6]],8],[[[8,9],4],[8,3]]]
[[[9,2],[1,0]],0]
[[5,[5,[8,5]]],4]
[[3,[5,[4,9]]],3]
[[8,[[7,7],6]],5]
[[4,[[5,1],1]],[1,[1,[9,8]]]]
[[[7,[3,6]],[[2,8],[4,7]]],[[[8,8],[4,0]],[2,4]]]
[[[[3,6],3],[0,9]],2]
[[2,8],[[8,[8,6]],[[1,1],[4,5]]]]
[[2,[1,[1,0]]],[[[6,2],[7,4]],[[7,1],6]]]
[3,[8,[7,[8,6]]]]
[[1,0],[[[0,4],[0,5]],[1,5]]]
[[[[5,0],4],[[7,8],[8,8]]],[[1,7],0]]
[1,[[[4,1],7],[6,[9,0]]]]
[[[1,8],2],[[5,5],[8,5]]]
[[4,[9,[0,6]]],[[[8,9],[4,5]],4]]
[[[[5,4],[1,7]],[[3,1],[7,9]]],[[[0,8],[4,7]],[[5,9],6]]]
[[[[8,0],9],4],[[7,[1,3]],5]]
[[[[5,0],6],[[6,1],8]],[[9,1],7]]
[[9,[6,[8,8]]],[7,[[7,1],6]]]
[[[5,[1,5]],[3,[4,2]]],[[[5,2],7],[[6,9],[2,8]]]]
[[[5,[5,5]],[5,7]],[4,[[2,9],7]]]
[[[[0,4],0],[[0,6],[3,0]]],[0,[[8,1],2]]]
[[[7,[4,6]],[[7,2],[4,6]]],[[[9,3],[4,9]],6]]
[[6,7],7]
[[[4,1],[8,[1,5]]],[[4,6],0]]
[[[4,[5,5]],5],[[0,[2,7]],[1,1]]]
[[[[0,1],3],[6,7]],[4,7]]
[[4,[6,4]],[[[9,8],1],[9,3]]]
[[[4,9],0],[[[7,0],[0,9]],[1,[1,0]]]]
[[[7,9],[[9,5],[6,9]]],[[0,[3,0]],[0,[5,9]]]]
[9,[[0,0],[[1,9],9]]]
[[[5,[0,5]],[[9,8],[9,5]]],[[0,[2,5]],7]]
[[[[5,8],6],9],[[[2,7],7],[[7,8],5]]]
[[8,[[4,7],6]],2]
[[[[7,1],[9,0]],[9,[1,7]]],[[8,[6,7]],[2,5]]]
[[4,[2,9]],8]
[[[[7,6],[5,3]],[5,[9,7]]],[[6,[8,1]],[[6,4],9]]]
[[7,[[7,8],4]],[[1,3],[4,[9,7]]]]
[[[6,[6,7]],[[2,8],3]],[7,[6,[0,3]]]]
[[9,8],[[0,[4,8]],[[9,1],1]]]
[[[[4,0],[5,9]],7],[6,[[5,9],[9,6]]]]
[[8,1],[1,[9,[8,3]]]]
[[[1,[5,1]],[6,7]],[[5,9],[2,[6,7]]]]
[[[3,7],[[7,8],1]],[[0,[6,3]],[8,0]]]
[[5,[[9,3],[1,2]]],7]
[[[1,[9,9]],3],[[6,4],[4,1]]]
[[6,[1,[3,6]]],[2,9]]
[[2,[0,2]],[5,[[9,4],[5,0]]]]
[[4,[[3,1],[7,0]]],[[9,1],[[5,5],[6,7]]]]
[[3,[[7,1],[3,4]]],[7,[9,[9,4]]]]
[[9,9],[[5,4],[[9,7],4]]]
[[[5,1],8],[[6,7],9]]
[[[0,[9,5]],[4,3]],[3,2]]
[[[6,[4,1]],[[8,7],[5,3]]],[[[1,2],5],[[9,2],5]]]
[[[[7,4],[9,0]],[[1,8],[2,9]]],[[5,[1,9]],[4,0]]]
[[[4,[3,8]],[[3,3],[2,8]]],[[[1,3],9],[[8,5],6]]]
[[[[6,4],[7,9]],[[7,6],8]],[7,[9,8]]]
[[7,[3,5]],7]
[[[[5,0],[2,3]],[3,7]],[[4,[6,3]],[7,[4,4]]]]
[[6,[3,[7,6]]],[[[5,8],[8,1]],[3,[1,5]]]]
[[8,[9,[5,2]]],2]
[[1,[5,4]],[[7,[8,0]],8]]
[[[[2,7],4],3],[[1,4],[8,4]]]
[3,[9,2]]''';

