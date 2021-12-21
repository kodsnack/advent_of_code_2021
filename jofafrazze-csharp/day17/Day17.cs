using AdventOfCode;
using System.Reflection;

namespace aoc
{
    public class Day17
    {
        // Trick Shot: Calculate initial speeds for projectile trajectories

        static int x1, x2, y1, y2;
        static void ReadData(string file) =>
            (x1, x2, y1, y2) = Extract.Ints(File.ReadAllLines(ReadInput.GetPath(Day, file))[0]);

        static (bool ok, int yTop) Trajectory(int xv0, int yv0)
        {
            int n = 0, ymax = int.MinValue, x = 0, y = 0, xv = xv0, yv = yv0;
            while (x <= x2 && y >= y1)
            {
                x += xv;
                y += yv;
                xv = Math.Max(xv - 1, 0);
                yv -= 1;
                ymax = Math.Max(y, ymax);
                if (x >= x1 && x <= x2 && y >= y1 && y <= y2)
                    n++;
            }
            return (n > 0, ymax);
        }

        public static (int n, int ymax) Part(string file)
        {
            ReadData(file);
            int n = 0, ymax = int.MinValue;
            for (int x = 1; x <= x2; x++)
                for (int y = y1; y <= 500; y++)
                {
                    (bool ok, int yhi) = Trajectory(x, y);
                    n += ok ? 1 : 0;
                    if (ok && yhi > ymax)
                        ymax = yhi;
                }
            return (n, ymax);
        }
        public static Object PartA(string file) => Part(file).ymax;
        public static Object PartB(string file) => Part(file).n;
        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
