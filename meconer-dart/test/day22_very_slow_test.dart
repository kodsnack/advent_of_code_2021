import 'package:advent_of_code/day22_very_slow.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  String testInput = '''on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10''';

  test('Get input', () {
    final command = Command.fromInputLine(testInput.split('\n')[0]);

    expect(command.turnOn, true);
    expect(command.xMax, 12);
  });

  test('Create cubes', () {
    CubeSpace cubes = CubeSpace();
    for (String line in testInput.split('\n')) {
      Command command = Command.fromInputLine(line);
      Cube cube = Cube.fromCommand(command);
      cubes.cubeList.add(cube);
    }
    expect(cubes.cubeList.length, 4);
  });

  test('Cube calc', () {
    String testInput = '''on x=10..20,y=10..20,z=10..20
on x=15..25,y=15..25,z=15..25
off x=5..12,y=5..12,z=5..12''';

    CubeSpace cubes = CubeSpace();
    for (String line in testInput.split('\n')) {
      Command command = Command.fromInputLine(line);
      Cube cube = Cube.fromCommand(command);
      cubes.cubeList.add(cube);
    }
    expect(cubes.cubeList.length, 3);
    expect(cubes.cubeList[0].interSect(cubes.cubeList[1]), true);
    expect(cubes.cubeList[0].interSect(cubes.cubeList[2]), true);
    expect(cubes.cubeList[1].interSect(cubes.cubeList[2]), false);
  });

  test('Cube split', () {
    String testInput = '''on x=10..20,y=10..20,z=10..20
on x=15..25,y=15..25,z=15..25''';

    CubeSpace cubes = CubeSpace();
    for (String line in testInput.split('\n')) {
      Command command = Command.fromInputLine(line);
      //command.print();
      Cube cube = Cube.fromCommand(command);
      cubes.cubeList.add(cube);
    }
    final cube1Split = CubeSpace.split(cubes.cubeList.first, cubes.cubeList[1]);
    expect(cube1Split.length, 8);
    for ( Cube cube in cube1Split) {
      cube.print();
    }
  });

  test('Cube split and add', () {
    String testInput = '''on x=10..20,y=10..20,z=10..20
on x=15..25,y=15..25,z=15..25''';

    CubeSpace cubes = CubeSpace();
    for (String line in testInput.split('\n')) {
      Command command = Command.fromInputLine(line);
      //command.print();
      Cube cube = Cube.fromCommand(command);
      cubes.cubeList.add(cube);
    }
    final cube1Split = CubeSpace.split(cubes.cubeList.first, cubes.cubeList[1]);
    final cube2Split = CubeSpace.split(cubes.cubeList[1], cubes.cubeList.first);
    expect(cube1Split.length, 8);
    for ( Cube cube in cube1Split) {
      cube.print();
    }
    expect(cube2Split.length, 8);
    for ( Cube cube in cube2Split) {
      cube.print();
    }
  });

  test('Cube split and add containing cube', () {
    String testInput = '''on x=10..30,y=10..30,z=10..30
on x=15..25,y=15..25,z=15..25''';

    CubeSpace cubes = CubeSpace();
    for (String line in testInput.split('\n')) {
      Command command = Command.fromInputLine(line);
      //command.print();
      cubes.handleCommand(command);
    }
    expect(cubes.cubeList.length, 1);
  });

  test('Cube split and remove contained cube', () {
    String testInput = '''on x=10..30,y=10..30,z=10..30
off x=15..25,y=15..25,z=15..25''';

    CubeSpace cubes = CubeSpace();
    for (String line in testInput.split('\n')) {
      Command command = Command.fromInputLine(line);
      //command.print();
      Cube cube = Cube.fromCommand(command);
      cubes.cubeList.add(cube);
    }
    final cube1Split = CubeSpace.split(cubes.cubeList.first, cubes.cubeList[1]);
    final cube2Split = CubeSpace.split(cubes.cubeList[1], cubes.cubeList.first);
    expect(cube1Split.length, 27);
    // for ( Cube cube in cube1Split) {
    //   cube.print();
    // }
    // debugPrint('+');
    expect(cube2Split.length, 1);
    // for ( Cube cube in cube2Split) {
    //   cube.print();
    // }
  });

  test('Handle commands', () {
    CubeSpace cubes = CubeSpace();
    for (String line in testInput.split('\n')) {
      Command command = Command.fromInputLine(line);
      cubes.handleCommand(command);
    }
    for ( Cube cube in cubes.cubeList) {
      cube.print();
    }
    int cellCount = cubes.getVolume();
    expect(cellCount, 39);
  });


  test('Example input', () {
    String testInput = '''on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15''';
    CubeSpace cubes = CubeSpace();
    for (String line in testInput.split('\n')) {
      Command command = Command.fromInputLine(line);
      cubes.handleCommand(command);
    }
    for ( Cube cube in cubes.cubeList) {
      cube.print();
    }
    int cellCount = cubes.getVolume();
    expect(cellCount, 590784);
  });
}
