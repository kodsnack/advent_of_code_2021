using AdventOfCode;
using System.Reflection;
using System.Text;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day23
    {
        // Amphipod: Play game moving all amphipods back home

        static readonly string playerChar = "ABCD.";
        static readonly int Empty = 4;
        static readonly int[] mult = new int[] { 1, 10, 100, 1000 };
        static List<Pos> idx2Pos = new();
        static int[,] distPos2Pos = new int[,] { { } };
        record struct StateId(long Hall, long Rooms);
        sealed record class State(int N, StateId Id, byte[] Board)
        {
            // Board lenghts: Each room = N, hall = 11
            // Board index: room A = 0, room B = N, room C = 2N, room D = 3N, hall = 4N
            public State(byte[] board) : this((board.Length - 11) / 4, CreateId(board), board) { }
            public static StateId CreateId(byte[] board)
            {
                long hall = 0, rooms = 0;
                for (int i = board.Length - 11; i < board.Length; i++)
                    hall = hall << 3 | board[i];
                for (int i = 0; i < board.Length - 11; i++)
                    rooms = rooms << 3 | board[i];
                return new StateId(hall, rooms);
            }
            public bool Equals(State? other) => other is not null && Id.Equals(other.Id);
            public override int GetHashCode() => Id.GetHashCode();
            public bool Done()
            {
                for (int i = 0; i < Board.Length - 11; i++)
                    if (Board[i] != i / N)
                        return false;
                return true;

            }
            public bool EvacuatingRoom(int r)
            {
                for (int i = r * N; i < r * N + N; i++)
                    if (Board[i] != r && Board[i] != Empty)
                        return true;
                return false;
            }
            public int NInHome(int r)
            {
                int n = 0;
                for (int i = r * N; i < r * N + N; i++)
                    if (Board[i] == r)
                        n++;
                return n;
            }
            public List<int> MoveInCandidates()
            {
                var l = new List<int>();
                for (int i = 4 * N; i < Board.Length; i++)
                    if (Board[i] != Empty)
                        l.Add(i);
                return l;
            }
            public void AddPlayerMovingOut(List<int> list, int r)
            {
                if (!EvacuatingRoom(r))
                    return;
                for (int i = r * N; true; i++)
                    if (Board[i] != Empty)
                    {
                        list.Add(i);
                        break;
                    }
            }
            public List<int> MoveOutCandidates()
            {
                var l = new List<int>();
                AddPlayerMovingOut(l, 0);
                AddPlayerMovingOut(l, 1);
                AddPlayerMovingOut(l, 2);
                AddPlayerMovingOut(l, 3);
                return l;
            }
            public string PrintToString(Map m0)
            {
                Map m = new(m0);
                for (int i = 0; i < Board.Length; i++)
                    m[idx2Pos[i]] = playerChar[Board[i]];
                return m.PrintToString();
            }
            public string PrintToCompactString()
            {
                var sb = new StringBuilder();
                for (int i = 4 * N; i < Board.Length; i++)
                    sb.Append(playerChar[Board[i]]);
                sb.Append(' ');
                for (int r = 0; r < 4; r++)
                {
                    sb.Append('[');
                    for (int i = 0; i < N; i++)
                        sb.Append(playerChar[Board[r * N + i]]);
                    sb.Append(']');
                }
                return sb.ToString();
            }
            public int EstimateRemainingCost() // Must not overestimate cost
            {
                int cost = 0;
                bool[] evac = new bool[4];
                int[] roomDepth = new int[4];
                for (int r = 0; r < 4; r++)
                {
                    evac[r] = EvacuatingRoom(r);
                    roomDepth[r] = N - (evac[r] ? 0 : NInHome(r)) - 1;
                }
                for (int i = 0; i < Board.Length; i++)
                {
                    int player = Board[i];
                    if (player != Empty && !(i < 4 * N && !evac[player]))
                        cost += distPos2Pos[i, player * N + roomDepth[player]--] * mult[player];
                }
                return cost;
            }
        }
        static void InitLookups(int N)
        {
            idx2Pos = new List<Pos>();
            for (int i = 0; i < N * 4; i++)
                idx2Pos.Add(new Pos(3 + i / N * 2, 2 + (i % N)));
            for (int i = 0; i < 11; i++)
                idx2Pos.Add(new Pos(i + 1, 1));
            distPos2Pos = new int[idx2Pos.Count, idx2Pos.Count];
            for (int i = 0; i < idx2Pos.Count; i++)
                for (int j = 0; j < idx2Pos.Count; j++)
                {
                    var pMid = new Pos(idx2Pos[i].x, 1);
                    distPos2Pos[i, j] = idx2Pos[i].ManhattanDistance(pMid) + pMid.ManhattanDistance(idx2Pos[j]);
                }
        }
        static Object Play(string file, bool partB)
        {
            int roomDepth = partB ? 4 : 2;
            InitLookups(roomDepth);
            var ls = File.ReadAllLines(ReadInput.GetPath(Day, file));
            var input = ls.Select(s => s.PadRight(13)).ToList();
            if (partB)
                input.InsertRange(3, new[] { "  #D#C#B#A#  ", "  #D#B#A#C#  " });
            var m = Map.Build(input);
            //m.Print();
            byte[] board = new byte[roomDepth * 4 + 11];
            for (int i = 0; i < board.Length; i++)
                board[i] = (byte)(i < roomDepth * 4 ? playerChar.IndexOf(m[idx2Pos[i]]) : Empty);
            var state0 = new State(board);
            var gameStates = new PriorityQueue<State, int>(new (State, int)[] { (state0, 0) });
            var gamesPlayed = new Dictionary<State, (int score, State? prev)>() { [state0] = (0, null) };
            m.Positions().Where(p => !" #.".Contains(m[p])).ToList().ForEach(p => m[p] = '.');
            List<(int idx, int cost)> Reachable(State s, int pIdx)
            {
                var canReach = new List<(int idx, int cost)>();
                int player = s.Board[pIdx];
                void GoDownHome(State state, int curIdx)
                {
                    int roomBottomIdx = curIdx + state.N - 1;
                    while (curIdx < roomBottomIdx && state.Board[curIdx + 1] == Empty)
                        curIdx++;
                    canReach!.Add((curIdx, distPos2Pos[pIdx, curIdx]));
                }
                bool gotHome = false;
                int hallIdx0 = 4 * s.N;
                int homeIdx0 = player * s.N;
                void GoSideways(State state, int curIdx, int dir, bool stopInHallway, int pHomeHallIdx = -1)
                {
                    int endIdx = dir < 0 ? hallIdx0 - 1 : hallIdx0 + 11;
                    curIdx += dir;
                    while (curIdx != endIdx && state.Board[curIdx] == Empty)
                    {
                        if (stopInHallway && (curIdx <= hallIdx0 + 1 || curIdx >= hallIdx0 + 9 || (curIdx - hallIdx0) % 2 == 1))
                            canReach!.Add((curIdx, distPos2Pos[pIdx, curIdx]));
                        if (curIdx == pHomeHallIdx)
                        {
                            canReach!.Clear();
                            GoDownHome(state, homeIdx0);
                            gotHome = true;
                            return;
                        }
                        curIdx += dir;
                    }
                }
                int homeHallIdx = hallIdx0 + 2 + player * 2;
                bool playerInhome = pIdx >= player * s.N && pIdx < player * (s.N + 1);
                bool canGoHome = !playerInhome && !s.EvacuatingRoom(player);
                bool pInHall = pIdx >= 4 * s.N;
                int homeDir = pInHall ? (pIdx > homeHallIdx ? -1 : 1) : (pIdx > homeIdx0 ? -1 : 1);
                int enterHallIdx = 4 * s.N + 2 + pIdx / s.N * 2;
                if (pInHall && canGoHome)
                    GoSideways(s, pIdx, homeDir, false, homeHallIdx);
                else if (!pInHall)
                    GoSideways(s, enterHallIdx, homeDir, true, canGoHome ? homeHallIdx : -1);
                if (!pInHall && !gotHome)
                    GoSideways(s, enterHallIdx, homeDir > 0 ? -1 : 1, true, -1);
                return canReach;
            }
            int nNewGames = 0, nBetterGames = 0, nOldGames = 0, nGamesTotal = 0;
            bool MovePlayer(IEnumerable<int> toMove, State state, int score)
            {
                int nGoodBefore = nNewGames + nBetterGames;
                foreach (var startIdx in toMove)
                {
                    byte player = state.Board[startIdx];
                    var r = Reachable(state, startIdx);
                    foreach ((int idx, int s) in r)
                    {
                        byte[] newBoard = (byte[])state.Board.Clone();
                        newBoard[idx] = player;
                        newBoard[startIdx] = (byte)Empty;
                        State newState = new(newBoard);
                        int newScore = score + s * mult[player];
                        bool playedBefore = gamesPlayed!.ContainsKey(newState);
                        if (!playedBefore || gamesPlayed[newState].score > newScore)
                        {
                            //Console.WriteLine(newState.PrintToString(m));
                            gameStates!.Enqueue(newState, newScore + newState.EstimateRemainingCost());
                            gamesPlayed[newState] = (newScore, state);
                            nNewGames += playedBefore ? 0 : 1;
                            nBetterGames += playedBefore ? 1 : 0;
                        }
                        else
                            nOldGames++;
                    }
                }
                return nNewGames + nBetterGames > nGoodBefore;
            }
            State? state;
            int score = 0;
            while (gameStates.TryDequeue(out state, out int hscore))
            {
                nGamesTotal++;
                score = gamesPlayed[state].score;
                if (state.Done())
                    break;
                else
                {
                    MovePlayer(state.MoveInCandidates(), state, score);
                    MovePlayer(state.MoveOutCandidates(), state, score);
                }
                //if (nGamesTotal % 10000 == 0)
                //{
                //    Console.WriteLine("Total: {0}, new: {1}, better: {2}, old: {3}, score: {4}, hscore: {5}",
                //        nGamesTotal, nNewGames, nBetterGames, nOldGames, score, hscore);
                //    nNewGames = nBetterGames = nOldGames = 0;
                //}
            }
            //Console.WriteLine("Total: {0}, min energy: {1}", nGamesTotal, score);
            //var moves = new List<State>() { state! };
            //while (gamesPlayed[state!].prev != null)
            //    moves.Add(state = (State)gamesPlayed[state!].prev!);
            //foreach (var (s, i) in moves.AsEnumerable().Reverse().WithIndex())
            //    Console.WriteLine("{0,2}: {1}: {2,5}", i, s.PrintToCompactString(), gamesPlayed[s].score);
            return score;
        }
        public static (Object a, Object b) DoPuzzle(string file) =>
            (Play(file, false), Play(file, true));
        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
