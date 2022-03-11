import 'package:advent_of_code/day19.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('Vector', () {
    Vector pos = Vector.fromStr('1,2,3');
    expect(pos.x, 1);
    expect(pos.y, 2);
    expect(pos.z, 3);

    pos = Vector.fromStr('5,7,9');
    expect(pos.x, 5);
    expect(pos.y, 7);
    expect(pos.z, 9);
  });

  test('Rotation', () {
    Vector vec = Vector(1, 2, 3);
    var rotated = rotations[1].multiply(vec); // Rotation about z 90 deg
    expect(rotated.x, -2);
    expect(rotated.y, 1);
    expect(rotated.z, 3);
    rotated = rotations[2].multiply(vec); // Rotation about z 180 deg
    expect(rotated.x, -1);
    expect(rotated.y, -2);
    expect(rotated.z, 3);
    rotated = rotations[3].multiply(vec); // Rotation about z 270 deg
    expect(rotated.x, 2);
    expect(rotated.y, -1);
    expect(rotated.z, 3);
  });

  test('Rotation matrixes', () {
    Vector vec = Vector(1, 2, 3);
    List<Vector> rotated = [];
    for (int i = 0; i < rotations.length; i++) {
      rotated.add(rotations[i].multiply(vec)); // Rotation about z 90 deg
    }
    bool allZero = false;
    for (int i = 0; i < rotations.length - 1; i++) {
      for (int j = i + 1; j < rotations.length; j++) {
        final dist = rotated[i].distance(rotated[j]);
        if (dist.x == 0 && dist.y == 0 && dist.z == 0) {
          debugPrint('i = $i ; j = $j');
          allZero = true;
        }
      }
    }
    expect(allZero, false);
  });

  test('Ocean', () {
    Ocean ocean = Ocean.fromInput(exampleInputText.split('\n'));
    expect(ocean.scanners[0].beacons[2].position.y, 591);
    expect(ocean.scanners[4].beacons[25].position.x, 30);

    final refScanner = ocean.scanners[0];

    final scannerToTest = ocean.scanners[1];

    var scannerToTestLocation = refScanner.findCommonLocation(scannerToTest);
    expect(scannerToTestLocation, isNotNull);

    final secondScannerToTest = ocean.scanners[2];
    scannerToTestLocation = refScanner.findCommonLocation(secondScannerToTest);
    expect(scannerToTestLocation, isNull);
  });

  test('Scanning entire ocean', () {
    Ocean ocean = Ocean.fromInput(exampleInputText.split('\n'));
    final refScanner = ocean.scanners[0];
    refScanner.actualLocation = Vector(0,0,0);
    while (ocean.isNotTotallyScanned()) {
      for ( var scanner in ocean.scanners.sublist(1)) {
        if ( scanner.actualLocation == null ) {
          final locationOfScanner = refScanner.findCommonLocation(scanner);
          if (locationOfScanner != null) {
            scanner.actualLocation = locationOfScanner.location;
            scanner.reOrient(locationOfScanner.orientation);
            refScanner.addBeaconsFromOtherScanner( scanner);
          }
        }
      }
    }
    expect(refScanner.beacons.length, 79);

  });

  test('Beacon', () {
    Beacon beacon1 = Beacon(Vector.fromStr('-618,-824,-621'));
    Beacon beacon2 = Beacon(Vector.fromStr('686,422,578'));
    final distance = beacon1.distance(beacon2);
    expect(distance.x, 1304);
    expect(distance.y, 1246);
    expect(distance.z, 1199);
  });
}

String exampleInputText = '''--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14''';
