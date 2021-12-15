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

        class RiskComparer : IComparer<(Pos p, int r)>
        {
            public int Compare((Pos p, int r) a, (Pos p, int r)b) => 
                (a.r == b.r) ? ((a.p == b.p) ? 0 : -1) : (a.r < b.r) ? -1 : 1;
        }

        static int WalkMap(Map m)
        {
            // Using SortedSet in the absence of a priority queue
            var minRisk = new Dictionary<Pos, int>();
            var steps = new SortedSet<(Pos, int)>(new RiskComparer()) { (new Pos(), 0) };
            int iter = 0;
            while (steps.Count > 0)
            {
                (Pos p, int risk) = steps.First();
                steps.Remove((p, risk));
                iter++;
                if (risk < minRisk.GetValueOrDefault(p, int.MaxValue))
                {
                    minRisk[p] = risk;
                    foreach (var n in CoordsRC.Neighbours4(p).Where(x => m.HasPosition(x)))
                        if (risk + m[n] - '0' < minRisk.GetValueOrDefault(n, int.MaxValue))
                            steps.Add((n, risk + m[n] - '0'));
                }
            }
            //Console.WriteLine("Used {0} iterations.", iter);
            return minRisk[m.Positions().Last()];
        }

        public static Object PartA(string file) => WalkMap(Map.Build(ReadInput.Strings(Day, file)));

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
            return WalkMap(m);
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
