using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using AdventOfCode;

namespace aoc
{
    public class Day10
    {
        // Today: Parse lines with different opening and closing brackets

        static (int v, Stack<char> t) Score(string s)
        {
            var stack = new Stack<char>();
            (var copen, var cclose, var score) = ("([{<", ")]}>", new int[] { 3, 57, 1197, 25137 });
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
            var z = ReadInput.Strings(Day, file);
            return z.Select(x => Score(x).v).Sum();
        }

        public static Object PartB(string file)
        {
            var z = ReadInput.Strings(Day, file);
            var stacks = z.Select(s => Score(s)).Where(x => x.v == 0).Select(x => x.t).ToList();
            static long f(Stack<char> t) => 
                t.Select(c => " )]}>".IndexOf(c)).Aggregate(0L, (a, x) => 5 * a + x);
            var w = stacks.Select(x => f(x)).OrderBy(x => x).ToList();
            return w[w.Count / 2];
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
