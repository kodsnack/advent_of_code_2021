using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using AdventOfCode;

namespace day04
{
    public class Day04
    {
        static readonly string day = "day04";

        // Day 04: Play bingo with giant squid (no diagonals, RTFM!)

        static List<List<int>> ReadBoards()
        {
            StreamReader reader = File.OpenText(ReadInput.GetPath(day));
            var list = new List<List<int>>();
            var bingo = new List<int>();
            string line;
            reader.ReadLine();
            reader.ReadLine();
            while ((line = reader.ReadLine()) != null)
            {
                var ls = line.Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(int.Parse).ToList();
                bingo.AddRange(ls);
                if (ls.Count == 0)
                {
                    list.Add(bingo);
                    bingo = new List<int>();
                }
            }
            return list;
        }

        static List<int> ReadInts()
        {
            StreamReader reader = File.OpenText(ReadInput.GetPath(day));
            List<int> list = new List<int>();
            string line = reader.ReadLine();
            list.AddRange(line.Split(',').Select(int.Parse).ToList());
            return list;
        }

        static bool CheckStride(int pos, int stride, List<int> board, List<int> drawn)
        {
            for (int i = 0; i < 5; i++)
                if (!drawn.Contains(board[pos + i * stride]))
                    return false;
            return true;
        }

        static Func<T1, TRes> ApplyPartial<T1, T2, T3, T4, TRes>(Func<T1, T2, T3, T4, TRes> func, T2 t2, T3 t3, T4 t4)
        {
            return (t1) => func(t1, t2, t3, t4);
        }
        static bool CheckBingo(List<int> board, List<int> drawn)
        {
            Func<int, bool> fh = ApplyPartial<int, int, List<int>, List<int>, bool>(CheckStride, 1, board, drawn);
            Func<int, bool> fv = ApplyPartial<int, int, List<int>, List<int>, bool>(CheckStride, 5, board, drawn);
            return fv(0) || fv(1) || fv(2) || fv(3) || fv(4) || fh(0) || fh(5) || fh(10) || fh(15) || fh(20);
        }

        static Object PartA()
        {
            var boards = ReadBoards();
            var nums = ReadInts();
            var drawn = new List<int>();
            foreach (int i in nums)
            {
                drawn.Add(i);
                foreach (var b in boards)
                {
                    if (CheckBingo(b, drawn))
                        return b.Except(drawn).Sum() * i;
                }
            }
            return -1;
        }

        static Object PartB()
        {
            var boards = ReadBoards();
            var nums = ReadInts();
            var drawn = new List<int>();
            int ans = 0;
            foreach (int i in nums)
            {
                var nextBoards = new List<List<int>>();
                drawn.Add(i);
                foreach (var b in boards)
                {
                    if (CheckBingo(b, drawn))
                        ans = b.Except(drawn).Sum() * i;
                    else
                        nextBoards.Add(b);
                }
                boards = nextBoards;
                if (boards.Count == 0)
                    return ans;
            }
            return -1;
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
        static readonly int qa = 29440;
        static readonly int qb = 13884;
        public static bool Test() => (PartA().Equals(qa)) && (PartB().Equals(qb));
    }
}
