using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using AdventOfCode;
//using Position = AdventOfCode.GenericPosition2D<int>;

namespace day08
{
    public class Day08
    {
        static readonly string day = "day08";

        // Day 08: 

        static Object PartA()
        {
            var z = ReadInput.Ints(day);
            //Console.WriteLine("A is {0}", a);
            return 0;
        }

        static Object PartB()
        {
            return 0;
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
        static readonly int qa = 42;
        static readonly int qb = 4711;
        public static bool Test() => (PartA().Equals(qa)) && (PartB().Equals(qb));
    }
}
