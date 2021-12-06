using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using AdventOfCode;

namespace day06
{
    public class Day06
    {
        readonly static string nsname = typeof(Day06).Namespace;
        readonly static string inputPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"..\..\..\..\" + nsname + "\\input.txt");

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

        static Object PartA()
        {
            var input = ReadIndata.Ints(inputPath);
            long ans = CountFish(input, 80);
            Console.WriteLine("Part A: Result is {0}", ans);
            return ans;
        }

        static Object PartB()
        {
            var input = ReadIndata.Ints(inputPath);
            long ans = CountFish(input, 256);
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
            long a = 393019;
            long b = 1757714216975;
            return (PartA().Equals(a)) && (PartB().Equals(b));
        }
    }
}
