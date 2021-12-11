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
    public class Day11
    {
        // Today: 

        static void FlashPos(Map m, Pos p, ref HashSet<Pos> visited)
        {
            visited.Add(p);
            foreach (Pos n in CoordsXY.Neighbours8(p))
                if (m.HasPosition(n))
                {
                    m[n] = (char)(m[n] + 1);
                    if (m[n] > '9' && !visited.Contains(n))
                        FlashPos(m, n, ref visited);
                }
        }

        static int StepMap(Map m)
        {
            HashSet<Pos> visited = new HashSet<Pos>();
            foreach (Pos p in m.Positions())
                m[p] = (char) (m[p] + 1);
            var flashed = m.Positions().Where(x => m[x] > '9').ToList();
            foreach (Pos p in flashed)
            {
                if (!visited.Contains(p))
                    FlashPos(m, p, ref visited);
            }
            foreach (Pos p in visited)
                m[p] = '0';
            return visited.Count;
        }

        public static Object PartA(string file)
        {
            Map m = Map.Build(ReadInput.Strings(Day, file));
            int sum = 0;
            for (int i = 0; i < 100; i++)
            {
                int a = StepMap(m);
                //m.Print();
                sum += a;
            }
            return sum;
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
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
