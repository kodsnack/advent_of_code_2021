using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using AdventOfCode;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day15
    {
        // Today: 

        static Dictionary<Pos, int> bestRisk;
        static int bestTotal;
        static void Walk(Map m, Pos p, int risk)
        {
            if (risk < bestRisk.GetValueOrDefault(p, int.MaxValue))
            {
                if (bestTotal < 0 || risk < bestTotal)
                {
                    bestRisk[p] = risk;
                    if (p.x == m.width - 1 && p.y == m.height - 1)
                    {
                        if (bestTotal < 0 || risk < bestTotal)
                            bestTotal = risk;
                    }
                    else
                    {
                        foreach (var n in CoordsRC.Neighbours4(p))
                        {
                            if (m.HasPosition(n))
                            {
                                int newRisk = risk + m[n] - '0';
                                if (newRisk < bestRisk.GetValueOrDefault(n, int.MaxValue))
                                    Walk(m, n, newRisk);
                            }
                        }
                    }
                }
            }
        }

        public static Object PartA(string file)
        {
            bestRisk = new Dictionary<Pos, int>();
            bestTotal = -1;
            Map m = Map.Build(ReadInput.Strings(Day, file));
            var p = new Pos();
            Walk(m, new Pos(), 0);
            var e = new Pos(m.width - 1, m.height - 1);
            return bestRisk[e];
        }

        static void CopyMap(Map m, int w, int h, Pos sp, Pos dp, int add)
        {
            for (int x = 0; x < w; x++)
            {
                for (int y = 0; y < h; y++)
                {
                    int a = m[new Pos(sp.x + x, sp.y + y)] + add;
                    if (a > '9')
                        a = a - 9;
                    m[new Pos(dp.x + x, dp.y + y)] = (char)a;
                }
            }
        }

        static void WalkB(Map m, Pos p0, int risk0)
        {
            var check = new List<(Pos p, int risk)>() { (p0, risk0) };
            while (check.Count > 0)
            {
                var checkNext = new List<(Pos p, int risk)>();
                foreach ((Pos p, int risk) in check)
                {
                    if (risk < bestRisk.GetValueOrDefault(p, int.MaxValue))
                    {
                        if (bestTotal < 0 || risk < bestTotal)
                        {
                            bestRisk[p] = risk;
                            if (p.x == m.width - 1 && p.y == m.height - 1)
                            {
                                if (bestTotal < 0 || risk < bestTotal)
                                    bestTotal = risk;
                            }
                            else
                            {
                                foreach (var n in CoordsRC.Neighbours4(p))
                                {
                                    if (m.HasPosition(n))
                                    {
                                        int newRisk = risk + m[n] - '0';
                                        if (newRisk < bestRisk.GetValueOrDefault(n, int.MaxValue))
                                            checkNext.Add((n, newRisk));
                                    }
                                }
                            }
                        }
                    }
                }
                check = checkNext.OrderBy(x => x.risk).ToList();
                //Console.Write(".");
            }
            //Console.WriteLine();
        }

        public static Object PartB(string file)
        {
            bestRisk = new Dictionary<Pos, int>();
            bestTotal = -1;
            Map m = Map.Build(ReadInput.Strings(Day, file));
            int sw = m.width;
            int sh = m.height;
            m.Expand(0, sw * 4, sh * 4, 0, ' ');
            var sp = new Pos(0, 0);
            for (int y = 0; y < 5; y++)
            {
                var dp = new Pos(0, y * sh);
                if (y > 0)
                    CopyMap(m, sw, sh, sp, dp, y);
                for (int x = 1; x < 5; x++)
                {
                    var spx = new Pos(0, y * sh);
                    var dpx = new Pos(x * sw, y * sh);
                    CopyMap(m, sw, sh, spx, dpx, x);
                }
            }
            //m.Print();
            var p = new Pos();
            int n = m[p] - '0';
            WalkB(m, new Pos(), 0);
            var e = new Pos(m.width - 1, m.height - 1);
            return bestRisk[e];
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
