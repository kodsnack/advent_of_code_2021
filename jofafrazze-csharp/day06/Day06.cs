using AdventOfCode;
using System;
using System.Collections.Generic;
using System.Linq;

namespace aoc
{
    public class Day06
    {
        static readonly string day = "day06";

        // Lanternfish: Count individuals in a school of fish growing exponentially

        static long CountFish(List<int> input, int days)
        {
            var z = Enumerable.Range(0, 9);
            var ages = z.Select(i => (long)input.Where(x => x == i).Count()).ToArray();
            for (int x = 0; x < days; x++)
            {
                var next = new long[9];
                long b = ages[0];
                for (int i = 1; i < 9; i++)
                    next[i - 1] = ages[i];
                next[6] += b;
                next[8] += b;
                ages = next;
            }
            return ages.Sum();
        }

        public static Object PartA(string file) => CountFish(ReadInput.Ints(day, file), 80);
        public static Object PartB(string file) => CountFish(ReadInput.Ints(day, file), 256);
        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
