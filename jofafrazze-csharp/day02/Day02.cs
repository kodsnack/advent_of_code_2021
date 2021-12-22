using AdventOfCode;
using System;

namespace aoc
{
    public class Day02
    {
        static readonly string day = "day02";

        // Dive!: Steer submarine up, down and forward

        public static Object PartA(string file)
        {
            var input = ReadInput.StringLists(day, file);
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

        public static Object PartB(string file)
        {
            var input = ReadInput.StringLists(day, file);
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
    }
}
