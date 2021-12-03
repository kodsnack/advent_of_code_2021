using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

using AdventOfCode;
//using Position = AdventOfCode.GenericPosition2D<int>;

namespace day03
{
    public class Day03
    {
        readonly static string nsname = typeof(Day03).Namespace;
        readonly static string inputPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"..\..\..\..\" + nsname + "\\input.txt");

        // Day 03: Bit calculations will get you dizzy

        static string GetMajorityBits(List<string> input)
        {
            var ones = new int[input[0].Length];
            foreach (var s in input)
                for (int i = 0; i < s.Length; i++)
                    ones[i] += (s[i] == '1') ? 1 : 0;
            string res = "";
            double mean = input.Count / 2.0;
            foreach (int i in ones)
                res += (i >= mean) ? '1' : '0';
            return res;
        }

        static string InvertBinString(string s)
        {
            string w = "";
            foreach (char c in s)
                w += (c == '1') ? '0' : '1';
            return w;
        }

        static int BinStringToInt(string s)
        {
            int a = 0;
            for (int i = 0; i < s.Length; i++)
            {
                a <<= 1;
                a += (s[i] == '1') ? 1 : 0;
            }
            return a;
        }

        static Object PartA()
        {
            var input = ReadIndata.Strings(inputPath);
            var cs = GetMajorityBits(input);
            int a = BinStringToInt(cs);
            int ones = (1 << cs.Length) - 1;
            int b = a ^ ones;
            int ans = a * b;
            Console.WriteLine("Part A: Result is {0}", ans);
            return ans;
        }

        static List<string> KeepMostCommon(List<string> input, int bitPos, bool invert)
        {
            var cs = GetMajorityBits(input);
            if (invert)
                cs = InvertBinString(cs);
            var res = new List<string>();
            foreach (var s in input)
                if (s[bitPos] == cs[bitPos])
                    res.Add(s);
            return res;
        }

        static Object PartB()
        {
            var input = ReadIndata.Strings(inputPath);
            var aList = input;
            var bList = input;
            for (int i = 0; i < input[0].Length; i++)
            {
                if (aList.Count > 1)
                    aList = KeepMostCommon(aList, i, false);
                if (bList.Count > 1)
                    bList = KeepMostCommon(bList, i, true);
            }
            int a = BinStringToInt(aList[0]);
            int b = BinStringToInt(bList[0]);
            int ans = a * b;
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
            int a = 2261546;
            int b = 6775520;
            return (PartA().Equals(a)) && (PartB().Equals(b));
        }
    }
}
