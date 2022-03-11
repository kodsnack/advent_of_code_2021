import 'package:flutter/material.dart';

import 'day1.dart';
import 'day10.dart';
import 'day11.dart';
import 'day12.dart';
import 'day13.dart';
import 'day14.dart';
import 'day15.dart';
import 'day16.dart';
import 'day17.dart';
import 'day18.dart';
import 'day19.dart';
import 'day2.dart';
import 'day20.dart';
import 'day21.dart';
import 'day22.dart';
import 'day23.dart';
import 'day24.dart';
import 'day25.dart';
import 'day3.dart';
import 'day4.dart';
import 'day5.dart';
import 'day6.dart';
import 'day7.dart';
import 'day8.dart';
import 'day9.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      routes: {
        '/': (context) => const MyHomePage(title: 'Advent of code 2021'),
        Day1.routeName: (context) => const Day1(),
        Day2.routeName: (context) => const Day2(),
        Day3.routeName: (context) => const Day3(),
        Day4.routeName: (context) => const Day4(),
        Day5.routeName: (context) => const Day5(),
        Day6.routeName: (context) => const Day6(),
        Day7.routeName: (context) => const Day7(),
        Day8.routeName: (context) => const Day8(),
        Day9.routeName: (context) => const Day9(),
        Day10.routeName: (context) => Day10(),
        Day11.routeName: (context) => const Day11(),
        Day12.routeName: (context) => const Day12(),
        Day13.routeName: (context) => const Day13(),
        Day14.routeName: (context) => const Day14(),
        Day15.routeName: (context) => const Day15(),
        Day16.routeName: (context) => Day16(),
        Day17.routeName: (context) => const Day17(),
        Day18.routeName: (context) => const Day18(),
        Day19.routeName: (context) => Day19(),
        Day20.routeName: (context) => const Day20(),
        Day21.routeName: (context) => const Day21(),
        Day22.routeName: (context) => const Day22(),
        Day23.routeName: (context) => const Day23(),
        Day24.routeName: (context) => const Day24(),
        Day25.routeName: (context) => const Day25(),
      },
    );
  }
}

class MyHomePage extends StatelessWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
      ),
      body: SingleChildScrollView(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              DayButton(
                titleText: 'Day 1 - Sonar Sweep',
                routeName:  Day1.routeName,
              ),
              DayButton(
                titleText: 'Day 2 - Dive!',
                routeName:  Day2.routeName,
              ),
              DayButton(
                titleText: 'Day 3 Binary Diagnostic',
                routeName: Day3.routeName,
              ),
              DayButton(
                titleText: 'Day 4 Giant Squid',
                routeName: Day4.routeName,
              ),
              DayButton(
                titleText: Day5.dayTitle,
                routeName: Day5.routeName,
              ),
              DayButton(
                titleText: Day6.dayTitle,
                routeName: Day6.routeName,
              ),
              DayButton(
                titleText: Day7.dayTitle,
                routeName: Day7.routeName,
              ),
              DayButton(
                titleText: Day8.dayTitle,
                routeName: Day8.routeName,
              ),
              DayButton(
                titleText: Day9.dayTitle,
                routeName: Day9.routeName,
              ),
              const DayButton(
                titleText: Day10.dayTitle,
                routeName: Day10.routeName,
              ),
              DayButton(
                titleText: Day11.dayTitle,
                routeName: Day11.routeName,
              ),
              DayButton(
                titleText: Day12.dayTitle,
                routeName: Day12.routeName,
              ),
              DayButton(
                titleText: Day13.dayTitle,
                routeName: Day13.routeName,
              ),
              DayButton(
                titleText: Day14.dayTitle,
                routeName: Day14.routeName,
              ),
              DayButton(
                titleText: Day15.dayTitle,
                routeName: Day15.routeName,
              ),
              DayButton(
                titleText: Day16.dayTitle,
                routeName: Day16.routeName,
              ),
              const DayButton(
                titleText: Day17.dayTitle,
                routeName: Day17.routeName,
              ),
              const DayButton(
                titleText: Day18.dayTitle,
                routeName: Day18.routeName,
              ),
              const DayButton(
                titleText: Day19.dayTitle,
                routeName: Day19.routeName,
              ),
              const DayButton(
                titleText: Day20.dayTitle,
                routeName: Day20.routeName,
              ),
              const DayButton(
                titleText: Day21.dayTitle,
                routeName: Day21.routeName,
              ),
              const DayButton(
                titleText: Day22.dayTitle,
                routeName: Day22.routeName,
              ),
              const DayButton(
                titleText: Day23.dayTitle,
                routeName: Day23.routeName,
              ),
              const DayButton(
                titleText: Day24.dayTitle,
                routeName: Day24.routeName,
              ),
              const DayButton(
                titleText: Day25.dayTitle,
                routeName: Day25.routeName,
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class DayButton extends StatelessWidget {
  const DayButton({
    Key? key,
    required this.titleText,
    required this.routeName,
  }) : super(key: key);

  final String titleText;
  final String routeName;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(4.0),
      child: MaterialButton(
        child: Text(titleText),
        color: Colors.lightBlueAccent,
        onPressed: () => Navigator.pushNamed(context, routeName),
      ),
    );
  }
}
