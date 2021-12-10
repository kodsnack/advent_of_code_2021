using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode;

namespace aoc
{
    public class Day10
    {
        static readonly string day = "day10";

        // Day 10: Parse lines with different opening and closing brackets

        static (int, Stack<char>) Score(string s)
        {
            var stack = new Stack<char>();
            var copen = "([{<";
            var cclose = ")]}>";
            var score = new int[] { 3, 57, 1197, 25137 };
            foreach (char c in s)
            {
                int a = copen.IndexOf(c);
                if (a >= 0)
                    stack.Push(cclose[a]);
                else if (c == stack.Peek())
                    stack.Pop();
                else
                    return (score[cclose.IndexOf(c)], stack);
            }
            return (0, stack);
        }
        public static Object PartA(string file)
        {
            var z = ReadInput.Strings(day, file);
            return z.Select(x => Score(x).Item1).Sum();
        }

        public static Object PartB(string file)
        {
            var z = ReadInput.Strings(day, file);
            var scores = z.Select(s => Score(s)).Where(x => x.Item1 == 0).Select(x => x.Item2).ToList();
            scores.ForEach(x => x.Push(' '));
            long f(Stack<char> s) => s.Select(c => (long)" )]}>".IndexOf(c)).Aggregate((a, x) => 5 * a + x);
            var s = scores.Select(s => f(s)).OrderBy(x => x).ToList();
            return s[s.Count / 2];
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
