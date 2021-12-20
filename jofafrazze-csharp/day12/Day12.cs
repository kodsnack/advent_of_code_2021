using AdventOfCode;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;

namespace aoc
{
    public class Day12
    {
        // Passage Pathing: Find path through caves, some reenterable

        static Dictionary<string, List<string>> nodes = new Dictionary<string, List<string>>();
        static void ReadNodes(string file)
        {
            nodes = new Dictionary<string, List<string>>();
            static void AddNode(string s, string neigh) =>
                (nodes[s] = nodes.ContainsKey(s) ? nodes[s] : new List<string>()).Add(neigh);
            foreach (var v in File.ReadAllLines(ReadInput.GetPath(Day, file)).Select(x => x.Split('-')))
            {
                AddNode(v[0], v[1]);
                AddNode(v[1], v[0]);
            }
        }

        static void GoToNeighs(string n0, HashSet<string> visited, ref int nOk, bool twice)
        {
            if (n0 != "end")
            {
                visited.Add(n0);
                foreach (var n in nodes[n0])
                {
                    bool valid = n.All(char.IsUpper) || !visited.Contains(n);
                    if (valid || (!n.All(char.IsUpper) && twice && n != "start"))
                        GoToNeighs(n, new HashSet<string>(visited), ref nOk, valid && twice);
                }
            }
            else
                nOk += 1;
        }

        static Object Part(string file, bool partA)
        {
            ReadNodes(file);
            int n = 0;
            GoToNeighs("start", new HashSet<string>(), ref n, !partA);
            return n;
        }

        public static Object PartA(string file) => Part(file, true);
        public static Object PartB(string file) => Part(file, false);

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()!); } }
    }
}
