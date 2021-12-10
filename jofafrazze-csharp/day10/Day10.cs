using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using AdventOfCode;
//using Position = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day10
    {
        static readonly string day = "day10";

        // Day XX: 

        static int Score(string s)
        {
            var last = new Stack<char>();
            for (int i = 0; i < s.Length; i++)
            {
                char c = s[i];
                if (c == '(')
                    last.Push(')');
                else if (c == '[')
                    last.Push(']');
                else if (c == '{')
                    last.Push('}');
                else if (c == '<')
                    last.Push('>');
                else if (c == last.Peek())
                    last.Pop();
                else
                {
                    char r = c; // last.Pop();
                    if (r == ')')
                        return 3;
                    else if (r == ']')
                        return 57;
                    else if (r == '}')
                        return 1197;
                    else if (r == '>')
                        return 25137;
                }
            }
            return 0;
        }
        public static Object PartA(string file)
        {
            var z = ReadInput.Strings(day, file);
            int sum = 0;
            foreach (var s in z)
                sum += Score(s);
            return sum;
        }

        static long ScoreB(string s)
        {
            var last = new Stack<char>();
            for (int i = 0; i < s.Length; i++)
            {
                char c = s[i];
                if (c == '(')
                    last.Push(')');
                else if (c == '[')
                    last.Push(']');
                else if (c == '{')
                    last.Push('}');
                else if (c == '<')
                    last.Push('>');
                else if (c == last.Peek())
                    last.Pop();
                else
                {
                    char r = c; // last.Pop();
                    if (r == ')')
                        return 0;
                    else if (r == ']')
                        return 0;
                    else if (r == '}')
                        return 0;
                    else if (r == '>')
                        return 0;
                }
            }
            long sum = 0;
            foreach (char c in last)
            {
                sum *= 5;
                if (c == ')')
                    sum += 1;
                else if (c == ']')
                    sum += 2;
                else if (c == '}')
                    sum += 3;
                else if (c == '>')
                    sum += 4;
            }
            return sum;
        }
        public static Object PartB(string file)
        {
            var z = ReadInput.Strings(day, file);
            var scores = new List<long>();
            foreach (var s in z)
            {
                long a = ScoreB(s);
                if (a > 0)
                    scores.Add(a);
            }
            scores.Sort();
            return scores[scores.Count / 2];
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
