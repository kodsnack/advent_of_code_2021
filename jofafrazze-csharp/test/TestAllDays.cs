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
        public void ExampleA() => Assert.Equal(7, day01.Day01.PartA(Input.example));
        [Fact]
        public void ExampleB() => Assert.Equal(5, day01.Day01.PartB(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(1301, day01.Day01.PartA(Input.actual));
        [Fact]
        public void TestB() => Assert.Equal(1346, day01.Day01.PartB(Input.actual));
    }

    public class TestDay02
    {
        [Fact]
        public void ExampleA() => Assert.Equal(150, day02.Day02.PartA(Input.example));
        [Fact]
        public void ExampleB() => Assert.Equal(900, day02.Day02.PartB(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(1727835, day02.Day02.PartA(Input.actual));
        [Fact]
        public void TestB() => Assert.Equal(1544000595, day02.Day02.PartB(Input.actual));
    }

    public class TestDay03
    {
        [Fact]
        public void ExampleA() => Assert.Equal(198, day03.Day03.PartA(Input.example));
        [Fact]
        public void ExampleB() => Assert.Equal(230, day03.Day03.PartB(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(2261546, day03.Day03.PartA(Input.actual));
        [Fact]
        public void TestB() => Assert.Equal(6775520, day03.Day03.PartB(Input.actual));
    }

    public class TestDay04
    {
        [Fact]
        public void ExampleA() => Assert.Equal(4512, day04.Day04.PartA(Input.example));
        [Fact]
        public void ExampleB() => Assert.Equal(1924, day04.Day04.PartB(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(29440, day04.Day04.PartA(Input.actual));
        [Fact]
        public void TestB() => Assert.Equal(13884, day04.Day04.PartB(Input.actual));
    }

    public class TestDay05
    {
        [Fact]
        public void ExampleA() => Assert.Equal(5, day05.Day05.PartA(Input.example));
        [Fact]
        public void ExampleB() => Assert.Equal(12, day05.Day05.PartB(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(6113, day05.Day05.PartA(Input.actual));
        [Fact]
        public void TestB() => Assert.Equal(20373, day05.Day05.PartB(Input.actual));
    }

    public class TestDay06
    {
        [Fact]
        public void ExampleA() => Assert.Equal(5934L, day06.Day06.PartA(Input.example));
        [Fact]
        public void ExampleB() => Assert.Equal(26984457539, day06.Day06.PartB(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(393019L, day06.Day06.PartA(Input.actual));
        [Fact]
        public void TestB() => Assert.Equal(1757714216975, day06.Day06.PartB(Input.actual));
    }

    public class TestDay07
    {
        [Fact]
        public void ExampleA() => Assert.Equal(37, day07.Day07.PartA(Input.example));
        [Fact]
        public void ExampleB() => Assert.Equal(168, day07.Day07.PartB(Input.example));
        [Fact]
        public void TestA() => Assert.Equal(348664, day07.Day07.PartA(Input.actual));
        [Fact]
        public void TestB() => Assert.Equal(100220525, day07.Day07.PartB(Input.actual));
    }
}
