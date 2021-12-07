using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using AdventOfCode;
//using Position = AdventOfCode.GenericPosition2D<int>;

namespace dayXX
{
    public class DayXX
    {
        static readonly string day = "dayXX";

        // Day 08: 

        public static Object PartA(string file)
        {
            var z = ReadInput.Ints(day, file);
            //Console.WriteLine("A is {0}", a);
            return 0;
        }

        public static Object PartB(string file)
        {
            return 0;
        }

        static void Main() => Aoc.Execute(day, PartA, PartB);
    }
}
