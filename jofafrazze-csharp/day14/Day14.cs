using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using AdventOfCode;

namespace aoc
{
    public class Day14
    {
        // Today: Polymerization 

        static Dictionary<string, char> rules;
        static string ReadData(string file)
        {
            rules = new Dictionary<string, char>();
            var ls = File.ReadAllLines(ReadInput.GetPath(Day, file));
            foreach (var s in ls.Skip(2))
            {
                var w = s.Split(" -> ");
                rules[w[0]] = w[1][0];
            }
            return ls[0];
        }

        public static Object Part(string file, int gens)
        {
            var poly = ReadData(file);
            var pf = new Dictionary<string, long>();
            for (int n = 0; n < poly.Length - 1; n++)
                pf.DefAdd(poly.Substring(n, 2), 1);
            var cf = poly.GroupBy(x => x).ToDictionary(x => x.Key, x => (long)x.Count());
            for (int i = 0; i < gens; i++)
            {
                foreach (var (k, v) in new Dictionary<string, long>(pf))
                {
                    pf.DefAdd(k, -v);
                    pf.DefAdd(new string(new char[] { k[0], rules[k] }), v);
                    pf.DefAdd(new string(new char[] { rules[k], k[1] }), v);
                    cf.DefAdd(rules[k], v);
                }
            }
            return cf.Values.Max() - cf.Values.Min();
        }

        public static Object PartA(string file) => Part(file, 10);
        public static Object PartB(string file) => Part(file, 40);

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
