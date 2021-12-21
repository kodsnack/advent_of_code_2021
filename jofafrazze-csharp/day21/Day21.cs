using AdventOfCode;
using System.Reflection;

namespace aoc
{
    public class Day21
    {
        // Dirac Dice: Roll dice to play game, even in multiple universes

        static (int, int) ReadData(string file)
        {
            var ls = File.ReadAllLines(ReadInput.GetPath(Day, file));
            return (int.Parse(ls[0].Split(' ').Last()) - 1, int.Parse(ls[1].Split(' ').Last()) - 1);
        }
        static Object PartA(string file)
        {
            (int pos1, int pos2) = ReadData(file);
            int rolls = 0;
            int Roll(ref int d)
            {
                int a = d + 1;
                d = a % 100;
                rolls++;
                return a;
            }
            int Step(ref int pos, int steps)
            {
                pos = (pos + steps) % 10;
                return pos + 1;
            }
            int sa = 0, sb = 0, d = 0;
            while (sa < 1000 && sb < 1000)
            {
                sa += Step(ref pos1, Roll(ref d) + Roll(ref d) + Roll(ref d));
                if (sa < 1000)
                    sb += Step(ref pos2, Roll(ref d) + Roll(ref d) + Roll(ref d));
            }
            return Math.Min(sa, sb) * rolls;
        }
        static Object PartB(string file)
        {
            (int pos1, int pos2) = ReadData(file);
            // games[s1, s2, p1, p2, turn]
            long[,,,,] games = new long[31, 31, 10, 10, 2];
            games[0, 0, pos1, pos2, 0] = 1;  // Our starting state
            // Play all possible games
            for (int s1 = 0; s1 < 21; s1++)
                for (int s2 = 0; s2 < 21; s2++)
                    for (int p1 = 0; p1 < 10; p1++)
                        for (int p2 = 0; p2 < 10; p2++)
                            for (int r1 = 1; r1 <= 3; r1++)
                                for (int r2 = 1; r2 <= 3; r2++)
                                    for (int r3 = 1; r3 <= 3; r3++)
                                    {
                                        int steps = r1 + r2 + r3;
                                        int np1 = (p1 + steps) % 10;
                                        int ns1 = s1 + np1 + 1;
                                        int np2 = (p2 + steps) % 10;
                                        int ns2 = s2 + np2 + 1;
                                        games[ns1, s2, np1, p2, 1] += games[s1, s2, p1, p2, 0];
                                        games[s1, ns2, p1, np2, 0] += games[s1, s2, p1, p2, 1];
                                    }
            long Wins(int turn)
            {
                long w = 0;
                (int, int) losses = (0, 21);
                (int, int) wins = (21, 31);
                (int s1l, int s1h) = turn == 0 ? losses : wins; 
                (int s2l, int s2h) = turn == 0 ? wins : losses;
                for (int s1 = s1l; s1 < s1h; s1++)
                    for (int s2 = s2l; s2 < s2h; s2++)
                        for (int p1 = 0; p1 < 10; p1++)
                            for (int p2 = 0; p2 < 10; p2++)
                                w += games[s1, s2, p1, p2, turn];
                return w;
            }
            return Math.Max(Wins(0), Wins(1));
        }
        public static (Object, Object) DoPuzzle(string file) => (PartA(file), PartB(file));
        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
