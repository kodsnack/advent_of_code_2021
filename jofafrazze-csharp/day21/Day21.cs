using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using AdventOfCode;
using Pos = AdventOfCode.GenericPosition2D<int>;

namespace aoc
{
    public class Day21
    {
        // Today: 

        public static (Object a, Object b) DoPuzzle(string file)
        {
            var z = ReadInput.Ints(Day, file);
            //Console.WriteLine("A is {0}", a);
            return (0, 0);
        }

        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
