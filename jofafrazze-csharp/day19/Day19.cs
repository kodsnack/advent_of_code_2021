using AdventOfCode;
using System.Reflection;
using Pos = AdventOfCode.GenericPosition3D<int>;

namespace aoc
{
    public class Day19
    {
        // Beacon Scanner: Map cloud of points onto other clouds

        static List<List<Pos>> ReadData(string file)
        {
            var ret = new List<List<Pos>>();
            var list = new List<Pos>();
            foreach (var s in File.ReadAllLines(ReadInput.GetPath(Day, file)))
            {
                var v = s.Split(',');
                if (s.Contains(','))
                    list.Add(new Pos(int.Parse(v[0]), int.Parse(v[1]), int.Parse(v[2])));
                else if (list.Count > 0)
                {
                    ret.Add(list);
                    list = new List<Pos>();
                }
            }
            if (list.Count > 0)
                ret.Add(list);
            return ret;
        }
        static Pos RotateX90(Pos p) => new(p.x, -p.z, p.y);
        static Pos FlipX(Pos p) => new(-p.x, p.y, -p.z);
        static Pos Y2X(Pos p) => new(p.y, -p.x, p.z);
        static Pos Z2X(Pos p) => new(p.z, p.y, -p.x);
        static List<List<Pos>> Permutations(List<Pos> pos)
        {
            var y2x = pos.Select(a => Y2X(a)).ToList();
            var z2x = pos.Select(a => Z2X(a)).ToList();
            var ret = new List<List<Pos>>() { pos, y2x, z2x };
            foreach (var l in new List<List<Pos>>(ret))
                ret.Add(l.Select(a => FlipX(a)).ToList());
            foreach (var l in new List<List<Pos>>(ret))
            {
                ret.Add(l.Select(a => RotateX90(a)).ToList());
                ret.Add(ret.Last().Select(a => RotateX90(a)).ToList());
                ret.Add(ret.Last().Select(a => RotateX90(a)).ToList());
            }
            return ret;
        }

        public static (Object, Object) DoPuzzle(string file)
        {
            var w = ReadData(file);
            var beacons = w[0].ToHashSet();
            var scanners = new HashSet<Pos>() { new Pos() };
            var todo = w.Skip(1).Select(a => Permutations(a)).ToList();
            while (todo.Count > 0)
            {
                var scannerPerms = todo[0];
                todo.RemoveAt(0);
                bool found = false;
                foreach (var perm in scannerPerms)
                {
                    var deltas = new Dictionary<Pos, int>();
                    foreach (var sp in perm)
                        foreach (var wp in beacons)
                            deltas.Inc(wp - sp, 1);
                    (Pos d, int n) = deltas.ToList().OrderBy(a => a.Value).Last();
                    if (n >= 12)
                    {
                        beacons.UnionWith(perm.Select(a => a + d));
                        scanners.Add(d);
                        found = true;
                        break;
                    }
                }
                if (!found)
                    todo.Add(scannerPerms);
            }
            int max = scanners.SelectMany(w => scanners, (a, b) => a.ManhattanDistance(b)).Max();
            return (beacons.Count, max);
        }
        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
