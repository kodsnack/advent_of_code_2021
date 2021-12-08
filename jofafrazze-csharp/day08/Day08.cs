using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using AdventOfCode;
//using Position = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day08
    {
        static readonly string day = "day08";

        // Day 08: 

        static int ReadA(string file)
        {
            StreamReader reader = File.OpenText(AdventOfCode.ReadInput.GetPath(day, file));
            List<int> list = new List<int>();
            string line;
            int sum = 0;
            while ((line = reader.ReadLine()) != null)
            {
                var ls = line.Split('|', StringSplitOptions.RemoveEmptyEntries);
                var a = ls[1].Split(' ', StringSplitOptions.RemoveEmptyEntries).ToList();
                foreach (string s in a)
                {
                    int n = s.Length;
                    if ((n == 2) || (n == 3) || (n == 4) || (n == 7))
                        sum++;
                }
            }
            return sum;
        }

        static (List<List<string>>, List<List<string>>) ReadInput(string file)
        {
            StreamReader reader = File.OpenText(AdventOfCode.ReadInput.GetPath(day, file));
            List<List<string>> a = new List<List<string>>();
            List<List<string>> b = new List<List<string>>();
            string line;
            while ((line = reader.ReadLine()) != null)
            {
                var ls = line.Split('|', StringSplitOptions.RemoveEmptyEntries);
                a.Add(ls[0].Split(' ', StringSplitOptions.RemoveEmptyEntries).ToList());
                b.Add(ls[1].Split(' ', StringSplitOptions.RemoveEmptyEntries).ToList());
            }
            return (a, b);
        }

        public static Object PartA(string file)
        {
            var z = ReadA(file);
            //Console.WriteLine("A is {0}", a);
            return z;
        }

        public static Object PartB(string file)
        {
            var (ca, cb) = ReadInput(file);
            var lookup = new Dictionary<string, int>
            {
                ["abcefg"] = 0,
                ["cf"] = 1,
                ["acdeg"] = 2,
                ["acdfg"] = 3,
                ["bcdf"] = 4,
                ["abdfg"] = 5,
                ["abdefg"] = 6,
                ["acf"] = 7,
                ["abcdefg"] = 8,
                ["abcdfg"] = 9
            };
            int sum = 0;
            for (int i = 0; i < ca.Count; i++)
            {
                var segment = new Dictionary<char, char>();
                var freq = new Dictionary<char, int>();
                var patterns = ca[i];
                string p1 = patterns.Where(x => x.Length == 2).First();
                string p4 = patterns.Where(x => x.Length == 4).First();
                string p7 = patterns.Where(x => x.Length == 3).First();
                foreach (string s in patterns)
                    foreach (char c in s)
                        freq[c] = freq.GetValueOrDefault(c, 0) + 1;
                char segF = freq.Where(x => x.Value == 9).First().Key;
                segment[segF] = 'f';
                char segC = p1.Where(x => x != segF).First();
                segment[segC] = 'c';
                char segA = p7.Except(p1).First();
                segment[segA] = 'a';
                char segE = freq.Where(x => x.Value == 4).First().Key;
                segment[segE] = 'e';
                char segB = freq.Where(x => x.Value == 6).First().Key;
                segment[segB] = 'b';

                var seg7 = freq.Where(x => x.Value == 7).Select(x => x.Key);
                char segG = seg7.Where(x => !p4.Contains(x)).First();
                segment[segG] = 'g';

                char segD = "abcdefg".Except(new char[]{ segA, segB, segC, segE, segF, segG }).First();
                segment[segD] = 'd';

                var outputs = cb[i];
                int rowSum = 0;
                for (int n = 0; n < 4; n++)
                {
                    string scrambled = outputs[n];
                    string decoded = new string(scrambled.Select(x => segment[x]).ToArray());
                    string ds = String.Concat(decoded.OrderBy(c => c));
                    rowSum += lookup[ds] * (int)Math.Pow(10, 3 - n);
                }
                sum += rowSum;
            }
            return sum;
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
