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
    public class Day13
    {
        // Today: 

        static (HashSet<Pos>, List<Pos>) ReadInput(string file)
        {
            var ps = new HashSet<Pos>();
            var fs = new List<Pos>();
            foreach (var s in File.ReadAllLines(AdventOfCode.ReadInput.GetPath(Day, file)))
            {
                if (s.Contains(','))
                {
                    var v = s.Split(',');
                    var p = new Pos(int.Parse(v[0]), int.Parse(v[1]));
                    ps.Add(p);
                }
                else if (s.Contains('='))
                {
                    var w = s.Split(' ').TakeLast(1).ToArray()[0].Split('=');
                    int x = w[0] == "x" ? int.Parse(w[1]) : 0;
                    int y = w[0] == "y" ? int.Parse(w[1]) : 0;
                    fs.Add(new Pos(x, y));
                }
            }
            return (ps, fs);
        }
        public static Object PartA(string file)
        {
            var (pos, fold) = ReadInput(file);
            var f = fold[0];
            var paper = new HashSet<Pos>();
            if (f.y == 0)
            {
                foreach (var p in pos)
                {
                    var q = new Pos(p);
                    if (q.x > f.x)
                        q.x = f.x - (q.x - f.x);
                    if (q.x != f.x && q.x >= 0)
                        paper.Add(q);
                }
            }
            else
            {
                foreach (var p in pos)
                {
                    var q = new Pos(p);
                    if (q.y > f.y)
                        q.y = f.y - (q.y - f.y);
                    if (q.y != f.y && q.y >= 0)
                        paper.Add(q);
                }
            }
            return paper.Count();
        }

        public static Object PartB(string file)
        {
            var (pos, fold) = ReadInput(file);
            foreach (Pos f in fold)
            {
                var paper = new HashSet<Pos>();
                if (f.y == 0)
                {
                    foreach (var p in pos)
                    {
                        var q = new Pos(p);
                        if (q.x > f.x)
                            q.x = f.x - (q.x - f.x);
                        if (q.x != f.x && q.x >= 0)
                            paper.Add(q);
                    }
                }
                else
                {
                    foreach (var p in pos)
                    {
                        var q = new Pos(p);
                        if (q.y > f.y)
                            q.y = f.y - (q.y - f.y);
                        if (q.y != f.y && q.y >= 0)
                            paper.Add(q);
                    }
                }
                pos = paper;
            }
            int x = pos.Select(a => a.x).Max()+1;
            int y = pos.Select(a => a.y).Max()+1;
            Map m = new Map(x, y, new Pos(), ' ');
            foreach (var p in pos)
                m[p] = '#';
            return m.PrintToString();
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
