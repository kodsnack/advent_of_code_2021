using System;
using Xunit;

namespace test
{
    public class TestDay01
    {
        [Fact]
        public void Test()
        {
            Assert.True(day01.Day01.MainTest());
        }
    }

    public class TestDay02
    {
        [Fact]
        public void Test()
        {
            Assert.True(day02.Day02.MainTest());
        }
    }
}
