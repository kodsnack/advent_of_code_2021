import 'dart:math';

import 'package:flutter/material.dart';


class Day17 extends StatelessWidget {
  const Day17({Key? key}) : super(key: key);
  static const String routeName = 'day17';
  final bool isExample = false;
  static const String dayTitle = 'Day 17: Trick Shot';

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
            SelectableText('Svar dag 17 del 1: $resultPart1'),
            SelectableText('Svar dag 17 del 2 : $resultPart2'),
          ],
        ),
      ),
    );
  }

  int doPart1() {
    TargetArea targetArea = TargetArea.fromString(getInput(isExample));
    // To get as high as possible we should aim as far as we can, xMax
    // The starting velocity should then be about sqr(xMax)
    // Lets start with this value -2 and
    int startX = sqrt(targetArea.xMax).round() - 2;
    // Start the y velocity at yMin and try to go upwards until we still hit the target
    int maxHeight = 0;
    for ( int xVel = startX; xVel < startX + 25; xVel++) {
      for ( int yVel =  targetArea.yMin; yVel <100 ; yVel++) {
        Result result = doLaunch(xVel, yVel, targetArea);
        if ( result.hitTarget && result.maxHeight > maxHeight) {
          maxHeight = result.maxHeight;
          debugPrint( 'Hit! Startvelocity : x = $xVel, y = $yVel, Height = $maxHeight');
        } else {
          //debugPrint( 'Miss! Startvelocity : x = $xVel, y = $yVel, stoppoint : ${result.stopX}, ${result.stopY}');
        }
      }
    }
    return maxHeight;
  }

  int doPart2() {
    TargetArea targetArea = TargetArea.fromString(getInput(isExample));
    // To get as many hits as possible we should start the aim as short as possible, xMin
    // and then increase it
    // The starting velocity should then be about sqr(xMax)
    // Lets start with this value -2 and
    int startX = sqrt(targetArea.xMin).round() - 2;
    int endX = targetArea.xMax + 1;
    // Start the y velocity at yMin and try to go upwards until we still hit the target
    int startY = targetArea.yMin;
    int hitCount = 0;
    for ( int xVel = startX; xVel < endX; xVel++) {
      for ( int yVel =  startY; yVel <100 ; yVel++) {
        Result result = doLaunch(xVel, yVel, targetArea);
        if ( result.hitTarget) {
          hitCount++;
          debugPrint( 'Hit! Startvelocity : x = $xVel, y = $yVel');
        } else {
          //debugPrint( 'Miss! Startvelocity : x = $xVel, y = $yVel, stoppoint : ${result.stopX}, ${result.stopY}');
        }
      }
    }
    return hitCount;
  }

  String getInput(bool example) {
    return  isExample ? exampleInputText : inputText;
  }

  Result doLaunch(int xVel, int yVel, TargetArea targetArea) {
    int x = 0;
    int y = 0;
    int maxHeight = 0;
    while (x <= targetArea.xMax && y >= targetArea.yMin) { // Run until we overshoot
      if ( y > maxHeight) maxHeight = y;
      if ( targetArea.isHit(x,y)) {
        return Result(true, maxHeight, x, y);
      }
      x += xVel;
      if ( xVel > 0 ) xVel--;
      if ( xVel < 0 ) xVel++;
      y += yVel;
      yVel -= 1;
    }
    return Result(false, 0, x, y);
  }

}

class Result {
  bool hitTarget;
  int maxHeight;
  int stopX, stopY;

  Result(this.hitTarget, this.maxHeight, this.stopX, this.stopY);
}

class TargetArea {
  late int xMin, xMax, yMin, yMax;

  TargetArea(this.xMin, this.xMax, this.yMin, this.yMax);

  TargetArea.fromString(String input ) {
    String areaString = input.split(':')[1]; // Remove start text and colon
    final area = areaString.split(',');
    xMin = int.parse(area[0].substring(3).split('..')[0]);
    xMax = int.parse(area[0].substring(3).split('..')[1]);
    yMin = int.parse(area[1].substring(3).split('..')[0]);
    yMax = int.parse(area[1].substring(3).split('..')[1]);
  }

  bool isHit(int x, int y) {
    if (x < xMin || x > xMax) return false;
    if (y < yMin || y > yMax) return false;
    return true;
  }


}

String exampleInputText ='target area: x=20..30, y=-10..-5';

String inputText = 'target area: x=209..238, y=-86..-59';
