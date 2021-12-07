using System;
using System.Linq;
using AdventOfCode;

namespace day07
{
    public class Day07
    {
        static readonly string day = "day07";

        // Day 07: Minimize sum of integers

        static Object PartA()
        {
            var z = ReadInput.Ints(day);
            static int f(int a, int mean) => Math.Abs(a - mean);
            var r = Enumerable.Range(z.Min(), z.Max());
            return r.Select(i => z.Select(x => f(x, i)).Sum()).Min();
        }

        static Object PartB()
        {
            var z = ReadInput.Ints(day);
            static int f(int a, int mean)
            {
                int d = Math.Abs(a - mean);
                return d * (d + 1) / 2;
            }
            var r = Enumerable.Range(z.Min(), z.Max());
            return r.Select(i => z.Select(x => f(x, i)).Sum()).Min();
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
        static readonly int qa = 348664;
        static readonly int qb = 100220525;
        public static bool Test() => (PartA().Equals(qa)) && (PartB().Equals(qb));
    }
}
