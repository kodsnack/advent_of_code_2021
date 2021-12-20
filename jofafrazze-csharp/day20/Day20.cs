using AdventOfCode;
using System.Reflection;

namespace aoc
{
    public class Day20
    {
        // Trench Map: Evolve infinite map ("image enhancement")

        static string key = "";
        static int Enhance(Map m, int iter)
        {
            char fill = '.';
            for (int i = 0; i < iter; i++)
            {
                m.Expand(1, fill);
                fill = (fill == '.') ? key[0] : key[511];
                var m2 = new Map(m);
                int GetNum(ref Map t, int x, int y) =>
                    t.data[Utils.Modulo(x, t.width), Utils.Modulo(y, t.height)] == '#' ? 1 : 0;
                foreach (var p in m.Positions())
                {
                    int k = 0;
                    for (int dy = -1; dy <= 1; dy++)
                        for (int dx = -1; dx <= 1; dx++)
                            k = k << 1 | GetNum(ref m, p.x + dx, p.y + dy);
                    m2[p] = key[k];
                }
                m = m2;
            }
            return m.Positions().Where(a => m[a] == '#').Count();
        }
        public static (Object a, Object b) DoPuzzle(string file)
        {
            var ls = File.ReadAllLines(ReadInput.GetPath(Day, file));
            key = ls[0];
            var m = Map.Build(ls.Skip(2).ToList());
            int a = Enhance(m, 2);
            int b = Enhance(m, 50);
            return (a, b);
        }
        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
