using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

using AdventOfCode;
//using Position = AdventOfCode.GenericPosition2D<int>;

namespace day06
{
    public class Day06
    {
        readonly static string nsname = typeof(Day06).Namespace;
        readonly static string inputPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"..\..\..\..\" + nsname + "\\input.txt");

        // Day 06: 

        static Object PartA()
        {
            var input = ReadIndata.Ints(inputPath);
            for (int x =0; x < 80; x++)
            {
                var l = new List<int>();
                foreach(int i in input)
                {
                    int a = i - 1;
                    if (a < 0)
                    {
                        l.Add(6);
                        l.Add(8);
                    }
                    else
                        l.Add(a);
                }
                input = l;
            }
            int ans = input.Count;
            Console.WriteLine("Part A: Result is {0}", ans);
            return ans;
        }

        static Object PartB()
        {
            var input = ReadIndata.Ints(inputPath);
            var ages = new long[9];
            ages[0] = input.Where(x => x == 0).Count();
            ages[1] = input.Where(x => x == 1).Count();
            ages[2] = input.Where(x => x == 2).Count();
            ages[3] = input.Where(x => x == 3).Count();
            ages[4] = input.Where(x => x == 4).Count();
            ages[5] = input.Where(x => x == 5).Count();
            ages[6] = input.Where(x => x == 6).Count();
            for (int x = 0; x < 256; x++)
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
            long ans = ages.Sum();
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
            int a = 42;
            int b = 4711;
            return (PartA().Equals(a)) && (PartB().Equals(b));
        }
    }
}
