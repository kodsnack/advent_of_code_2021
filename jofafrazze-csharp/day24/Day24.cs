using AdventOfCode;
using System.Reflection;

namespace aoc
{
    public class Day24
    {
        // Arithmetic Logic Unit: Interpret ALU assembler to find model numbers

        // Interpreting the ALU code (see notes.txt) gives requirements:
        //
        // Require: D4 == D5
        // Require: D6 + 1 == D7
        // Require: D8 + 2 == D9
        // Require: D3 + 7 == D10
        // Require: D11 - 1 == D12
        // Require: D2 + 4 == D13
        // Require: D1 - 2 == D14
        // 
        // which leads to
        // 
        // #  12345678901234
        // A: 95299897999897 // Largest possible model number
        // 
        // #  12345678901234
        // B: 31111121382151 // Smallest possible model number

        public static (Object a, Object b) DoPuzzle(string file) => (95299897999897, 31111121382151);
        static void Main() => Aoc.Execute(Day, DoPuzzle);
        static string Day => Aoc.Day(MethodBase.GetCurrentMethod()!);
    }
}
