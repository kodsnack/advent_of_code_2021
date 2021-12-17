using System.Reflection;
using AdventOfCode;

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
            bool ok = false;
            int yTop = int.MinValue;
            int x = 0, y = 0, xv = xv0, yv = yv0;
            while (x <= x2 && y >= y1)
            {
                x += xv;
                y += yv;
                xv = Math.Max(xv - 1, 0);
                yv -= 1;
                yTop = Math.Max(y, yTop);
                if (x >= x1 && x <= x2 && y >= y1 && y <= y2)
                    ok = true;
            }
            return (ok, yTop);
        }

        public static (int n, int yMax) Part(string file)
        {
            ReadData(file);
            int n = 0, yMax = int.MinValue;
            for (int x = 1; x <= x2; x++)
                for (int y = y1; y <= 500; y++)
                {
                    (bool ok, int yTop) = Trajectory(x, y);
                    n += ok ? 1 : 0;
                    if (ok && yTop > yMax)
                        yMax = yTop;
                }
            return (n, yMax);
        }
        public static Object PartA(string file) => Part(file).yMax;
        public static Object PartB(string file) => Part(file).n;

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
