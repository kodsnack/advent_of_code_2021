using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

using AdventOfCode;
//using Position = AdventOfCode.GenericPosition2D<int>;

namespace day07
{
    public class Day07
    {
        readonly static string nsname = typeof(Day07).Namespace;
        readonly static string inputPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"..\..\..\..\" + nsname + "\\input.txt");

        // Day 07: 

        static Object PartA()
        {
            var z = ReadIndata.Ints(inputPath);
            static int f(int a, int mean) => Math.Abs(a - mean);
            long ans = Enumerable.Range(z.Min(), z.Max()).Select(i => z.Select(x => f(x, i)).Sum()).Min();
            Console.WriteLine("Part A: Result is {0}", ans);
            return ans;
        }

        static Object PartB()
        {
            var z = ReadIndata.Ints(inputPath);
            static int f(int a, int mean)
            {
                int d = Math.Abs(a - mean);
                return d * (d + 1) / 2;
            }
            long ans = Enumerable.Range(z.Min(), z.Max()).Select(i => z.Select(x => f(x, i)).Sum()).Min();
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
            long a = 348664;
            long b = 100220525;
            return (PartA().Equals(a)) && (PartB().Equals(b));
        }
    }
}
