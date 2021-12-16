using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using AdventOfCode;

namespace aoc
{
    public class Day16
    {
        // Today: Decode packets, convert between bases 2 and 16

        static string ReadData(string file)
        {
            string ret = "";
            foreach (var s in File.ReadAllLines(ReadInput.GetPath(Day, file)))
                foreach (var c in s)
                    ret += Convert.ToString(Convert.ToInt32(c.ToString(), 16), 2).PadLeft(4, '0');
            return ret;
        }

        static long verSum;

        static long GetNum(string z, ref int offs, int n)
        {
            string s = z.Substring(offs, n);
            offs += n;
            return Convert.ToUInt32(s, 2);
        }
        static long GetLiterals(string z, ref int offs)
        {
            bool lastNum = false;
            long res = 0;
            while (!lastNum)
            {
                lastNum = z[offs++] == '0';
                long a = GetNum(z, ref offs, 4);
                res = res * 16 + a;
            }
            return res;
        }
        static long PrintOp(string op, List<long> nums, int d, long res)
        {
            string s = "(" + nums.Select(x => x.ToString()).Aggregate((a, x) => a + " " + op + " " + x) + ")";
            Console.WriteLine("L{0} {1}", d.ToString("00"), new string(' ', d) + s + " = " + res.ToString());
            return res;
        }

        static long GetPacket(string z, ref int offs, int depth, bool log)
        {
            long ver = GetNum(z, ref offs, 3);
            verSum += ver;
            long type = GetNum(z, ref offs, 3);
            if (type == 4)
                return GetLiterals(z, ref offs);
            else
            {
                var nums = new List<long>();
                long lid = GetNum(z, ref offs, 1);
                long n = GetNum(z, ref offs, lid == 0 ? 15 : 11);
                int startOffs = offs;
                int np = 0;
                if (lid == 0)
                    while (offs - startOffs < n)
                        nums.Add(GetPacket(z, ref offs, depth + 1, log));
                else
                    while (np++ < n)
                        nums.Add(GetPacket(z, ref offs, depth + 1, log));
                long res = 0;
                res = type switch
                {
                    0 => nums.Aggregate((a, x) => a + x),
                    1 => nums.Aggregate((a, x) => a * x),
                    2 => nums.Min(),
                    3 => nums.Max(),
                    5 => nums[0] > nums[1] ? 1 : 0,
                    6 => nums[0] < nums[1] ? 1 : 0,
                    7 => nums[0] == nums[1] ? 1 : 0,
                    _ => throw new ArgumentOutOfRangeException(),
                };
                string[] ops = { "+", "*", "min", "max", "_", ">", "<", "==" };
                return log ? PrintOp(ops[type], nums, depth, res) : res;
            }
        }

        public static (Object, long) Part(string file, bool log)
        {
            int offs = 0;
            verSum = 0;
            return (GetPacket(ReadData(file), ref offs, 0, log), verSum); 
        }
        public static Object PartA(string file) => Part(file, false).Item2;
        public static Object PartB(string file) => Part(file, false).Item1;

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod());
    }
}
