using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode;

namespace day06
{
    public class Day06
    {
        static readonly string day = "day06";

        // Day 06: Count individuals in a school of fish growing exponentially

        static long CountFish(List<int> input, int days)
        {
            var ages = new long[9];
            for (int i = 0; i < 6; i++)
                ages[i] = input.Where(x => x == i).Count();
            for (int x = 0; x < days; x++)
            {
                var l = new long[9];
                for (int i = 0; i < 9; i++)
                {
                    long n = ages[i];
                    if (i == 0)
                    {
                        l[6] += n;
                        l[8] += n;
                    }
                    else
                        l[i - 1] += n;
                }
                ages = l;
            }
            return ages.Sum();
        }

        public static Object PartA(string file)
        {
            var input = ReadInput.Ints(day, file);
            return CountFish(input, 80);
        }

        public static Object PartB(string file)
        {
            var input = ReadInput.Ints(day, file);
            return CountFish(input, 256);
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
