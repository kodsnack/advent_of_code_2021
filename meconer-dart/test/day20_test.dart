import 'package:advent_of_code/day20.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  String testInput =
      '''..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###''';

  test('Get input', () {
    final trench = TrenchMap.fromInputString(testInput);
    expect(trench.enhAlgorithmString.length, 512);
    expect(trench.image.imageLines.length, 5);
    trench.image.expand();
    expect(trench.image.imageLines.length, 7);
    expect(trench.image.imageLines[0].length, 7);
    trench.image.print();
  });

  test('Enhance pixel', () {
    String pixels = '...#...#.';
    final trenchMap = TrenchMap.fromInputString(testInput);

    final result =
        TrenchImage.enhancePixel(pixels, trenchMap.enhAlgorithmString);
    expect(result, '#');
  });

  test('Pixel count', () {
    final trenchMap = TrenchMap.fromInputString(testInput);
    int count = trenchMap.image.countBrightPixels();
    expect(count, 10);
  });

  test('Enhance image', () {
    final trenchMap = TrenchMap.fromInputString(testInput);
    trenchMap.enhanceImage();
    trenchMap.enhanceImage();
    trenchMap.image.print();
    int count = trenchMap.image.countBrightPixels();
    expect(count, 35);

  });
}
