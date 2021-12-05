using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using AdventOfCode;

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

        static int BinStringToInt(string s)
        {
            return s.Select((c, i) => (c == '1' ? 1 : 0) << (s.Length - 1 - i)).Sum();
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
                cs = new string(cs.Select(c => (c == '1' ? '0' : '1')).ToArray());
            var res = new List<string>();
            foreach (var s in input)
                if (s[bitPos] == cs[bitPos])
                    res.Add(s);
            return res;
        }

        static Object PartB()
        {
            var input = ReadIndata.Strings(inputPath);
            var al = input;
            var bl = input;
            for (int i = 0; i < input[0].Length; i++)
            {
                if (al.Count > 1)
                    al = KeepMostCommon(al, i, false);
                if (bl.Count > 1)
                    bl = KeepMostCommon(bl, i, true);
            }
            int a = BinStringToInt(al[0]);
            int b = BinStringToInt(bl[0]);
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
