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

        static List<(List<string>, List<string>)> ReadInput(string file)
        {
            StreamReader reader = File.OpenText(AdventOfCode.ReadInput.GetPath(day, file));
            var r = new List<(List<string>, List<string>)>();
            string line;
            while ((line = reader.ReadLine()) != null)
            {
                var v = line.Split('|');
                r.Add((v[0].Split(' ', StringSplitOptions.RemoveEmptyEntries).ToList(),
                       v[1].Split(' ', StringSplitOptions.RemoveEmptyEntries).ToList()));
            }
            return r;
        }

        public static Object PartA(string file)
        {
            var rows = ReadInput(file);
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


        static readonly Dictionary<string, int> lookup = new Dictionary<string, int>
        {
            ["abcefg"] = 0, ["cf"] = 1, ["acdeg"] = 2, ["acdfg"] = 3, ["bcdf"] = 4,
            ["abdfg"] = 5, ["abdefg"] = 6, ["acf"] = 7, ["abcdefg"] = 8, ["abcdfg"] = 9
        };

        public static Object PartB(string file)
        {
            var rows = ReadInput(file);
            int sum = 0;
            foreach (var (patterns, outputs) in rows)
            {
                var seg = new Dictionary<char, char>();
                var freq = new Dictionary<char, int>();
                string p1 = patterns.Where(x => x.Length == 2).First();
                string p4 = patterns.Where(x => x.Length == 4).First();
                string p7 = patterns.Where(x => x.Length == 3).First();
                var fs = String.Join("", patterns).ToList();
                fs.ForEach(c => freq[c] = freq.GetValueOrDefault(c, 0) + 1);
                char f = freq.Where(x => x.Value == 9).First().Key;
                seg[f] = 'f';
                seg[p1.Where(x => x != f).First()] = 'c';
                seg[p7.Except(p1).First()] = 'a';
                seg[freq.Where(x => x.Value == 4).First().Key] = 'e';
                seg[freq.Where(x => x.Value == 6).First().Key] = 'b';
                var seg7 = freq.Where(x => x.Value == 7).Select(x => x.Key);
                seg[seg7.Where(x => !p4.Contains(x)).First()] = 'g';
                seg["abcdefg".Except(seg.Keys).First()] = 'd';
                int rowSum = 0;
                for (int n = 0; n < 4; n++)
                {
                    string decoded = new string(outputs[n].Select(x => seg[x]).OrderBy(y => y).ToArray());
                    rowSum += lookup[decoded] * (int)Math.Pow(10, 3 - n);
                }
                sum += rowSum;
            }
            return sum;
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
