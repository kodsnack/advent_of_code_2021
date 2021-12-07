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
            var input = ReadIndata.Ints(inputPath);
            int n = input.Count();
            int q = input.Min();
            int r = input.Max();
            long ans = long.MaxValue;
            //Console.WriteLine("Part A: From {0} to {1}", q, r);
            for (int i = q; i < r; i++)
            {
                long sum = 0;
                foreach (int a in input)
                    sum += Math.Abs(a - i);
                if (sum < ans)
                {
                    //Console.WriteLine("Part A: New min {0}", sum);
                    ans = sum;
                }
            }
            Console.WriteLine("Part A: Result is {0}", ans);
            return ans;
        }

        static Object PartB()
        {
            var input = ReadIndata.Ints(inputPath);
            int q = input.Min();
            int r = input.Max();
            long ans = long.MaxValue;
            //Console.WriteLine("Part A: From {0} to {1}", q, r);
            for (int i = q; i < r; i++)
            {
                long sum = 0;
                foreach (int a in input)
                {
                    int d = Math.Abs(a - i);
                    sum += d * (d + 1) / 2;
                }
                if (sum < ans)
                {
                    //Console.WriteLine("Part A: New min {0}", sum);
                    ans = sum;
                }
            }
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
