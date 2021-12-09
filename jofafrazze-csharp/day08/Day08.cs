using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using AdventOfCode;

namespace aoc
{
    public class Day08
    {
        static readonly string day = "day08";

        // Day 08: Decode scrambled seven-segment displays

        static List<(List<string>, List<string>)> ReadData(string file)
        {
            static List<string> f(string s) => s.Split(' ', StringSplitOptions.RemoveEmptyEntries).ToList();
            var lines = File.ReadAllLines(ReadInput.GetPath(day, file));
            return lines.Select(x => x.Split('|')).Select(x => (f(x[0]), f(x[1]))).ToList();
        }

        public static Object PartA(string file)
        {
            var rows = ReadData(file);
            var lengths = new int[] { 2, 3, 4, 7 };
            var s = rows.Select(x => x.Item2);
            return s.Select(x => x.Where(a => lengths.Contains(a.Length)).Count()).Sum();
        }

        //  Segment     Which numbers?          # of
        //  name                                numbers
        //  -------     --------------------    -------
        //
        //   -A-             0-23-56789          -8-
        //  B   C       0---4          01234    6   8
        //  |   |       56-89          --789    |   |
        //   -D-             --23456-89          -7-
        //  E   F       0-2--          01-34    4   9
        //  |   |       -6-8-          56789    |   |
        //   -G-             0-23-56-89          -7-


        static readonly Dictionary<string, char> segs2num = new Dictionary<string, char>
        {
            ["abcefg"] = '0', ["cf"] = '1', ["acdeg"] = '2', ["acdfg"] = '3', ["bcdf"] = '4',
            ["abdfg"] = '5', ["abdefg"] = '6', ["acf"] = '7', ["abcdefg"] = '8', ["abcdfg"] = '9'
        };

        public static Object PartB(string file)
        {
            var rows = ReadData(file);
            int sum = 0;
            foreach (var (patterns, outputs) in rows)
            {
                var freq = new Dictionary<char, int>();
                var fs = String.Join("", patterns).ToList();
                fs.ForEach(c => freq[c] = freq.GetValueOrDefault(c, 0) + 1);
                var decode = new Dictionary<char, char>();
                decode[freq.Where(x => x.Value == 9).First().Key] = 'f';
                char cf = decode.First().Key;
                decode[freq.Where(x => x.Value == 4).First().Key] = 'e';
                decode[freq.Where(x => x.Value == 6).First().Key] = 'b';
                string p1 = patterns.Where(x => x.Length == 2).First();
                string p4 = patterns.Where(x => x.Length == 4).First();
                string p7 = patterns.Where(x => x.Length == 3).First();
                decode[p1.Where(x => x != cf).First()] = 'c';
                decode[p7.Except(p1).First()] = 'a';
                var seg7 = freq.Where(x => x.Value == 7).Select(x => x.Key);
                decode[seg7.Where(x => !p4.Contains(x)).First()] = 'g';
                decode["abcdefg".Except(decode.Keys).First()] = 'd';
                string f(string s) => new string(s.Select(x => decode[x]).OrderBy(y => y).ToArray());
                sum += int.Parse(outputs.Select(w => segs2num[f(w)]).ToArray());
            }
            return sum;
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
