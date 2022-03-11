import 'package:advent_of_code/day18.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  String testString1 = '[[1,2],[[3,4],5]]';

  test('TokenProvider', () {
    TokenProvider tokenProvider = TokenProvider(testString1);
    expect(tokenProvider.getToken(), '[');
    expect(tokenProvider.getToken(), '[');
    expect(tokenProvider.getToken(), '1');
  });

  test('Snailfish pair', () {
    TokenProvider tokenProvider = TokenProvider('[1,2]');
    final pair = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(pair!.isSingleNumber, false);
    expect(pair.left!.getValue(), 1);
    expect(pair.right!.getValue(), 2);
  });

  test('Snailfish 2 levels', () {
    TokenProvider tokenProvider = TokenProvider('[1,[2,3]]');
    final sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.isSingleNumber, false);
    expect(sfn.left!.getValue(), 1);
    expect(sfn.right!.left!.getValue(), 2);
    expect(sfn.right!.right!.getValue(), 3);
  });

  test('Snailfish magnitudes', () {
    TokenProvider tokenProvider = TokenProvider('[[1,2],[[3,4],5]]');
    var sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.getMagnitude(), 143);
    tokenProvider = TokenProvider('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.getMagnitude(), 1384);
    tokenProvider = TokenProvider('[[[[1,1],[2,2]],[3,3]],[4,4]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.getMagnitude(), 445);
    tokenProvider =
        TokenProvider('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.getMagnitude(), 3488);
  });

  test('Snailfish depths', () {
    TokenProvider tokenProvider = TokenProvider('[[1,2],[[3,4],5]]');
    var sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.getDepth(), 3);
    tokenProvider = TokenProvider('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.getDepth(), 4);
    tokenProvider = TokenProvider('[[[[1,1],[2,2]],[3,3]],[4,4]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.getDepth(), 4);
    tokenProvider = TokenProvider('[[[8,6],[7,7]],5]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.getDepth(), 3);
  });

  test('Snailfish strings', () {
    String s = '[1,2]';
    TokenProvider tokenProvider = TokenProvider(s);
    var sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.toSnailfishString(), s);

    s = '[[[[1,1],[2,2]],[3,3]],[4,4]]';
    tokenProvider = TokenProvider(s);
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.toSnailfishString(), s);

    s = '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]';
    tokenProvider = TokenProvider(s);
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.toSnailfishString(), s);
  });

  test('Snailfish addition', () {
    TokenProvider tokenProvider1 = TokenProvider('[1,2]');
    TokenProvider tokenProvider2 = TokenProvider('[[3,4],5]');
    var sfn1 = SnailfishNumber.fromTokenProvider(tokenProvider1);
    var sfn2 = SnailfishNumber.fromTokenProvider(tokenProvider2);
    var sfn3 = sfn1!.add(sfn2);
    expect(sfn3.toSnailfishString(), '[[1,2],[[3,4],5]]');
  });

  test('Snailfish getLeft and getRight', () {
    TokenProvider tokenProvider1 = TokenProvider('[1,2]');
    TokenProvider tokenProvider2 = TokenProvider('[[3,4],5]');
    TokenProvider tokenProvider3 = TokenProvider('[1,[3,4]]');
    var sfn1 = SnailfishNumber.fromTokenProvider(tokenProvider1);
    var sfn2 = SnailfishNumber.fromTokenProvider(tokenProvider2);
    var sfn3 = SnailfishNumber.fromTokenProvider(tokenProvider3);
    expect(sfn1!.getLeftAtLevel(1, 0), 1);
    expect(sfn2!.getLeftAtLevel(2, 0), 3);
    expect(sfn3!.getLeftAtLevel(2, 0), 3);
    expect(sfn1.getRightAtLevel(1, 0), 2);
    expect(sfn2.getRightAtLevel(2, 0), 4);
    expect(sfn3.getRightAtLevel(2, 0), 4);
  });

  test('Snailfish order numbering', () {
    TokenProvider tokenProvider = TokenProvider('[1,[2,3]]');
    var sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    sfn!.calcOrderNumbersPrepare();
    sfn.calcOrderNumbers();
    String s = sfn.toSnailfishStringWithOrderNumbers();
    expect(s, '[0|1,[1|2,2|3]]');
    sfn = sfn.getNodeWithOrderNumber(2);
    expect(sfn!.number!, 3);

    tokenProvider =
        TokenProvider('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    sfn!.calcOrderNumbersPrepare();
    sfn.calcOrderNumbers();
    s = sfn.toSnailfishStringWithOrderNumbers();
    expect(s,
        '[[[[0|8,1|7],[2|7,3|7]],[[4|8,5|6],[6|7,7|7]]],[[[8|0,9|7],[10|6,11|6]],[12|8,13|7]]]');
    sfn = sfn.getNodeWithOrderNumber(12);
    expect(sfn!.number!, 8);
  });

  test('Snailfish needsReduce', () {
    TokenProvider tokenProvider = TokenProvider('[1,[2,[3,[4,5]]]]');
    var sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.needsExplode(), false);
    tokenProvider = TokenProvider('[1,[2,[3,[4,[5,6]]]]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.needsExplode(), true);
  });

  test('Snailfish explode', () {
    var tokenProvider = TokenProvider('[[[[[1,2],3],4],5],6]');
    var sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.needsExplode(), true);
    var nodeToReduce = sfn.getNodeAtLevel(5, 0);
    expect(nodeToReduce!.toSnailfishString(), '[1,2]');
    sfn.explode();
    var s = sfn.toSnailfishString();
    expect(s, '[[[[0,5],4],5],6]');

    tokenProvider = TokenProvider('[1,[2,[3,[4,[5,6]]]]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.needsExplode(), true);
    nodeToReduce = sfn.getNodeAtLevel(5, 0);
    expect(nodeToReduce!.toSnailfishString(), '[5,6]');
    sfn.explode();
    s = sfn.toSnailfishString();
    expect(s, '[1,[2,[3,[9,0]]]]');

    tokenProvider = TokenProvider('[1,[2,[[[3,4],5],6]]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.needsExplode(), true);
    nodeToReduce = sfn.getNodeAtLevel(5, 0);
    expect(nodeToReduce!.toSnailfishString(), '[3,4]');
    sfn.explode();
    s = sfn.toSnailfishString();
    expect(s, '[1,[5,[[0,9],6]]]');

    tokenProvider = TokenProvider('[7,[6,[5,[4,[3,2]]]]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.needsExplode(), true);
    nodeToReduce = sfn.getNodeAtLevel(5, 0);
    expect(nodeToReduce!.toSnailfishString(), '[3,2]');
    sfn.explode();
    s = sfn.toSnailfishString();
    expect(s, '[7,[6,[5,[7,0]]]]');
  });

  test('Snailfish split', () {
    var tokenProvider = TokenProvider('[[[[11,3],4],5],6]');
    var sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.needsSplit(), true);
    SnailfishNumber.splitDone = false;
    sfn.split();
    expect(sfn.toSnailfishString(), '[[[[[5,6],3],4],5],6]');

    tokenProvider = TokenProvider('[1,[2,[3,[4,11]]]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.needsSplit(), true);
    SnailfishNumber.splitDone = false;
    sfn.split();
    expect(sfn.toSnailfishString(), '[1,[2,[3,[4,[5,6]]]]]');

    tokenProvider = TokenProvider('[1,[2,[[[3,4],5],6]]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    expect(sfn!.needsSplit(), false);
    SnailfishNumber.splitDone = false;
    sfn.split();
    expect(sfn.toSnailfishString(), '[1,[2,[[[3,4],5],6]]]');
  });

  test('Snailfish reduce', () {
    var tokenProvider = TokenProvider('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]');
    var sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    sfn!.reduce();
    expect(sfn.toSnailfishString(), '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]');

    tokenProvider = TokenProvider(
        '[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]');
    sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
    sfn!.reduce();
    expect(sfn.toSnailfishString(),
        '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]');
  });

  test('Snailfish addition with reduce', () {
    var tokenProvider1 = TokenProvider('[[[[4,3],4],4],[7,[[8,4],9]]]');
    var sfn1 = SnailfishNumber.fromTokenProvider(tokenProvider1);
    var tokenProvider2 = TokenProvider('[1,1]');
    var sfn2 = SnailfishNumber.fromTokenProvider(tokenProvider2);
    sfn1 = sfn1!.add(sfn2!);
    sfn1.reduce();
    expect(sfn1.toSnailfishString(), '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]');
  });

  test('Snailfish addition with reduce', () {
    List<String> stringList = [
      '[1,1]',
      '[2,2]',
      '[3,3]',
      '[4,4]',
      '[5,5]',
    ];

    bool first = true;
    SnailfishNumber? sfn;
    for (String s in stringList) {
      final tokenProvider = TokenProvider(s);
      if (first) {
        sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
        first = false;
      } else {
        final sfn2 = SnailfishNumber.fromTokenProvider(tokenProvider);
        sfn = sfn!.add(sfn2);
        sfn.reduce();
      }
    }
    sfn!.reduce();
    expect(sfn.toSnailfishString(), '[[[[3,0],[5,3]],[4,4]],[5,5]]');
  });

  test('Snailfish addition with reduce', () {
    List<String> stringList = [
      '[1,1]',
      '[2,2]',
      '[3,3]',
      '[4,4]',
      '[5,5]',
      '[6,6]',
    ];

    bool first = true;
    SnailfishNumber? sfn;
    for (String s in stringList) {
      final tokenProvider = TokenProvider(s);
      if (first) {
        sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
        first = false;
      } else {
        final sfn2 = SnailfishNumber.fromTokenProvider(tokenProvider);
        sfn = sfn!.add(sfn2);
        sfn.reduce();
      }
    }
    sfn!.reduce();
    expect(sfn.toSnailfishString(), '[[[[5,0],[7,4]],[5,5]],[6,6]]');
  });


  test('Snailfish addition with reduce', () {
    List<String> stringList = [
      '[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]',
      '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]',
      '[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]',
      '[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]',
      '[7,[5,[[3,8],[1,4]]]]',
      '[[2,[2,2]],[8,[8,1]]]',
      '[2,9]',
      '[1,[[[9,3],9],[[9,0],[0,7]]]]',
      '[[[5,[7,4]],7],1]',
      '[[[[4,2],2],6],[8,7]]',
    ];

    bool first = true;
    SnailfishNumber? sfn;
    for (String s in stringList) {
      final tokenProvider = TokenProvider(s);
      if (first) {
        sfn = SnailfishNumber.fromTokenProvider(tokenProvider);
        first = false;
      } else {
        final sfn2 = SnailfishNumber.fromTokenProvider(tokenProvider);
        sfn = sfn!.add(sfn2);
        sfn.reduce();
      }
    }
    sfn!.reduce();
    expect(sfn.toSnailfishString(),
        '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]');
  });
}
