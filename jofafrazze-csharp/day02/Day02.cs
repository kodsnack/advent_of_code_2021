using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

using AdventOfCode;
//using Position = AdventOfCode.GenericPosition2D<int>;

namespace day02
{
    public class Day02
    {
        readonly static string nsname = typeof(Day02).Namespace;
        readonly static string inputPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"..\..\..\..\" + nsname + "\\input.txt");

        // Day 02: 

        static int ReadInputA()
        {
            StreamReader reader = File.OpenText(inputPath);
            int d = 0;
            int f = 0;
            string line;
            while ((line = reader.ReadLine()) != null)
            {
                string[] s = line.Split(' ').ToArray();
                var i = int.Parse(s[1]);
                if (s[0][0] == 'd')
                    d += i;
                else if (s[0][0] == 'u')
                    d -= i;
                else
                    f += i;
            }
            return d * f;
        }

        static int ReadInputB()
        {
            StreamReader reader = File.OpenText(inputPath);
            int d = 0;
            int f = 0;
            int aim = 0;
            string line;
            while ((line = reader.ReadLine()) != null)
            {
                string[] s = line.Split(' ').ToArray();
                var i = int.Parse(s[1]);
                if (s[0][0] == 'd')
                {
                    aim += i;
                }
                else if (s[0][0] == 'u')
                {
                    aim -= i;
                }
                else
                {
                    d += aim * i;
                    f += i;
                }
            }
            return d * f;
        }

        static Object PartA()
        {
            var input = ReadInputA();
            int ans = input;
            Console.WriteLine("Part A: Result is {0}", ans);
            return ans;
        }

        static Object PartB()
        {
            var input = ReadInputB();
            int ans = input;
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
