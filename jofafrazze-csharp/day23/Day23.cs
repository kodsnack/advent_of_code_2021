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
            public bool Evacuating(int x, char c)
            {
                char cx = (char)('E' + x);
                for (int i = 0; i < Id.Length; i += 3)
                    if (Id[i + 1] == cx && Id[i] != c)
                        return true;
                return false;
            }
            public Amp GetFirstAmp(int x)
            {
                char cx = (char)('E' + x);
                for (int i = 0; i < Id.Length; i += 3)
                    if (Id[i + 1] == cx)
                        return new Amp(Id.Substring(i, 3));
                throw new ArgumentOutOfRangeException();
            }
            public List<Amp> MovingOut()
            {
                var l = new List<Amp>();
                if (Evacuating(3, 'A')) l.Add(GetFirstAmp(3));
                if (Evacuating(5, 'B')) l.Add(GetFirstAmp(5));
                if (Evacuating(7, 'C')) l.Add(GetFirstAmp(7));
                if (Evacuating(9, 'D')) l.Add(GetFirstAmp(9));
                return l;
            }
            public string PrintToString(Map m0)
            {
                Map m = new(m0);
                foreach (var amp in AllAmps())
                    m.data[amp.p.x, amp.p.y] = amp.c;
                return m.PrintToString();
            }
            public string PrintToCompactString(int maxDepth, int index, int score)
            {
                var map = AllAmps().ToDictionary(w => w.p, w => w.c);
                var sb = new StringBuilder();
                sb.AppendFormat("{0,2}: ", index);
                for (int x = 1; x <= 11; x++)
                {
                    if (IsXHome(x))
                    {
                        sb.Append('[');
                        for (int y = 2; y <= maxDepth + 1; y++)
                            sb.Append(map.GetValueOrDefault(new APos((byte)x, (byte)y), '.'));
                        sb.Append(']');
                    }
                    else
                        sb.Append(map.GetValueOrDefault(new APos((byte)x, 1), '.'));
                }
                return sb.AppendFormat(": {0,5}", score).ToString();
            }
            public int EstimateRemainingCost(int maxDepth) // Must not overestimate cost
            {
                int cost = 0;
                Dictionary<int, bool> evac = new();
                foreach (char c in "ABCD")
                    evac[xhome[c]] = Evacuating(xhome[c], c);
                foreach (var a in AllAmps())
                    if (!(IsXHome(a.p.x) && !evac[a.p.x]))
                        cost += (a.p.y - 1 + Math.Abs(a.p.x - xhome[a.c]) + 1) * mult[a.c];
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
            int mDist(APos p1, APos p2) => Math.Abs(p1.x - p2.x) + Math.Abs(p1.y - p2.y);
            List<(APos, int)> Reachable(ref State state, Amp start)
            {
                var playersPos = state.AllAPos().ToHashSet();
                var canReach = new List<(APos p, int s)>();
                void GoDownHome(APos p, int dist)
                {
                    APos nextp = p;
                    nextp.y += 1;
                    while (nextp.y <= ymax && !playersPos!.Contains(nextp))
                    {
                        p = nextp;
                        nextp.y += 1;
                    }
                    canReach!.Add((p, dist + p.y - 1));
                }
                void GoSideways(APos p, int dir, bool stopInHallway, int xhome = -1)
                {
                    int end = dir < 0 ? 0 : 12;
                    p.x += (byte)dir;
                    while (p.x != end && !playersPos!.Contains(p))
                    {
                        if (stopInHallway && (p.x <= 2 || p.x >= 10 || p.x % 2 == 0))
                            canReach!.Add((p, mDist(start.p, p)));
                        if (p.x == xhome)
                            GoDownHome(p, mDist(start.p, p));
                        p.x += (byte)dir;
                    }
                }
                int sxhome = xhome[start.c];
                bool canGoHome = (start.p.x != sxhome) && !state.Evacuating(start.p.x, start.c);
                int homeDir = start.p.x > sxhome ? -1 : 1;
                if (start.p.y == 1 && canGoHome)
                    GoSideways(start.p, homeDir, false, sxhome);
                else if (start.p.y > 1)
                {
                    APos p = new APos(start.p.x, 1);
                    GoSideways(p, homeDir, true, canGoHome ? sxhome : -1);
                    GoSideways(p, homeDir > 0 ? -1 : 1, true, -1);
                }
                return canReach;
            }
            State Id3(Map m)
            {
                var pos = m.Positions().Where(w => "ABCD".Contains(m[w]));
                return new State(pos.Select(p => new Amp(m[p], new APos(p))).ToList());
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
                    foreach ((APos p, int s) in r)
                    {
                        State newState = new(State.Replace(ref state, amp.p, p));
                        int newScore = score + s * mult![amp.c];
                        bool playedBefore = gamesPlayed!.ContainsKey(newState);
                        if (!playedBefore || gamesPlayed[newState].score > newScore)
                        {
                            //Console.WriteLine(newState.PrintToString(m));
                            int h = newState.EstimateRemainingCost(ymax - 1);
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
                    bool keepOn = true;
                    while (keepOn)
                    {
                        var movingIn = state.AllAmps().Where(w => w.p.y == 1);
                        keepOn = MovePlayer(movingIn, ref state, score);
                    }
                    //var movingIn = state.AllAmps().Where(w => w.p.y == 1);
                    //MovePlayer(movingIn, ref state, score);
                    var movingOut = state.MovingOut();
                    MovePlayer(movingOut, ref state, score);
                }
                if (nGamesTotal % 300000 == 0)
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
            var moves = new List<State>() { state };
            var curState = state;
            while (gamesPlayed[curState].prev != null)
            {
                curState = (State)gamesPlayed[curState].prev!;
                moves.Add(curState);
            }
            foreach (var (s, i) in moves.AsEnumerable().Reverse().WithIndex())
                Console.WriteLine(s.PrintToCompactString(ymax - 1, i, gamesPlayed[s].score));
            return score;
        }
        public static (Object a, Object b) DoPuzzle(string file) =>
            (Play(file, false), Play(file, true));
        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
