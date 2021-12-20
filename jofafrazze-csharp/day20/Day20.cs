using System.Reflection;
using AdventOfCode;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day20
    {
        // Trench Map: Evolve infinite map ("image enhancement")

        static string key = "";
        static Map ReadData(string file)
        {
            var ls = File.ReadAllLines(ReadInput.GetPath(Day, file));
            key = ls[0];
            return Map.Build(ls.Skip(2).ToList());
        }
        static int Enhance(Map m, int iter)
        {
            m.Expand(iter, '.');
            //m.Print();
            for (int i = 0; i < iter; i++)
            {
                var m2 = new Map(m);
                char GetNum(ref Map t, Pos w)
                {
                    w.x = Math.Max(Math.Min(w.x, t.width - 1), 0);
                    w.y = Math.Max(Math.Min(w.y, t.height - 1), 0);
                    return t[w] == '#' ? '1' : '0';
                }
                foreach (var p in m.Positions())
                {
                    string s = "";
                    for (int y = -1; y <= 1; y++)
                        for (int x = -1; x <= 1; x++)
                            s += GetNum(ref m, p + new Pos(x, y));
                    int k = Convert.ToInt32(s, 2);
                    m2[p] = key[k];
                }
                m = m2;
                //m.Print();
            }
            return m.Positions().Where(a => m[a] == '#').Count();
        }
        public static (Object a, Object b) DoPuzzle(string file)
        {
            var m = ReadData(file);
            int a = Enhance(m, 2);
            int b = Enhance(m, 50);
            return (a, b);
        }

        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
