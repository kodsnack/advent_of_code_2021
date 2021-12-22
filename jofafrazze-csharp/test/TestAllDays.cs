using Xunit;

namespace test
{
    public class Input
    {
        public static readonly string actual = "input.txt";
        public static readonly string example = "example.txt";
    }

    public class TestDay01
    {
        [Fact]
        public void ExampleA() => Assert.Equal(7, aoc.Day01.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(1301, aoc.Day01.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(5, aoc.Day01.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(1346, aoc.Day01.PartB(Input.actual));
    }

    public class TestDay02
    {
        [Fact]
        public void ExampleA() => Assert.Equal(150, aoc.Day02.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(1727835, aoc.Day02.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(900, aoc.Day02.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(1544000595, aoc.Day02.PartB(Input.actual));
    }

    public class TestDay03
    {
        [Fact]
        public void ExampleA() => Assert.Equal(198, aoc.Day03.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(2261546, aoc.Day03.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(230, aoc.Day03.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(6775520, aoc.Day03.PartB(Input.actual));
    }

    public class TestDay04
    {
        [Fact]
        public void ExampleA() => Assert.Equal(4512, aoc.Day04.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(29440, aoc.Day04.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(1924, aoc.Day04.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(13884, aoc.Day04.PartB(Input.actual));
    }

    public class TestDay05
    {
        [Fact]
        public void ExampleA() => Assert.Equal(5, aoc.Day05.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(6113, aoc.Day05.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(12, aoc.Day05.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(20373, aoc.Day05.PartB(Input.actual));
    }

    public class TestDay06
    {
        [Fact]
        public void ExampleA() => Assert.Equal(5934L, aoc.Day06.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(393019L, aoc.Day06.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(26984457539, aoc.Day06.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(1757714216975, aoc.Day06.PartB(Input.actual));
    }

    public class TestDay07
    {
        [Fact]
        public void ExampleA() => Assert.Equal(37, aoc.Day07.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(348664, aoc.Day07.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(168, aoc.Day07.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(100220525, aoc.Day07.PartB(Input.actual));
    }

    public class TestDay08
    {
        [Fact]
        public void ExampleA() => Assert.Equal(26, aoc.Day08.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(416, aoc.Day08.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(61229, aoc.Day08.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(1043697, aoc.Day08.PartB(Input.actual));
    }

    public class TestDay09
    {
        [Fact]
        public void ExampleA() => Assert.Equal(15, aoc.Day09.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(448, aoc.Day09.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(1134, aoc.Day09.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(1417248, aoc.Day09.PartB(Input.actual));
    }

    public class TestDay10
    {
        [Fact]
        public void ExampleA() => Assert.Equal(26397, aoc.Day10.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(390993, aoc.Day10.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(288957L, aoc.Day10.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(2391385187L, aoc.Day10.PartB(Input.actual));
    }

    public class TestDay11
    {
        [Fact]
        public void ExampleA() => Assert.Equal(1656, aoc.Day11.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(1599, aoc.Day11.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(195, aoc.Day11.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(418, aoc.Day11.PartB(Input.actual));
    }

    public class TestDay12
    {
        [Fact]
        public void ExampleA() => Assert.Equal(226, aoc.Day12.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(4885, aoc.Day12.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(3509, aoc.Day12.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(117095, aoc.Day12.PartB(Input.actual));
    }

    public class TestDay13
    {
        [Fact]
        public void ExampleA() => Assert.Equal(17, aoc.Day13.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(602, aoc.Day13.PartA(Input.actual));
        readonly string b =
            " ##   ##  ####   ## #  # ####  ##  #  #" + System.Environment.NewLine +
            "#  # #  # #       # #  #    # #  # # # " + System.Environment.NewLine +
            "#    #  # ###     # ####   #  #    ##  " + System.Environment.NewLine +
            "#    #### #       # #  #  #   #    # # " + System.Environment.NewLine +
            "#  # #  # #    #  # #  # #    #  # # # " + System.Environment.NewLine +
            " ##  #  # #     ##  #  # ####  ##  #  #" + System.Environment.NewLine;
        [Fact]
        public void TestB() => Assert.Equal(b, aoc.Day13.PartB(Input.actual));
    }

    public class TestDay14
    {
        [Fact]
        public void ExampleA() => Assert.Equal(1588L, aoc.Day14.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(3213L, aoc.Day14.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(2188189693529, aoc.Day14.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(3711743744429, aoc.Day14.PartB(Input.actual));
    }

    public class TestDay15
    {
        [Fact]
        public void ExampleA() => Assert.Equal(40, aoc.Day15.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(503, aoc.Day15.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(315, aoc.Day15.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(2853, aoc.Day15.PartB(Input.actual));
    }

    public class TestDay16
    {
        [Fact]
        public void ExampleA() => Assert.Equal(20L, aoc.Day16.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(821L, aoc.Day16.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(1L, aoc.Day16.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(2056021084691, aoc.Day16.PartB(Input.actual));
    }

    public class TestDay17
    {
        [Fact]
        public void ExampleA() => Assert.Equal(45, aoc.Day17.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(15931, aoc.Day17.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(112, aoc.Day17.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(2555, aoc.Day17.PartB(Input.actual));
    }

    public class TestDay18
    {
        [Fact]
        public void ExampleA() => Assert.Equal(4140, aoc.Day18.PartA(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(3494, aoc.Day18.PartA(Input.actual));
        [Fact]
        public void ExampleB() => Assert.Equal(3993, aoc.Day18.PartB(Input.example));
        [Fact]
        public void TestB() => Assert.Equal(4712, aoc.Day18.PartB(Input.actual));
    }

    public class TestDay19
    {
        [Fact]
        public void Example() => Assert.Equal((79, 3621), aoc.Day19.DoPuzzle(Input.example));
        [Fact]
        public void Test() => Assert.Equal((318, 12166), aoc.Day19.DoPuzzle(Input.actual));
    }

    public class TestDay20
    {
        [Fact]
        public void Example() => Assert.Equal((35, 3351), aoc.Day20.DoPuzzle(Input.example));
        [Fact]
        public void Test() => Assert.Equal((5349, 15806), aoc.Day20.DoPuzzle(Input.actual));
    }

    public class TestDay21
    {
        [Fact]
        public void Example() => Assert.Equal((739785, 444356092776315), aoc.Day21.DoPuzzle(Input.example));
        [Fact]
        public void Test() => Assert.Equal((797160, 27464148626406), aoc.Day21.DoPuzzle(Input.actual));
    }

    public class TestDay22
    {
        [Fact]
        public void Example() => Assert.Equal((474140, 2758514936282235), aoc.Day22.DoPuzzle(Input.example));
        [Fact]
        public void Test() => Assert.Equal((589411, 1130514303649907), aoc.Day22.DoPuzzle(Input.actual));
    }
}
