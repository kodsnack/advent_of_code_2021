import java.io.File
import kotlin.math.abs

fun main() {
    println(Day08.part1())
    println(Day08.part2())
}

object Day08 {
    private var input = File("/home/mendlock/.aoc/202108").readText().trim()

    private var normalDigits = mapOf(
        "abcefg" to 0,
        "cf" to 1,
        "acdeg" to 2,
        "acdfg" to 3,
        "bcdf" to 4,
        "abdfg" to 5,
        "abdefg" to 6,
        "acf" to 7,
        "abcdefg" to 8,
        "abcdfg" to 9,
    )

    private var permutations = "abcdefg".toList().permutations().map { it.joinToString("") }
    private val outputs = input.lines()
        .map { P(it.split("|")[0], it.split("|")[1]) } // Split into input, output digits
        .map { translate(solve(it.first), it.second) }

    fun part1() = outputs.sumOf { it.toCharArray().filter { c -> c == '1' || c == '4' || c == '7' || c == '8' }.size }
    fun part2() =  outputs.sumOf { it.toInt() }

    private fun translate(t: String, inp: String): String {
        return inp.split(" ")
            .filter { it.trim() != "" }
            .map { it.tr(t, "abcdefg").sortChars() }
            .joinToString("") { normalDigits[it].toString() }
    }

    private fun solve(inp: String): String {
        val digitsInp = inp.split(" ").map { it.toCharArray().sorted().joinToString("") }.filter { it.trim() != "" }
        return  permutations.first { cand ->
            digitsInp.mapNotNull { normalDigits[it.tr(cand, "abcdefg").toList().sorted().joinToString("")] }.size == 10
        }
    }
}




