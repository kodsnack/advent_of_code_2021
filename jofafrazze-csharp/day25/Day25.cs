using AdventOfCode;
using System.Reflection;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day25
    {
        // Sea Cucumber: Herds moving in two different steps

        public static (Object a, Object b) DoPuzzle(string file)
        {
            var m2 = Map.Build(File.ReadAllLines(ReadInput.GetPath(Day, file)));
            int iter = 0;
            Map m = new(0, 0, ' ');
            while (m2 != m)
            {
                m = m2;
                iter++;
                Map m1 = new(m);
                foreach (Pos p in m1.Positions().Where(p => m1[p] == '>').ToList())
                {
                    Pos np = new((p.x + 1) % m1.width, p.y);
                    if (m[np] == '.')
                        m1.Switch(p, np);
                }
                m2 = new(m1);
                foreach (Pos p in m2.Positions().Where(p => m2[p] == 'v').ToList())
                {
                    Pos np = new(p.x, (p.y + 1) % m.height);
                    if (m1[np] == '.')
                        m2.Switch(p, np);
                }
            }
            return (iter, 0);
        }
        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
