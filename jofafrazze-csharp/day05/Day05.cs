using AdventOfCode;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Position = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day05
    {
        static readonly string day = "day05";

        // Hydrothermal Venture: Count positions with more than one line

        static List<(Position p1, Position p2)> ReadPositions(string file)
        {
            StreamReader reader = File.OpenText(ReadInput.GetPath(day, file));
            var list = new List<(Position p1, Position p2)>();
            string? line;
            static Position ReadPos(string s)
            {
                var ls = s.Split(',').Select(int.Parse).ToList();
                return new Position(ls[0], ls[1]);
            }
            while ((line = reader.ReadLine()) != null)
            {
                var ls = line.Split(" -> ");
                list.Add((ReadPos(ls[0]), ReadPos(ls[1])));
            }
            return list;
        }

        static void IncPos(Dictionary<Position, int> dict, Position p)
        {
            dict[p] = dict.GetValueOrDefault(p, 0) + 1;
        }

        static void DrawLines(List<(Position, Position)> lines, Dictionary<Position, int> dict, bool diagonals)
        {
            foreach ((Position p1, Position p2) in lines)
            {
                if (p1.x == p2.x)
                {
                    int a = Math.Min(p1.y, p2.y);
                    int b = Math.Max(p1.y, p2.y);
                    for (int i = a; i <= b; i++)
                        IncPos(dict, new Position(p1.x, i));
                }
                else if (p1.y == p2.y)
                {
                    int a = Math.Min(p1.x, p2.x);
                    int b = Math.Max(p1.x, p2.x);
                    for (int i = a; i <= b; i++)
                        IncPos(dict, new Position(i, p1.y));
                }
                else if (diagonals)
                {
                    Position hp = (p1.y < p2.y) ? new Position(p1) : new Position(p2);
                    Position lp = (p1.y < p2.y) ? new Position(p2) : new Position(p1);
                    int len = lp.y - hp.y;
                    int direction = (hp.x < lp.x) ? 1 : -1;
                    for (int i = 0; i <= len; i++)
                        IncPos(dict, new Position(hp.x + i * direction, hp.y + i));
                }
            }
        }

        public static Object PartA(string file)
        {
            var input = ReadPositions(file);
            var dict = new Dictionary<Position, int>();
            DrawLines(input, dict, false);
            return dict.Where(a => a.Value > 1).Count();
        }

        public static Object PartB(string file)
        {
            var input = ReadPositions(file);
            var dict = new Dictionary<Position, int>();
            DrawLines(input, dict, true);
            return dict.Where(a => a.Value > 1).Count();
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
