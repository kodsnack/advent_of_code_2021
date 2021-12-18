using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day09
    {
        static readonly string day = "day09";

        // Smoke Basin: Find local lows and baisins in map

        static List<Pos> GetLows(Map m)
        {
            var lows = new List<Pos>();
            foreach (var p in m.Positions())
                if (CoordsXY.Neighbours4(p).Select(n => !m.HasPosition(n) || m[p] < m[n]).Aggregate((a, x) => a && x))
                    lows.Add(p);
            return lows;
        }

        public static Object PartA(string file)
        {
            Map m = Map.Build(ReadInput.Strings(day, file));
            return GetLows(m).Select(p => m[p] - '0' + 1).Sum();
        }

        static bool AllNeighs9(Map m, Pos p) => 
            CoordsXY.Neighbours4(p).Select(n => !m.HasPosition(n) || m[n] == '9').Aggregate((a, x) => a && x);

        static int GetArea(Map m, Pos p)
        {
            var visited = new HashSet<Pos>();
            var check = new List<Pos> { p };
            while (check.Count > 0)
            {
                var checkNext = new List<Pos>();
                visited.UnionWith(check);
                foreach (var q in check)
                    if (!AllNeighs9(m, q))
                        foreach (var n in CoordsXY.Neighbours4(q))
                            if (m.HasPosition(n) && !visited.Contains(n) && m[n] != '9')
                                checkNext.Add(n);
                check = checkNext;
            }
            return visited.Count;
        }

        public static Object PartB(string file)
        {
            Map m = Map.Build(ReadInput.Strings(day, file));
            return GetLows(m).Select(x => GetArea(m, x)).OrderByDescending(x => x).Take(3).Aggregate((a, x) => a * x);
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
