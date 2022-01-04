using AdventOfCode;
using System.Reflection;
using System.Text;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day23
    {
        // Amphipod: Play game moving all amphipods back home

        record struct APos(byte x, byte y) : IComparable<APos>
        {
            public APos(Pos p) : this((byte)p.x, (byte)p.y) { }
            public APos(char x, char y) : this((byte)(x - 'E'), (byte)(y - 'E')) { }
            public int CompareTo(APos a) => (y != a.y) ? (y < a.y ? -1 : 1) : (x == a.x ? 0 : x < a.x ? -1 : 1);
        }
        record struct Amp(char c, APos p) : IComparable<Amp>
        {
            public Amp(Amp a) : this(a.c, a.p) { }
            public Amp(string s) : this(s[0], new APos(s[1], s[2])) { }
            public int CompareTo(Amp a) => p.CompareTo(a.p);
            public string Str() => new StringBuilder().Append(c).Append((char)('E' + p.x)).Append((char)('E' + p.y)).ToString();
        }
        record struct State(string Id)
        {
            public State(List<Amp> amps) : this(FromAmps(amps)) { }
            public static string FromAmps(List<Amp> amps)
            {
                var sb = new StringBuilder();
                amps.OrderBy(w => w).ToList().ForEach(w => sb.Append(w.Str()));
                return sb.ToString();
            }
            public static List<Amp> Replace(ref State s, APos from, APos to)
            {
                var amps = s.AllAmps();
                for (int i = 0; i < amps.Count; i++)
                    if (amps[i].p == from)
                    {
                        amps[i] = new Amp(amps[i]) { p = to };
                        break;
                    }
                return amps;
            }
            public bool Done()
            {
                for (int i = 0; i < Id.Length; i += 3)
                {
                    char c = Id[i];
                    byte x = (byte)(Id[i + 1] - 'E');
                    if ((c == 'A' && x != 3) || (c == 'B' && x != 5) || (c == 'C' && x != 7) || (c == 'D' && x != 9))
                        return false;
                }
                return true;
            }
            public List<Amp> AllAmps()
            {
                var res = new List<Amp>(Id.Length / 3);
                for (int i = 0; i < Id.Length; i += 3)
                    res.Add(new Amp(Id.Substring(i, 3)));
                return res;
            }
            public List<APos> AllAPos()
            {
                var res = new List<APos>(Id.Length / 3);
                for (int i = 0; i < Id.Length; i += 3)
                    res.Add(new APos(Id[i + 1], Id[i + 2]));
                return res;
            }
            public void AddAnyOut(List<Amp> list, int x, char c)
            {
                int idx1 = -1, idx2 = -1;
                char cx = (char)('E' + x);
                for (int i = 0; i < Id.Length && idx2 < 0; i += 3)
                {
                    if (Id[i + 1] == cx && idx1 < 0)
                        idx1 = i;
                    if (Id[i + 1] == cx && Id[i] != c)
                        idx2 = i;
                }
                if (idx2 >= 0)
                    list.Add(new Amp(Id.Substring(idx1, 3)));
            }
            public List<Amp> MovingOut()
            {
                var l = new List<Amp>();
                AddAnyOut(l, 3, 'A');
                AddAnyOut(l, 5, 'B');
                AddAnyOut(l, 7, 'C');
                AddAnyOut(l, 9, 'D');
                return l;
            }
        }
        static Object Play(string file, bool partB)
        {
            var ls = File.ReadAllLines(ReadInput.GetPath(Day, file));
            var input = ls.Select(s => s.PadRight(13)).ToList();
            if (partB)
                input.InsertRange(3, new[] { "  #D#C#B#A#  ", "  #D#B#A#C#  " });
            int ymax = partB ? 5 : 3;
            var m = Map.Build(input);
            m.Print();
            var players = "ABCD";
            var mult = new Dictionary<char, int> { ['A'] = 1, ['B'] = 10, ['C'] = 100, ['D'] = 1000 };
            var hallway = m.Positions().Where(p => m[p] == '.');
            var allHomes = m.Positions().Where(p => players.Contains(m[p])).ToList();
            var homes = new Dictionary<char, List<APos>>();
            foreach (var (c, i) in players.ToList().WithIndex())
                homes[c] = allHomes.Where(p => p.x == i * 2 + 3).Select(p => new APos(p)).ToList();
            var xHomes = allHomes.Select(p => p.x).ToHashSet();
            var hallwayStops = hallway.Where(p => !xHomes.Contains(p.x)).Select(p => new APos(p)).ToList();
            var world = hallway.Union(allHomes).ToList();
            var gameStates = new PriorityQueue<State, int>();
            gameStates.Enqueue(Id3(m), 0);
            var gamesPlayed = new Dictionary<State, int>() { [Id3(m)] = 0 };
            allHomes.ForEach(p => m[p] = '.');
            int minEnergy = int.MaxValue;
            static APos[] Neighbours4(APos p) => new APos[]
            {
                new APos((byte)(p.x + 1), p.y),
                new APos((byte)(p.x - 1), p.y),
                new APos(p.x, (byte)(p.y + 1)),
                new APos(p.x, (byte)(p.y - 1))
            };
            List<(APos, int)> Reachable(ref State state, Amp start, List<APos> home, bool onlyGoHome)
            {
                var PlayersPos = state.AllAPos().ToHashSet();
                var canReach = new List<(APos p, int s)>();
                var been = new HashSet<APos>();
                var toTry = new List<(APos, int)>() { (start.p, 0) };
                while (toTry.Any())
                {
                    foreach ((APos p, int s) in toTry)
                    {
                        been.Add(p);
                        foreach (APos n in Neighbours4(p))
                        {
                            bool bHomePos = (n.x == 3 || n.x == 5 || n.x == 7 || n.x == 9) && (n.y > 1 && n.y <= ymax);
                            bool bHallPos = n.y == 1 && (n.x >= 1 && n.x <= 11);
                            if ((bHomePos || bHallPos) && !been.Contains(n) && !PlayersPos.Contains(n))
                                canReach.Add((n, s + 1));
                        }
                    }
                    toTry = canReach.Where(a => !been.Contains(a.p)).ToList();
                }
                //bool allowGoHome1 = home.All(w => m0[w] == '.' || m0[w] == m0[start]) &&
                //    home.Any(w => m0[w] == '.') && !home.Contains(start);
                //bool allowGoHome2 = state.Items.All(w => w.p.x != home[0].x || w.c == player) && start.x != home[0].x;
                var amps = state.AllAmps();
                bool allowGoHome = amps.All(w => w.p.x != home[0].x || w.c == start.c) && start.p.x != home[0].x;
                var allowed = new List<APos>();
                if (!onlyGoHome)
                    allowed.AddRange(hallwayStops!);
                if (allowGoHome)
                    allowed.AddRange(home);
                return canReach.Where(w => allowed.Contains(w.p)).ToList();
            }
            State Id3(Map m)
            {
                var pos = world!.Where(w => players.Contains(m[w]));
                return new State(pos.Select(p => new Amp(m[p], new APos(p))).ToList());
            }
            int nNewGames = 0;
            int nBetterGames = 0;
            int nOldGames = 0;
            int nGamesTotal = 0;
            bool MovePlayer(IEnumerable<Amp> toMove, ref State state, int score, bool onlyGoHome)
            {
                int nGoodBefore = nNewGames + nBetterGames;
                foreach (var amp in toMove)
                {
                    var r = Reachable(ref state, amp, homes![amp.c], onlyGoHome);
                    foreach ((APos p, int s) in r)
                    {
                        State newState = new(State.Replace(ref state, amp.p, p));
                        int newScore = score + s * mult![amp.c];
                        bool playedBefore = gamesPlayed!.ContainsKey(newState);
                        if (!playedBefore || gamesPlayed[newState] > newScore)
                        {
                            //m2.Print();
                            gameStates!.Enqueue(newState, newScore);
                            gamesPlayed[newState] = newScore;
                            if (!playedBefore)
                                nNewGames++;
                            else
                                nBetterGames++;
                        }
                        else
                        {
                            nOldGames++;
                        }
                    }
                }
                return nNewGames + nBetterGames > nGoodBefore;
            }
            while (gameStates.TryDequeue(out State state, out int score))
            {
                nGamesTotal++;
                if (score >= minEnergy)
                    continue;
                if (state.Done())
                    minEnergy = Math.Min(minEnergy, score);
                else
                {
                    //bool keepOn = true;
                    //while (keepOn)
                    //{
                    //    var movingIn = state.AllAmps().Where(w => w.y == 1);
                    //    keepOn = MovePlayer(movingIn, ref state, score, true);
                    //}
                    var movingIn = state.AllAmps().Where(w => w.p.y == 1);
                    MovePlayer(movingIn, ref state, score, true);
                    var movingOut = state.MovingOut();
                    MovePlayer(movingOut, ref state, score, false);
                }
                if (nGamesTotal % 10000 == 0)
                {
                    Console.WriteLine("Total: {0}, new: {1}, better: {2}, old: {3}, current score: {4}",
                        nGamesTotal, nNewGames, nBetterGames, nOldGames, score);
                    nNewGames = 0;
                    nBetterGames = 0;
                    nOldGames = 0;
                    //Console.WriteLine(state.ToString());
                }
            }
            Console.WriteLine("Total: {0}", nGamesTotal);
            return minEnergy;
        }
        public static (Object a, Object b) DoPuzzle(string file) =>
            (Play(file, false), 0); // Play(file, true));
        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
