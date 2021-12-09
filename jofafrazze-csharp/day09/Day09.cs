using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using AdventOfCode;
using Position = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day09
    {
        static readonly string day = "day09";

        // Day 09: 

        public static Object PartA(string file)
        {
            Map m = Map.Build(ReadInput.Strings(day, file));
            int w = m.width;
            int h = m.height;
            int sum = 0;
            for (int y = 0; y < h; y++)
            {
                for (int x = 0; x < w; x++)
                {
                    bool ok = true;
                    var p = new Position(x, y);
                    var pl = p + CoordsRC.goLeft;
                    var pu = p + CoordsRC.goUp;
                    var pr = p + CoordsRC.goRight;
                    var pd = p + CoordsRC.goDown;
                    ok = ok && (!m.HasPosition(pl) || m[pl] > m[p]);
                    ok = ok && (!m.HasPosition(pu) || m[pu] > m[p]);
                    ok = ok && (!m.HasPosition(pr) || m[pr] > m[p]);
                    ok = ok && (!m.HasPosition(pd) || m[pd] > m[p]);
                    if (ok)
                        sum += (m[p] - '0' + 1);
                }
            }
            //Console.WriteLine("A is {0}", a);
            return sum;
        }

        static void GetLows(Map m, List<Position> lows)
        {
            int w = m.width;
            int h = m.height;
            for (int y = 0; y < h; y++)
            {
                for (int x = 0; x < w; x++)
                {
                    bool ok = true;
                    var p = new Position(x, y);
                    var pl = p + CoordsRC.goLeft;
                    var pu = p + CoordsRC.goUp;
                    var pr = p + CoordsRC.goRight;
                    var pd = p + CoordsRC.goDown;
                    ok = ok && (!m.HasPosition(pl) || m[pl] > m[p]);
                    ok = ok && (!m.HasPosition(pu) || m[pu] > m[p]);
                    ok = ok && (!m.HasPosition(pr) || m[pr] > m[p]);
                    ok = ok && (!m.HasPosition(pd) || m[pd] > m[p]);
                    if (ok)
                        lows.Add(p);
                }
            }
        }

        static bool IsLow(Map m, Position p)
        {
            bool ok = true;
            var pl = p + CoordsRC.goLeft;
            var pu = p + CoordsRC.goUp;
            var pr = p + CoordsRC.goRight;
            var pd = p + CoordsRC.goDown;
            ok = ok && (!m.HasPosition(pl) || m[pl] > m[p]);
            ok = ok && (!m.HasPosition(pu) || m[pu] > m[p]);
            ok = ok && (!m.HasPosition(pr) || m[pr] > m[p]);
            ok = ok && (!m.HasPosition(pd) || m[pd] > m[p]);
            return ok;
        }
        static bool AllNeighs9(Map m, Position p)
        {
            bool ok = true;
            var pl = p + CoordsRC.goLeft;
            var pu = p + CoordsRC.goUp;
            var pr = p + CoordsRC.goRight;
            var pd = p + CoordsRC.goDown;
            ok = ok && (!m.HasPosition(pl) || m[pl] == '9');
            ok = ok && (!m.HasPosition(pu) || m[pu] == '9');
            ok = ok && (!m.HasPosition(pr) || m[pr] == '9');
            ok = ok && (!m.HasPosition(pd) || m[pd] == '9');
            return ok;
        }

        static int GetArea(Map m, Position p)
        {
            var been = new HashSet<Position>();
            var check = new List<Position>();
            check.Add(p);
            while (check.Count > 0)
            {
                var checkNext = new List<Position>();
                foreach (var q in check)
                {
                    been.Add(q);
                    if (!AllNeighs9(m, q))
                    {
                        foreach (var d in CoordsRC.directions4)
                        {
                            Position r = new Position(q + d);
                            if (m.HasPosition(r) && !been.Contains(r) && m[r] != '9')
                                checkNext.Add(r);
                        }
                    }
                }
                check = checkNext;
            }
            return been.Count;
        }


        public static Object PartB(string file)
        {
            Map m = Map.Build(ReadInput.Strings(day, file));
            var lows = new List<Position>();
            GetLows(m, lows);
            List<int> areas = new List<int>();
            foreach (var p in lows)
                areas.Add(GetArea(m, p));
            areas.Sort();
            int a = 1;
            for (int i = 0; i < 3; i++)
                a *= areas[areas.Count - 1 - i];
            return a;
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
