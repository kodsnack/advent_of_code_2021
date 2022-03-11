import 'package:collection/collection.dart';
import 'package:flutter/material.dart';

class Day6 extends StatelessWidget {
  const Day6({Key? key}) : super(key: key);
  static String routeName = 'day6';
  final bool isExample = false;
  static String dayTitle = 'Day 6 Lanternfish';

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
            SelectableText('Svar dag 6 del 1: $resultPart1'),
            SelectableText('Svar dag 6 del 2 : $resultPart2'),
          ],
        ),
      ),
    );
  }

  int doPart1() {
    List<int> lanternFishList = getInput(isExample);
    int numberOfDays = 18;
    for ( int dayNo = 0; dayNo < numberOfDays; dayNo++) {
      List<int> fishToAdd = [];
      for ( int fishNo = 0; fishNo < lanternFishList.length ; fishNo++ ) {
        lanternFishList[fishNo]--;
        if ( lanternFishList[fishNo] < 0) {
          lanternFishList[fishNo] = 6;
          fishToAdd.add(8);
        }
      }
      lanternFishList.addAll(fishToAdd);
    }

    return lanternFishList.length;
  }

  int doPart2() {
    final inputList = getInput(isExample);
    int noOfTimerSlots = 9;
    List<int> fishList = List.filled(noOfTimerSlots, 0);
    for (int fishTimer in inputList) {
      fishList[fishTimer]++;
    }
    int noOfDays = 256;
    for ( int day = 0; day < noOfDays; day++) {
      //Handle fish in first slot
      int noOfFishToReset = fishList[0];
      for (int slot = 1; slot < noOfTimerSlots; slot++) {
        fishList[slot-1] = fishList[slot];
      }
      //Reset slot 0 fishes to slot 6
      fishList[6] += noOfFishToReset;
      // And spawn new fish in slot 8
      fishList[8] = noOfFishToReset;
    }
    int totalNoOfFish = fishList.sum;
    return totalNoOfFish;
  }

}


List<int> getInput(bool example) {
  late String text;
  if (example) {
    text = exampleInputText;
  } else {
    text = inputText;
  }
  List<String> sList = text.split(',');
  List<int> iList = [];
  for (String s in sList ) {
    iList.add(int.parse(s));
  }
  return iList;
}

String exampleInputText = '3,4,3,1,2';

String inputText = '3,4,1,2,1,2,5,1,2,1,5,4,3,2,5,1,5,1,2,2,2,3,4,5,2,5,1,3,3,1,3,4,1,5,3,2,2,1,3,2,5,1,1,4,1,4,5,1,3,1,1,5,3,1,1,4,2,2,5,1,5,5,1,5,4,1,5,3,5,1,1,4,1,2,2,1,1,1,4,2,1,3,1,1,4,5,1,1,1,1,1,5,1,1,4,1,1,1,1,2,1,4,2,1,2,4,1,3,1,2,3,2,4,1,1,5,1,1,1,2,5,5,1,1,4,1,2,2,3,5,1,4,5,4,1,3,1,4,1,4,3,2,4,3,2,4,5,1,4,5,2,1,1,1,1,1,3,1,5,1,3,1,1,2,1,4,1,3,1,5,2,4,2,1,1,1,2,1,1,4,1,1,1,1,1,5,4,1,3,3,5,3,2,5,5,2,1,5,2,4,4,1,5,2,3,1,5,3,4,1,5,1,5,3,1,1,1,4,4,5,1,1,1,3,1,4,5,1,2,3,1,3,2,3,1,3,5,4,3,1,3,4,3,1,2,1,1,3,1,1,3,1,1,4,1,2,1,2,5,1,1,3,5,3,3,3,1,1,1,1,1,5,3,3,1,1,3,4,1,1,4,1,1,2,4,4,1,1,3,1,3,2,2,1,2,5,3,3,1,1';
