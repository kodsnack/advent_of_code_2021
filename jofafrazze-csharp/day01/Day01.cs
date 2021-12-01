using System;
using System.IO;
using AdventOfCode;

namespace day01
{
    public class Day01
    {
        readonly static string nsname = typeof(Day01).Namespace;
        readonly static string inputPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"..\..\..\..\" + nsname + "\\input.txt");

        // Day 01: Count increments

        static Object PartA()
        {
            var input = ReadIndata.Ints(inputPath);
            int ans = 0;
            for (int i = 1; i < input.Count; i++)
                if (input[i] > input[i-1])
                    ans++;
            Console.WriteLine("Part A: Result is {0}", ans);
            return ans;
        }

        static Object PartB()
        {
            var v = ReadIndata.Ints(inputPath);
            int ans = 0;
            for (int i = 1; i < v.Count-2; i++)
                if (v[i] + v[i+1] + v[i+2] > v[i-1] + v[i] + v[i+1])
                    ans++;
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
            int a = 1301;
            int b = 1346;
            return (PartA().Equals(a)) && (PartB().Equals(b));
        }
    }
}
