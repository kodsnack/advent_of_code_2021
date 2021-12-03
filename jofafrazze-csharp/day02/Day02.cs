using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using AdventOfCode;

namespace day02
{
    public class Day02
    {
        readonly static string nsname = typeof(Day02).Namespace;
        readonly static string inputPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"..\..\..\..\" + nsname + "\\input.txt");

        // Day 02: Steer submarine up, down and forward

        /*
        static List<(char c, int i)> ReadInput()
        {
            StreamReader reader = File.OpenText(inputPath);
            var list = new List<(char, int)>();
            string line;
            while ((line = reader.ReadLine()) != null)
            {
                string[] s = line.Split(' ').ToArray();
                list.Add((s[0][0], int.Parse(s[1])));
            }
            return list;
        }
        */

        static Object PartA()
        {
            var input = ReadIndata.StringLists(inputPath, ' ');
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
            int ans = d * f;
            Console.WriteLine("Part A: Result is {0}", ans);
            return ans;
        }

        static Object PartB()
        {
            var input = ReadIndata.StringLists(inputPath);
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
            int ans = d * f;
            Console.WriteLine("Part B: Result is {0}", ans);
            return ans;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("AoC 2021 - " + nsname + ":");
            var w = System.Diagnostics.Stopwatch.StartNew();
            PartA();
            PartB();
            w.Stop();
            Console.WriteLine("[Execution took {0} ms]", w.ElapsedMilliseconds);
        }

        public static bool MainTest()
        {
            int a = 1727835;
            int b = 1544000595;
            return (PartA().Equals(a)) && (PartB().Equals(b));
        }
    }
}
