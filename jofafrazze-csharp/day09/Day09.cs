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

        // Day 09: Find local lows and baisins in map

        static List<Pos> GetLows(Map m)
        {
            var lows = new List<Pos>();
            foreach (var p in m.Positions())
                if (CoordsXY.directions4.Select(d => !m.HasPosition(p + d) || m[p] < m[p + d]).Aggregate((a, x) => a && x))
                    lows.Add(p);
            return lows;
        }

        public static Object PartA(string file)
        {
            Map m = Map.Build(ReadInput.Strings(day, file));
            var lows = GetLows(m);
            return lows.Select(p => m[p] - '0' + 1).Sum();
        }

        static bool AllNeighs9(Map m, Pos p) => 
            CoordsXY.directions4.Select(d => !m.HasPosition(p + d) || m[p + d] == '9').Aggregate((a, x) => a && x);

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
                        foreach (var d in CoordsXY.directions4)
                            if (m.HasPosition(q + d) && !visited.Contains(q + d) && m[q + d] != '9')
                                checkNext.Add(q + d);
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
