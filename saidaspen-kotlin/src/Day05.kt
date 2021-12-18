import java.io.File
import kotlin.math.sign

fun main() {
    println(Day05.part1())
    println(Day05.part2())
}

object Day05 {
    private var input = File("/home/mendlock/.aoc/202105").readText().trim()
    private val lines = input.lines().map { ints(it) }.map { P(P(it[0], it[1]), P(it[2], it[3])) }

    fun part1() =
        countCrosses(lines.filter { it.first.first == it.second.first || it.first.second == it.second.second })

    fun part2() = countCrosses(lines)

    private fun countCrosses(lines: List<P<P<Int, Int>, P<Int, Int>>>) =
        lines.flatMap { toPoints(it) }.groupingBy { it }.eachCount().count { it.value >= 2 }

    private fun toPoints(l: Pair<Pair<Int, Int>, Pair<Int, Int>>): List<P<Int, Int>> {
        val list = mutableListOf<P<Int, Int>>()
        var curr = l.first
        val dx = (l.second.first - l.first.first).sign
        val dy = (l.second.second - l.first.second).sign
        while (curr != l.second) {
            list.add(curr)
            curr = P(curr.first + dx, curr.second + dy)
        }
        list.add(l.second)
        return list
    }
}
