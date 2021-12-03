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

        static string GetMostCommonBits(List<string> input, char prefered='X')
        {
            var ones = new int[input[0].Length];
            int n = 0;
            foreach (var s in input)
            {
                for (int i = 0; i < s.Length; i++)
                    ones[i] += (s[i] == '1') ? 1 : 0;
                n += 1;
            }
            string res = "";
            double mean = n / 2.0;
            foreach (int i in ones)
            {
                if (i > mean)
                    res += '1';
                else if (i < mean)
                    res += '0';
                else
                    res += prefered;
            }
            return res;
        }

        static Object PartA()
        {
            var input = ReadIndata.Strings(inputPath);
            var s = GetMostCommonBits(input);
            int a = 0;
            for (int i = 0; i < s.Length; i++)
            {
                a <<= 1;
                a += (s[i] == '1') ? 1 : 0;
            }
            int ones = (1 << s.Length) - 1;
            int b = a ^ ones;
            int ans = a * b;
            Console.WriteLine("Part A: Result is {0}", ans);
            return ans;
        }

        static List<string> KeepMostCommon(List<string> input, int bitPos)
        {
            List<int> tot = new List<int>(new int[input[0].Length]);
            int n = 0;
            foreach (var s in input)
            {
                for (int i = 0; i < s.Length; i++)
                {
                    if (s[s.Length - 1 - i] == '1')
                        tot[i] += 1;
                }
                n += 1;
            }
            var res = new List<string>();
            bool keep1 = tot[bitPos] >= n / 2.0;
            foreach (var s in input)
            {
                if (keep1 && s[tot.Count - 1 - bitPos] == '1')
                    res.Add(s);
                else if (!keep1 && s[tot.Count - 1 - bitPos] == '0')
                    res.Add(s);
            }
            return res;
        }

        static List<string> KeepLeastCommon(List<string> input, int bitPos)
        {
            List<int> tot = new List<int>(new int[input[0].Length]);
            int n = 0;
            foreach (var s in input)
            {
                for (int i = 0; i < s.Length; i++)
                {
                    if (s[s.Length - 1 - i] == '1')
                        tot[i] += 1;
                }
                n += 1;
            }
            var res = new List<string>();
            bool keep1 = tot[bitPos] < n / 2.0;
            foreach (var s in input)
            {
                if (keep1 && s[tot.Count - 1 - bitPos] == '1')
                    res.Add(s);
                else if (!keep1 && s[tot.Count - 1 - bitPos] == '0')
                    res.Add(s);
            }
            return res;
        }

        static Object PartB()
        {
            var input = ReadIndata.Strings(inputPath);
            List<int> tot = new List<int>(new int[input[0].Length]);
            int n = 0;
            foreach (var s in input)
            {
                for (int i = 0; i < s.Length; i++)
                {
                    if (s[s.Length - 1 - i] == '1')
                        tot[i] += 1;
                }
                n += 1;
            }

            var list1 = input;
            var list2 = input;
            for (int i = 0; i < tot.Count; i++)
            {
                if (list1.Count > 1)
                    list1 = KeepMostCommon(list1, tot.Count - 1 - i);
                if (list2.Count > 1)
                    list2 = KeepLeastCommon(list2, tot.Count - 1 - i);
            }

            int num1 = 0;
            int num2 = 0;
            for (int i = 0; i < tot.Count; i++)
            {
                if (list1[0][tot.Count - 1 - i] == '1')
                    num1 += (int)Math.Pow(2, i);
                if (list2[0][tot.Count - 1 - i] == '1')
                    num2 += (int)Math.Pow(2, i);
            }

            int ans = num1 * num2;
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
