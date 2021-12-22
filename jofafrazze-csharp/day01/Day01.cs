using AdventOfCode;
using System;

namespace aoc
{
    public class Day01
    {
        static readonly string day = "day01";

        // Sonar Sweep: Count increments

        public static Object PartA(string file)
        {
            var input = ReadInput.Ints(day, file);
            int ans = 0;
            for (int i = 1; i < input.Count; i++)
                if (input[i] > input[i - 1])
                    ans++;
            return ans;
        }

        public static Object PartB(string file)
        {
            var v = ReadInput.Ints(day, file);
            int ans = 0;
            for (int i = 1; i < v.Count - 2; i++)
                if (v[i] + v[i + 1] + v[i + 2] > v[i - 1] + v[i] + v[i + 1])
                    ans++;
            return ans;
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
