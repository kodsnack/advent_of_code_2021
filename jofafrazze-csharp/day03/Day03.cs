using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode;

namespace aoc
{
    public class Day03
    {
        static readonly string day = "day03";

        // Binary Diagnostic: Bit calculations will get you dizzy

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

        public static Object PartA(string file)
        {
            var input = ReadInput.Strings(day, file);
            var cs = GetMajorityBits(input);
            int a = BinStringToInt(cs);
            int ones = (1 << cs.Length) - 1;
            int b = a ^ ones;
            return a * b;
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

        public static Object PartB(string file)
        {
            var input = ReadInput.Strings(day, file);
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
            return a * b;
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
