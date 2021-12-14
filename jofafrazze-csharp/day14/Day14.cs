using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using AdventOfCode;
//using Position = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day14
    {
        // Today: Polymerization 

        static Dictionary<string, char> rulesDict;
        static string ReadData(string file)
        {
            rulesDict = new Dictionary<string, char>();
            string ret = "";
            foreach (var s in File.ReadAllLines(ReadInput.GetPath(Day, file)))
            {
                if (ret == "")
                    ret = s;
                else if (s != "")
                {
                    var w = s.Split(" -> ");
                    rulesDict[w[0]] = w[1][0];
                }
            }
            return ret;
        }
        public static Object PartA(string file)
        {
            var poly = ReadData(file);
            for (int i = 0; i < 10; i++)
            {
                string nextPoly = "";
                for (int n = 0; n < poly.Length - 1; n++)
                {
                    char add = rulesDict[poly.Substring(n, 2)];
                    if (nextPoly == "")
                        nextPoly += poly.Substring(n, 1);
                    nextPoly += add + poly.Substring(n + 1, 1);
                }
                poly = nextPoly;
            }
            var counts = poly.GroupBy(x => x).ToDictionary(g => g.Key, g => g.Count());
            var nc = counts.Values.OrderBy(x => x).ToList();
            return nc.Last() - nc.First();
        }

        public static Object PartB(string file)
        {
            var freq = new Dictionary<string, long>();
            var cFreq = new Dictionary<char, long>();
            var poly = ReadData(file);
            for (int n = 0; n < poly.Length - 1; n++)
            {
                string s = poly.Substring(n, 2);
                freq[s] = freq.GetValueOrDefault(s, 0) + 1;
            }
            for (int n = 0; n < poly.Length; n++)
            {
                char c = poly[n];
                cFreq[c] = cFreq.GetValueOrDefault(c, 0) + 1;
            }
            for (int i = 0; i < 40; i++)
            {
                var nextFreq = new Dictionary<string, long>(freq);
                var nextCFreq = new Dictionary<char, long>(cFreq);
                foreach (var (k, v) in freq)
                {
                    long n = freq[k];
                    char c = rulesDict[k];
                    string s1 = new string(new char[] { k[0], c });
                    string s2 = new string(new char[] { c, k[1] });
                    nextFreq[k] = nextFreq[k] - n;
                    nextFreq[s1] = nextFreq.GetValueOrDefault(s1, 0) + n;
                    nextFreq[s2] = nextFreq.GetValueOrDefault(s2, 0) + n;
                    nextCFreq[c] = nextCFreq.GetValueOrDefault(c, 0) + n;
                }
                freq = nextFreq;
                cFreq = nextCFreq;
            }
            var nFreq = cFreq.Values.OrderBy(x => x).ToList();
            long a = nFreq.Max();
            long b = nFreq.Min();
            Console.WriteLine("max = {0}", a);
            Console.WriteLine("min = {0}", b);
            return a - b;
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
