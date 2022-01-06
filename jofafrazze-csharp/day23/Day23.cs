using AdventOfCode;
using System.Reflection;
using System.Text;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day23
    {
        // Amphipod: Play game moving all amphipods back home

        //record struct StateId(long hall, long rooms);
        record struct Amp(char c, Pos p) : IComparable<Amp>
        {
            public Amp(Amp a) : this(a.c, a.p) { }
            public Amp(string s) : this(s[0], new Pos(s[1] - 'E', s[2] - 'E')) { }
            public int CompareTo(Amp a) => p.CompareTo(a.p);
            public string Str() => new StringBuilder().Append(c).Append((char)('E' + p.x)).Append((char)('E' + p.y)).ToString();
        }
        record struct State(string Id, Amp[] Amps)
        {
            public State(Amp[] amps) : this(CreateId(amps), amps) { }
            public static string CreateId(Amp[] amps)
            {
                var sb = new StringBuilder();
                for (int i = 0; i < amps.Length; i++)
                    sb.Append(amps[i].Str());
                return sb.ToString();
            }
            public static Amp[] Replace(Amp[] amps, Pos from, Pos to)
            {
                for (int i = 0; i < amps.Length; i++)
                    if (amps[i].p == from)
                    {
                        amps[i] = new Amp(amps[i]) { p = to };
                        break;
                    }
                Array.Sort(amps);
                return amps;
            }
            public bool Equals(State other) => Id.Equals(other.Id);
            public override int GetHashCode() => Id.GetHashCode();
            public bool Done() => Amps.All(a => a.p.x == xhome[a.c]);
            public bool Evacuating(char c) => Amps.Where(a => a.p.x == xhome[c]).Any(a => a.c != c);
            public int AmpsInHome(char c) => Amps.Where(a => a.p.x == xhome[c]).Count(a => a.c == c);
            public Amp GetFirstAmp(char c) => Amps.Where(a => a.p.x == xhome[c]).First();
            public List<Amp> MovingOut()
            {
                var l = new List<Amp>();
                if (Evacuating('A')) l.Add(GetFirstAmp('A'));
                if (Evacuating('B')) l.Add(GetFirstAmp('B'));
                if (Evacuating('C')) l.Add(GetFirstAmp('C'));
                if (Evacuating('D')) l.Add(GetFirstAmp('D'));
                return l;
            }
            public string PrintToString(Map m0)
            {
                Map m = new(m0);
                foreach (var amp in Amps)
                    m.data[amp.p.x, amp.p.y] = amp.c;
                return m.PrintToString();
            }
            public string PrintToCompactString(int index, int score)
            {
                int maxDepth = Id.Length / 12;
                var map = Amps.ToDictionary(w => w.p, w => w.c);
                var sb = new StringBuilder();
                sb.AppendFormat("{0,2}: ", index);
                for (int x = 1; x <= 11; x++)
                {
                    if (IsXHome(x))
                    {
                        sb.Append('[');
                        for (int y = 2; y <= maxDepth + 1; y++)
                            sb.Append(map.GetValueOrDefault(new Pos(x, y), '.'));
                        sb.Append(']');
                    }
                    else
                        sb.Append(map.GetValueOrDefault(new Pos(x, 1), '.'));
                }
                return sb.AppendFormat(": {0,5}", score).ToString();
            }
            public int EstimateRemainingCost() // Must not overestimate cost
            {
                int maxDepth = Id.Length / 12;
                int cost = 0;
                Dictionary<int, bool> evac = new();
                int[] distHome = new int[10];
                foreach (char c in "ABCD")
                {
                    bool e = Evacuating(c);
                    evac[xhome[c]] = e;
                    distHome[xhome[c]] = maxDepth - (e ? 0 : AmpsInHome(c));
                }
                foreach (var a in Amps)
                    if (!(IsXHome(a.p.x) && !evac[a.p.x]))
                        cost += (a.p.y - 1 + Math.Abs(a.p.x - xhome[a.c]) + distHome[xhome[a.c]]--) * mult[a.c];
                return cost;
            }
        }
        static bool IsXHome(int x) => x == 3 || x == 5 || x == 7 || x == 9;
        static readonly Dictionary<char, int> xhome = new() { ['A'] = 3, ['B'] = 5, ['C'] = 7, ['D'] = 9 };
        static readonly Dictionary<char, int> mult = new() { ['A'] = 1, ['B'] = 10, ['C'] = 100, ['D'] = 1000 };
        static Object Play(string file, bool partB)
        {
            var ls = File.ReadAllLines(ReadInput.GetPath(Day, file));
            var input = ls.Select(s => s.PadRight(13)).ToList();
            if (partB)
                input.InsertRange(3, new[] { "  #D#C#B#A#  ", "  #D#B#A#C#  " });
            int ymax = partB ? 5 : 3;
            var m = Map.Build(input);
            m.Print();
            var gameStates = new PriorityQueue<State, int>();
            gameStates.Enqueue(Id3(m), 0);
            var gamesPlayed = new Dictionary<State, (int score, State? prev)>() { [Id3(m)] = (0, null) };
            m.Positions().Where(p => !" #.".Contains(m[p])).ToList().ForEach(p => m[p] = '.');
            List<(Pos, int)> Reachable(ref State state, Amp start)
            {
                var playersPos = state.Amps.Select(w => w.p).ToHashSet();
                var canReach = new List<(Pos p, int s)>();
                void GoDownHome(Pos p, int dist)
                {
                    Pos nextp = p;
                    nextp.y += 1;
                    while (nextp.y <= ymax && !playersPos!.Contains(nextp))
                    {
                        p = nextp;
                        nextp.y += 1;
                    }
                    canReach!.Add((p, dist + p.y - 1));
                }
                bool gotHome = false;
                void GoSideways(Pos p, int dir, bool stopInHallway, int xhome = -1)
                {
                    int end = dir < 0 ? 0 : 12;
                    p.x += dir;
                    while (p.x != end && !playersPos!.Contains(p))
                    {
                        if (stopInHallway && (p.x <= 2 || p.x >= 10 || p.x % 2 == 0))
                            canReach!.Add((p, p.ManhattanDistance(start.p)));
                        if (p.x == xhome)
                        {
                            canReach!.Clear();
                            GoDownHome(p, p.ManhattanDistance(start.p));
                            gotHome = true;
                            return;
                        }
                        p.x += dir;
                    }
                }
                int sxhome = xhome[start.c];
                bool canGoHome = (start.p.x != sxhome) && !state.Evacuating(start.c);
                int homeDir = start.p.x > sxhome ? -1 : 1;
                if (start.p.y == 1 && canGoHome)
                    GoSideways(start.p, homeDir, false, sxhome);
                else if (start.p.y > 1)
                {
                    Pos p = new Pos(start.p.x, 1);
                    GoSideways(p, homeDir, true, canGoHome ? sxhome : -1);
                    if (!gotHome)
                        GoSideways(p, homeDir > 0 ? -1 : 1, true, -1);
                }
                return canReach;
            }
            State Id3(Map m)
            {
                var pos = m.Positions().Where(w => "ABCD".Contains(m[w]));
                return new State(pos.Select(p => new Amp(m[p], p)).OrderBy(w => w).ToArray());
            }
            int nNewGames = 0;
            int nBetterGames = 0;
            int nOldGames = 0;
            int nGamesTotal = 0;
            bool MovePlayer(IEnumerable<Amp> toMove, ref State state, int score)
            {
                int nGoodBefore = nNewGames + nBetterGames;
                foreach (var amp in toMove)
                {
                    var r = Reachable(ref state, amp);
                    foreach ((Pos p, int s) in r)
                    {
                        Amp[] newAmps = (Amp[])state.Amps.Clone();
                        State newState = new(State.Replace(newAmps, amp.p, p));
                        int newScore = score + s * mult![amp.c];
                        bool playedBefore = gamesPlayed!.ContainsKey(newState);
                        if (!playedBefore || gamesPlayed[newState].score > newScore)
                        {
                            //Console.WriteLine(newState.PrintToString(m));
                            int h = newState.EstimateRemainingCost();
                            gameStates!.Enqueue(newState, newScore + h);
                            gamesPlayed[newState] = (newScore, state);
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
            State state;
            int score = 0;
            while (gameStates.TryDequeue(out state, out int hscore))
            {
                nGamesTotal++;
                score = gamesPlayed[state].score;
                if (state.Done())
                    break;
                else
                {
                    //bool keepOn = true;
                    //while (keepOn)
                    //{
                    //    var movingIn = state.Amps.Where(w => w.p.y == 1);
                    //    keepOn = MovePlayer(movingIn, ref state, score);
                    //}
                    var movingIn = state.Amps.Where(w => w.p.y == 1);
                    MovePlayer(movingIn, ref state, score);
                    var movingOut = state.MovingOut();
                    MovePlayer(movingOut, ref state, score);
                }
                if (nGamesTotal % 100000 == 0)
                {
                    Console.WriteLine("Total: {0}, new: {1}, better: {2}, old: {3}, score: {4}, hscore: {5}",
                        nGamesTotal, nNewGames, nBetterGames, nOldGames, score, hscore);
                    nNewGames = 0;
                    nBetterGames = 0;
                    nOldGames = 0;
                    //Console.WriteLine(state.ToString());
                }
            }
            Console.WriteLine("Total: {0}, min energy: {1}", nGamesTotal, score);
            //var moves = new List<State>() { state };
            //var curState = state;
            //while (gamesPlayed[curState].prev != null)
            //{
            //    curState = (State)gamesPlayed[curState].prev!;
            //    moves.Add(curState);
            //}
            //foreach (var (s, i) in moves.AsEnumerable().Reverse().WithIndex())
            //    Console.WriteLine(s.PrintToCompactString(i, gamesPlayed[s].score));
            return score;
        }
        public static (Object a, Object b) DoPuzzle(string file) =>
            (Play(file, false), Play(file, true));
        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
