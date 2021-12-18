using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using AdventOfCode;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day11
    {
        // Dumbo Octopus: Handle flashes in a 10 by 10 grid

        static void FlashPos(Map m, Pos p, HashSet<Pos> visited)
        {
            visited.Add(p);
            foreach (Pos n in CoordsXY.Neighbours8(p))
                if (m.HasPosition(n))
                {
                    m[n] = (char)(m[n] + 1);
                    if (m[n] > '9' && !visited.Contains(n))
                        FlashPos(m, n, visited);
                }
        }

        static int StepMap(Map m)
        {
            HashSet<Pos> visited = new HashSet<Pos>();
            foreach (Pos p in m.Positions())
                m[p] = (char) (m[p] + 1);
            var flashed = m.Positions().Where(x => m[x] > '9').ToList();
            foreach (Pos p in flashed)
                if (!visited.Contains(p))
                    FlashPos(m, p, visited);
            foreach (Pos p in visited)
                m[p] = '0';
            return visited.Count;
        }

        public static Object PartA(string file)
        {
            Map m = Map.Build(ReadInput.Strings(Day, file));
            return Enumerable.Range(0, 100).Select(x => StepMap(m)).Sum();
        }

        public static Object PartB(string file)
        {
            Map m = Map.Build(ReadInput.Strings(Day, file));
            int n = 1;
            while (StepMap(m) < 100)
                n++;
            return n;
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()!); } }
    }
}
