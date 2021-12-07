using System;
using AdventOfCode;

namespace day02
{
    public class Day02
    {
        static readonly string day = "day02";

        // Day 02: Steer submarine up, down and forward

        static Object PartA()
        {
            var input = ReadInput.StringLists(day, " ");
            int d = 0;
            int f = 0;
            foreach (var v in input)
            {
                char c = v[0][0];
                int i = int.Parse(v[1]);
                if (c == 'd')
                    d += i;
                else if (c == 'u')
                    d -= i;
                else
                    f += i;
            }
            return d * f;
        }

        static Object PartB()
        {
            var input = ReadInput.StringLists(day);
            int d = 0;
            int f = 0;
            int aim = 0;
            foreach (var v in input)
            {
                char c = v[0][0];
                int i = int.Parse(v[1]);
                if (c == 'd')
                    aim += i;
                else if (c == 'u')
                    aim -= i;
                else
                {
                    d += aim * i;
                    f += i;
                }
            }
            return d * f;
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
        static readonly int qa = 1727835;
        static readonly int qb = 1544000595;
        public static bool Test() => (PartA().Equals(qa)) && (PartB().Equals(qb));
    }
}
