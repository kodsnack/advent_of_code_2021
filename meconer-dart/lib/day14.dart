import 'package:flutter/material.dart';


class Day14 extends StatelessWidget {
  const Day14({Key? key}) : super(key: key);
  static String routeName = 'day14';
  final bool isExample = false;
  static String dayTitle = 'Day 14: Extended Polymerization';

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
            SelectableText('Svar dag 14 del 1: $resultPart1'),
            SelectableText('Svar dag 14 del 2 : $resultPart2'),
          ],
        ),
      ),
    );
  }



  int doPart1() {
    final lines = getInput(isExample);
    var polymer = lines[0];
    final insertionRuleStrings = lines.sublist(2);
    Map<String,String> insertionRules = {};
    for (final rule in insertionRuleStrings) {
      final rulePair = rule.split(' -> ');
      insertionRules[rulePair[0]] = rulePair[1];
    }
    const noOfSteps = 10;
    for ( int step = 0 ; step < noOfSteps ; step++ ) {
      polymer = doStep(polymer, insertionRules);
    }
    final occurrencesList = countLetters(polymer);
    final largestCount = findLargest(occurrencesList);
    final smallestCount = findSmallest(occurrencesList);
    return largestCount - smallestCount;
  }

  int doPart2() {
    final lines = getInput(isExample);
    var polymer = lines[0];
    final lastLetter = polymer.substring(polymer.length-1);
    final insertionRuleStrings = lines.sublist(2);
    Map<String,String> insertionRules = {};
    for (final rule in insertionRuleStrings) {
      final rulePair = rule.split(' -> ');
      insertionRules[rulePair[0]] = rulePair[1];
    }
    const noOfSteps = 40;
    Pairs pairs = Pairs.fromString(polymer);

    for ( int step = 0 ; step < noOfSteps ; step++ ) {
      pairs.doStep(insertionRules);
    }
    final occurrencesList = pairs.countLetters(lastLetter);
    final largestCount = findLargest(occurrencesList);
    final smallestCount = findSmallest(occurrencesList);
    return largestCount - smallestCount;
  }


  String doStep(String polymer, Map<String,String> rules ) {
    String newPolymer = '';

    for ( int i = 0 ; i < polymer.length - 1; i++ ) {
      String pair = polymer.substring(i, i+2);
      String replacement = doRule(pair, rules);
      newPolymer += replacement;
    }
    newPolymer += polymer.substring(polymer.length-1);
    return newPolymer;
  }

  String doRule(String pair, Map<String, String> rules) {
    if (rules.containsKey(pair)) {
      return pair.substring(0,1) + rules[pair]!;
    }
    return pair;
  }

  void doStepPart2( Map<String, String> insertionRules, Pairs pairs) {

  }

  List<String> getInput(bool example) {
      if (example) {
        return exampleInputText.split('\n');
      } else {
        return inputText.split('\n');
      }
  }

  Map<String, int> countLetters(String s) {
    Map<String, int> counts = {};
    for (String char in s.split('')) {
      if (counts.containsKey(char)) {
        int count = counts[char]!;
        count++;
        counts[char] = count;
      } else {
        counts[char] = 1;
      }
    }

    return counts;
  }

  int findLargest(Map<String, int> occurrencesList) {
    int largest = 0 ;
    for ( final occ in occurrencesList.values) {
      if (occ > largest ) largest = occ;
    }
    return largest;
  }

  int findSmallest(Map<String, int> occurrencesList) {
    int smallest = 9999999999999 ;
    for ( final occ in occurrencesList.values) {
      if (occ < smallest ) smallest = occ;
    }
    return smallest;
  }

}

class Pairs {
  Map<String, int> pairCounter = {};

  Pairs.fromString(String polymer) {
    for ( int i = 0 ; i < polymer.length - 1; i++ ) {
      String pair = polymer.substring(i, i+2);
      increment(pair,1);
    }
  }

  void doStep(Map<String, String> rules) {
    final oldPairCounter = {...pairCounter};
    for ( final key in oldPairCounter.keys ) {
      int pairCount = oldPairCounter[key]!;
      String result = doRule( key, rules);
      if (result.length == 3) {
        // In rule set. Result is 3 chars long and 2 pairs
        String leftPair = result.substring(0,2);
        String rightPair = result.substring(1,3);
        increment(leftPair, pairCount);
        increment(rightPair, pairCount);
        // And the original pair is removed so we have to decrement it
        decrement(key, pairCount);
      }
    }
  }

  String doRule(String pair, Map<String, String> rules) {
    if (rules.containsKey(pair)) {
      return pair.substring(0,1) + rules[pair]! + pair.substring(1,2);
    }
    return pair;
  }

  void increment(String pair, int pairCount) {
    if (pairCounter.containsKey(pair)) {
      int count = pairCounter[pair]!;
      count += pairCount;
      pairCounter[pair] = count;
    } else {
      pairCounter[pair] = pairCount;
    }
  }

  void decrement(String pair, int pairCount) {
    if (pairCounter.containsKey(pair)) {
      int count = pairCounter[pair]!;
      count -= pairCount;
      if ( count == 0) {
        pairCounter.remove(pair);
      } else if (count > 0 ){
        pairCounter[pair] = count;
      } else {
        throw UnsupportedError('Wtf?');
      }
    } else {
      throw UnsupportedError('Very strange');
    }
  }

  Map<String, int> countLetters(String lastLetter) {
      Map<String, int> counts = {};
      for ( final key in pairCounter.keys) {
        countLetter( counts, key[0], pairCounter[key]!);
      }
      // Add 1 to the last letter in polymer. It will always be the same as the start polymer and wont be counted elsewhere
      countLetter(counts, lastLetter, 1);
      return counts;
    }

  void countLetter(Map<String, int> counts, String letter, int letterCount) {
    if (counts.containsKey(letter)) {
      int count = counts[letter]!;
      count += letterCount;
      counts[letter] = count;
    } else {
      counts[letter] = letterCount;
    }
  }
}

String exampleInputText =
'''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C''';

String inputText =
'''KKOSPHCNOCHHHSPOBKVF

NV -> S
OK -> K
SO -> N
FN -> F
NB -> K
BV -> K
PN -> V
KC -> C
HF -> N
CK -> S
VP -> H
SK -> C
NO -> F
PB -> O
PF -> P
VC -> C
OB -> S
VF -> F
BP -> P
HO -> O
FF -> S
NF -> B
KK -> C
OC -> P
OV -> B
NK -> B
KO -> C
OH -> F
CV -> F
CH -> K
SC -> O
BN -> B
HS -> O
VK -> V
PV -> S
BO -> F
OO -> S
KB -> N
NS -> S
BF -> N
SH -> F
SB -> S
PP -> F
KN -> H
BB -> C
SS -> V
HP -> O
PK -> P
HK -> O
FH -> O
BC -> N
FK -> K
HN -> P
CC -> V
FO -> F
FP -> C
VO -> N
SF -> B
HC -> O
NN -> K
FC -> C
CS -> O
FV -> P
HV -> V
PO -> H
BH -> F
OF -> P
PC -> V
CN -> O
HB -> N
CF -> P
HH -> K
VH -> H
OP -> F
BK -> S
SP -> V
BS -> V
VB -> C
NH -> H
SN -> K
KH -> F
OS -> N
NP -> P
VN -> V
KV -> F
KP -> B
VS -> F
NC -> F
ON -> S
FB -> C
SV -> O
PS -> K
KF -> H
CP -> H
FS -> V
VV -> H
CB -> P
PH -> N
CO -> N
KS -> K''';
