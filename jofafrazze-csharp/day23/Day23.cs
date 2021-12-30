using AdventOfCode;
using System.Reflection;
using System.Text;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day23
    {
        // Amphipod: Play game moving all amphipods back home

        static Object Play(string file, bool partB)
        {
            var ls = File.ReadAllLines(ReadInput.GetPath(Day, file));
            int maxLen = ls.Select(s => s.Length).Max();
            var input = ls.Select(s => s.PadRight(maxLen)).ToList();
            if (partB)
            {
                input.Insert(3, "  #D#C#B#A#  ");
                input.Insert(4, "  #D#B#A#C#  ");
            }
            var m0 = Map.Build(input);
            m0.Print();
            var players = "ABCD";
            var mult = new Dictionary<char, int> { ['A'] = 1, ['B'] = 10, ['C'] = 100, ['D'] = 1000 };
            var hallway = m0.Positions().Where(p => m0[p] == '.');
            var homes = new Dictionary<char, List<Pos>>();
            homes['A'] = m0.Positions().Where(p => players.Contains(m0[p]) && p.x == 3).ToList();
            homes['B'] = m0.Positions().Where(p => players.Contains(m0[p]) && p.x == 5).ToList();
            homes['C'] = m0.Positions().Where(p => players.Contains(m0[p]) && p.x == 7).ToList();
            homes['D'] = m0.Positions().Where(p => players.Contains(m0[p]) && p.x == 9).ToList();
            var allHomes = homes.SelectMany(w => w.Value).ToHashSet();
            var xHomes = allHomes.Select(p => p.x).ToHashSet();
            var hallwayStops = hallway.Where(p => !xHomes.Contains(p.x)).ToList();
            var gameStates = new PriorityQueue<Map, int>();
            gameStates.Enqueue(m0, 0);
            var gamesPlayed = new Dictionary<string, int>() { [Id(m0)] = 0 };
            int minEnergy = int.MaxValue;
            List<(Pos, int)> Reachable(Map m, Pos start, List<Pos> home, bool onlyGoHome)
            {
                var canReach = new List<(Pos p, int s)>();
                var been = new HashSet<Pos>();
                var toTry = new List<(Pos, int)>() { (start, 0) };
                while (toTry.Any())
                {
                    foreach ((Pos p, int s) in toTry)
                    {
                        been.Add(p);
                        foreach (Pos n in CoordsRC.Neighbours4(p))
                        {
                            if (m[n] == '.' && !been.Contains(n))
                            {
                                canReach.Add((n, s + 1));
                            }
                        }
                    }
                    toTry = canReach.Where(a => !been.Contains(a.Item1)).ToList();
                }
                bool allowGoHome = home.All(w => m[w] == '.' || m[w] == m[start]) &&
                    home.Any(w => m[w] == '.') && !home.Contains(start);
                var allowed = new List<Pos>();
                if (!onlyGoHome)
                    allowed.AddRange(hallwayStops);
                if (allowGoHome)
                {
                    var hPos = home.Where(w => m[w] == '.').Last();
                    allowed.Add(hPos);
                    //if (hPos.y == 2 && canReach.Any(w => w.p == hPos))
                    //    m.Print();
                }
                return canReach.Where(w => allowed.Contains(w.p)).ToList();
            }
            string Id(Map m)
            {
                var a = m.Positions().Where(w => players!.Contains(m[w])).Select(w => (m[w], w));
                StringBuilder sb = new StringBuilder();
                var b = a.OrderBy(w => w.Item1).ThenBy(w => w.Item2);
                foreach ((char c, Pos p) in b)
                    sb.Append(c).Append(p.x).Append(',').Append(p.y);
                return sb.ToString();
            }
            while (gameStates.TryDequeue(out Map? m1, out int score))
            {
                if (score >= minEnergy)
                    continue;
                //Console.WriteLine("Testing {0} games", gameStates.Count);
                bool done = true;
                foreach ((char c, var h) in homes)
                    foreach(var p in h)
                        done &= (m1[p] == c);
                if (done)
                {
                    minEnergy = Math.Min(minEnergy, score);
                    Console.WriteLine("New lowest energy: {0}", minEnergy);
                }
                else
                {
                    //if (m1.data[1, 1] == 'A' && m1.data[2, 1] == 'A' // 10
                    //    && m1.data[5, 3] == 'B' // 60
                    //    && m1.data[10, 1] == 'D' // 2060
                    //    && m1.data[9, 3] == 'D' // 8560
                    //    && m1.data[7, 3] == 'C' // 8060
                    //    && m1.data[7, 2] == 'C' // 9460
                    //    && m1.data[5, 2] == 'B')
                    //{
                    //    m1.Print();
                    //    Console.WriteLine("Score now: {0}", score);
                    //}
                    var movingOut = allHomes.Where(p => players.Contains(m1[p]) && m1[p + CoordsRC.goUp] == '.');
                    foreach (var amp in movingOut)
                    {
                        var r = Reachable(m1, amp, homes[m1[amp]], false);
                        foreach ((Pos p, int s) in r)
                        {
                            Map m2 = new(m1);
                            m2[p] = m1[amp];
                            m2[amp] = '.';
                            int newScore = score + s * mult[m1[amp]];
                            var id = Id(m2);
                            if (!gamesPlayed.ContainsKey(id) || gamesPlayed[id] > newScore)
                            {
                                //m2.Print();
                                gameStates.Enqueue(m2, newScore);
                                gamesPlayed[id] = newScore;
                            }
                        }
                    }
                    //m1.Print();
                    var movingIn = hallwayStops.Where(p => m1[p] != '.');
                    foreach (var amp in movingIn)
                    {
                        var r = Reachable(m1, amp, homes[m1[amp]], true);
                        foreach ((Pos p, int s) in r)
                        {
                            Map m2 = new(m1);
                            m2[p] = m1[amp];
                            m2[amp] = '.';
                            int newScore = score + s * mult[m1[amp]];
                            var id = Id(m2);
                            if (!gamesPlayed.ContainsKey(id) || gamesPlayed[id] > newScore)
                            {
                                //m2.Print();
                                gameStates.Enqueue(m2, newScore);
                                gamesPlayed[id] = newScore;
                            }
                        }
                    }
                }
            }
            return minEnergy;
        }
        public static (Object a, Object b) DoPuzzle(string file) => 
            (Play(file, false), Play(file, true));
        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
