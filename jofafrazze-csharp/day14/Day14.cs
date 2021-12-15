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
        // Today: Polymerization, each generation grows exponentially

        static Dictionary<string, char> rules;
        static string ReadData(string file)
        {
            rules = new Dictionary<string, char>();
            var ls = File.ReadAllLines(ReadInput.GetPath(Day, file));
            foreach (var v in ls.Skip(2).Select(x => x.Split(" -> ")))
                rules[v[0]] = v[1][0];
            return ls[0];
        }

        public static Object Part(string file, int gens)
        {
            var poly = ReadData(file);
            var pfreq = Enumerable.Range(0, poly.Length - 1).Select(x => poly.Substring(x, 2)).CounterLong();
            var cfreq = poly.CounterLong();
            for (int i = 0; i < gens; i++)
                foreach (var (k, v) in new Dictionary<string, long>(pfreq))
                {
                    pfreq.Inc(k, -v);
                    pfreq.Inc(new string(new char[] { k[0], rules[k] }), v);
                    pfreq.Inc(new string(new char[] { rules[k], k[1] }), v);
                    cfreq.Inc(rules[k], v);
                }
            return cfreq.Values.Max() - cfreq.Values.Min();
        }

        public static Object PartA(string file) => Part(file, 10);
        public static Object PartB(string file) => Part(file, 40);

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
