using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using AdventOfCode;
//using Position = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day14
    {
        // Today: 

        public static Object PartA(string file)
        {
            var z = ReadInput.Ints(Day, file);
            //Console.WriteLine("A is {0}", a);
            return 0;
        }

        public static Object PartB(string file)
        {
            return 0;
        }

        static void Main() => Aoc.Execute(Day, PartA, PartB);
        static string Day { get { return Aoc.Day(MethodBase.GetCurrentMethod()); } }
    }
}
