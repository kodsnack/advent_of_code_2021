using System.Reflection;
using AdventOfCode;

namespace aoc
{
    public class Day17
    {
        // Today: Calculate initial speeds for projectile trajectories

        static void ReadData(string file)
        {
            string Strip(string s) => new string(s.Where(c => "-0123456789".Contains(c)).ToArray());
            var s = File.ReadAllLines(ReadInput.GetPath(Day, file))[0];
            var v = s.Split(" ");
            xmin = int.Parse(Strip(v[2].Split("..")[0]));
            xmax = int.Parse(Strip(v[2].Split("..")[1]));
            ymin = int.Parse(Strip(v[3].Split("..")[0]));
            ymax = int.Parse(Strip(v[3].Split("..")[1]));
        }

        static int xmin;
        static int xmax;
        static int ymin;
        static int ymax;
        static (bool ok, int yTop) DoIt(int xv0, int yv0)
        {
            bool ok = false;
            int yTop = int.MinValue;
            int x = 0;
            int y = 0;
            int xv = xv0;
            int yv = yv0;
            while (x <= xmax && y >= ymin)
            {
                x += xv;
                y += yv;
                if (xv > 0)
                    xv -= 1;
                yv -= 1;
                if (y > yTop)
                    yTop = y;
                if (x >= xmin && x <= xmax && y >= ymin && y <= ymax)
                    ok = true;
            }
            return (ok, yTop);
        }

        public static (int n, int yMax) Part(string file)
        {
            ReadData(file);
            int n = 0;
            int yMax = int.MinValue;
            for (int x = 1; x <= xmax; x++)
                for (int y = ymin; y <= 500; y++)
                {
                    (bool ok, int yTop) = DoIt(x, y);
                    n += ok ? 1 : 0;
                    if (ok && yTop > yMax)
                        yMax = yTop;
                }
            return (n, yMax);
        }
        public static Object PartA(string file) => Part(file).yMax;
        public static Object PartB(string file) => Part(file).n;

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod());
    }
}
