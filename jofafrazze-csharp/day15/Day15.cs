using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using AdventOfCode;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day15
    {
        // Today: Walk map, find minimum total sum to the end position

        static Dictionary<Pos, int> minRisk;
        static int minFinalRisk;
        
        class RiskComparer : IComparer<(Pos p, int r)>
        {
            public int Compare((Pos p, int r) a, (Pos p, int r)b) => (a.r == b.r) 
                ? ((a.p == b.p) ? 0 : (a.p.ManhattanDistance() < b.p.ManhattanDistance() ? 1 : -1)) 
                : (a.r < b.r) ? -1 : 1;
        }

        static void WalkMap(Map m)
        {
            // Using SortedSet in the absence of a priority queue
            var prio = new SortedSet<(Pos, int)>(new RiskComparer()) { (new Pos(), 0) };
            var pEnd = m.Positions().Last();
            while (prio.Count > 0)
            {
                (Pos p, int risk) = prio.First();
                prio.Remove((p, risk));
                if (risk < minFinalRisk && risk < minRisk.GetValueOrDefault(p, int.MaxValue))
                {
                    minRisk[p] = risk;
                    if (p == pEnd)
                        minFinalRisk = Math.Min(risk, minFinalRisk);
                    else
                        foreach (var n in CoordsRC.Neighbours4(p).Where(x => m.HasPosition(x)))
                        {
                            int newRisk = risk + m[n] - '0';
                            if (newRisk < minFinalRisk && newRisk < minRisk.GetValueOrDefault(n, int.MaxValue))
                                prio.Add((n, newRisk));
                        }
                }
            }
        }

        public static Object PartA(string file)
        {
            minRisk = new Dictionary<Pos, int>();
            minFinalRisk = int.MaxValue;
            WalkMap(Map.Build(ReadInput.Strings(Day, file)));
            return minFinalRisk;
        }

        public static Object PartB(string file)
        {
            static void CopyMap(Map m, int w, int h, Pos sp, Pos dp, int add)
            {
                foreach (Pos p in m.Positions(sp, w, h))
                {
                    int a = m[p] + add;
                    m[p + (dp - sp)] = (char)((a > '9') ? a - 9 : a);
                }
            }
            minRisk = new Dictionary<Pos, int>();
            minFinalRisk = int.MaxValue;
            Map m = Map.Build(ReadInput.Strings(Day, file));
            int w = m.width;
            int h = m.height;
            m.Expand(0, w * 4, h * 4, 0, '.');
            for (int y = 0; y < 5; y++)
            {
                if (y > 0)
                    CopyMap(m, w, h, new Pos(), new Pos(0, y * h), y);
                for (int x = 1; x < 5; x++)
                    CopyMap(m, w, h, new Pos(0, y * h), new Pos(x * w, y * h), x);
            }
            WalkMap(m);
            return minFinalRisk;
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
