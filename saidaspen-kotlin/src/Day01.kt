import java.io.File

fun main() {
    println(Day01.part1())
    println(Day01.part2())
}

object Day01 {
    private var input = File("/home/mendlock/.aoc/202101").readText()
    fun part1() = ints(input).windowed(2).count { it[1] > it[0] }
    fun part2() = ints(input).windowed(4).count { it[3] > it[0] }
}