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

        static (HashSet<Pos>, List<(bool useX, int n)>) ReadInput(string file)
        {
            var ps = new HashSet<Pos>();
            var fs = new List<(bool, int)>();
            foreach (var s in File.ReadAllLines(AdventOfCode.ReadInput.GetPath(Day, file)))
            {
                var v = s.Split(',');
                var w = s.Split(' ').TakeLast(1).ToArray()[0].Split('=');
                if (v.Length > 1)
                    ps.Add(new Pos(int.Parse(v[0]), int.Parse(v[1])));
                else if (w.Length > 1)
                    fs.Add((w[0] == "x", int.Parse(w[1])));
            }
            return (ps, fs);
        }

        static HashSet<Pos> FoldPositions(HashSet<Pos> pos, List<(bool useX, int n)> fold)
        {
            static Pos FoldX(Pos p, int f) => new Pos((p.x > f) ? 2 * f - p.x : p.x, p.y);
            foreach (var (useX, n) in fold)
                pos = pos.Select(p => useX ? p : p.SwitchXY()).
                    Where(p => p.x != n).Select(p => FoldX(p, n)).
                    Select(p => useX ? p : p.SwitchXY()).ToHashSet();
            return pos;
        }

        public static Object PartA(string file)
        {
            var (pos, fold) = ReadInput(file);
            return FoldPositions(pos, new List<(bool, int)>() { fold[0] }).Count();
        }

        public static Object PartB(string file)
        {
            var (pos, fold) = ReadInput(file);
            pos = FoldPositions(pos, fold);
            Map m = new Map(pos.Select(a => a.x).Max() + 1, pos.Select(a => a.y).Max() + 1, ' ');
            pos.ToList().ForEach(p => m[p] = '#');
            return m.PrintToString();
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
