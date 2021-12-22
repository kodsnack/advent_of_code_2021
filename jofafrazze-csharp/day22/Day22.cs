using AdventOfCode;
using System.Reflection;
using Pos = AdventOfCode.GenericPosition3D<int>;

namespace aoc
{
    public class Day22
    {
        // Reactor Reboot: Keep track of cubes and their intersections

        record struct Cube(bool on, int x1, int x2, int y1, int y2, int z1, int z2)
        {
            public Cube? Intersect(Cube c, bool ion) =>
                (x1 > c.x2 || x2 < c.x1 || y1 > c.y2 || y2 < c.y1 || z1 > c.z2 || z2 < c.z1) ? 
                null : new Cube(ion, 
                    Math.Max(x1, c.x1), Math.Min(x2, c.x2), 
                    Math.Max(y1, c.y1), Math.Min(y2, c.y2), 
                    Math.Max(z1, c.z1), Math.Min(z2, c.z2));
            public long Volume() => (x2 - x1 + 1L) * (y2 - y1 + 1) * (z2 - z1 + 1) * (on ? 1 : -1);
        }
        public static (Object a, Object b) DoPuzzle(string file)
        {
            var input = new List<Cube>();
            foreach (var s in File.ReadAllLines(ReadInput.GetPath(Day, file)))
            {
                var v = Extract.Ints(s);
                input.Add(new Cube(s[1] == 'n', v[0], v[1], v[2], v[3], v[4], v[5]));
            }
            var pos = new Dictionary<Pos, bool>();
            foreach (var c in input)
                if (c.x1 >= -50 && c.y1 >= -50 && c.z1 >= -50 && c.x2 <= 50 && c.y2 <= 50 && c.z2 <= 50)
                    for (int x = c.x1; x <= c.x2; x++)
                        for (int y = c.y1; y <= c.y2; y++)
                            for (int z = c.z1; z <= c.z2; z++)
                                pos[new(x, y, z)] = c.on;
            int a = pos.Where(d => d.Value).Count();
            var volumeCubes = new List<Cube>();
            foreach (var cube in input)
            {
                var newCubes = new List<Cube>();
                Cube? icube;
                foreach (var vcube in volumeCubes)
                    if ((icube = cube.Intersect(vcube, !vcube.on)) != null)
                        newCubes.Add((Cube)icube);
                if (cube.on)
                    newCubes.Add(cube);
                volumeCubes.AddRange(newCubes);
            }
            return (a, volumeCubes.Aggregate(0L, (a, x) => a + x.Volume()));
        }
        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
