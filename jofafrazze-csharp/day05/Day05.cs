using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

using AdventOfCode;
using Position = AdventOfCode.GenericPosition2D<int>;

namespace day05
{
    public class Day05
    {
        readonly static string nsname = typeof(Day05).Namespace;
        readonly static string inputPath = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, @"..\..\..\..\" + nsname + "\\input.txt");

        // Day 05: Count positions with more than one line

        static List<(Position p1, Position p2)> ReadPositions()
        {
            StreamReader reader = File.OpenText(inputPath);
            var list = new List<(Position p1, Position p2)>();
            string line;
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
            if (dict.ContainsKey(p))
                dict[p] = dict[p] + 1;
            else
                dict[p] = 1;
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

        static Object PartA()
        {
            var input = ReadPositions();
            var dict = new Dictionary<Position, int>();
            DrawLines(input, dict, false);
            int ans = dict.Where(a => a.Value > 1).Count(); 
            Console.WriteLine("Part A: Result is {0}", ans);
            return ans;
        }

        static Object PartB()
        {
            var input = ReadPositions();
            var dict = new Dictionary<Position, int>();
            DrawLines(input, dict, true);
            int ans = dict.Where(a => a.Value > 1).Count();
            Console.WriteLine("Part B: Result is {0}", ans);
            return ans;
        }

        static void Main(string[] args)
        {
            Console.WriteLine("AoC 2021 - " + nsname + ":");
            var w = System.Diagnostics.Stopwatch.StartNew();
            PartA();
            PartB();
            w.Stop();
            Console.WriteLine("[Execution took {0} ms]", w.ElapsedMilliseconds);
        }

        public static bool MainTest()
        {
            int a = 6113;
            int b = 20373;
            return (PartA().Equals(a)) && (PartB().Equals(b));
        }
    }
}
