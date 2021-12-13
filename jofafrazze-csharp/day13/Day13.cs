using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using AdventOfCode;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day13
    {
        // Today: Fold paper, do manual OCR 

        static List<(bool useX, int n)> fold;
        static HashSet<Pos> ReadData(string file)
        {
            var ps = new HashSet<Pos>();
            fold = new List<(bool, int)>();
            foreach (var s in File.ReadAllLines(ReadInput.GetPath(Day, file)))
            {
                var v = s.Split(',');
                var w = s.Split(' ').Last().Split('=');
                if (v.Length > 1)
                    ps.Add(new Pos(int.Parse(v[0]), int.Parse(v[1])));
                else if (w.Length > 1)
                    fold.Add((w[0] == "x", int.Parse(w[1])));
            }
            return ps;
        }

        static HashSet<Pos> FoldPositions(HashSet<Pos> pos, bool partA)
        {
            static Pos FoldX(Pos p, int f) => new Pos((p.x > f) ? 2 * f - p.x : p.x, p.y);
            foreach (var (useX, n) in (partA ? new List<(bool, int)>() { fold[0] } : fold))
                pos = pos.Select(p => useX ? p : p.SwitchXY()).
                    Where(p => p.x != n).Select(p => FoldX(p, n)).
                    Select(p => useX ? p : p.SwitchXY()).ToHashSet();
            return pos;
        }

        public static Object PartA(string file) => FoldPositions(ReadData(file), true).Count();

        public static Object PartB(string file)
        {
            var pos = FoldPositions(ReadData(file), false);
            Map m = new Map(pos.Select(a => a.x).Max() + 1, pos.Select(a => a.y).Max() + 1, ' ');
            pos.ToList().ForEach(p => m[p] = '#');
            return m.PrintToString();
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
