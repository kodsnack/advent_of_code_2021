using System;
using System.Linq;
using AdventOfCode;

namespace aoc
{
    public class Day07
    {
        static readonly string day = "day07";

        // Day 07: Minimize sum of integers

        public static Object PartA(string file)
        {
            var z = ReadInput.Ints(day, file);
            static int f(int a, int mean) => Math.Abs(a - mean);
            var r = Enumerable.Range(z.Min(), z.Max());
            return r.Select(i => z.Select(x => f(x, i)).Sum()).Min();
        }

        public static Object PartB(string file)
        {
            var z = ReadInput.Ints(day, file);
            static int f(int a, int mean)
            {
                int d = Math.Abs(a - mean);
                return d * (d + 1) / 2;
            }
            var r = Enumerable.Range(z.Min(), z.Max());
            return r.Select(i => z.Select(x => f(x, i)).Sum()).Min();
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
