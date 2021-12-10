import java.io.File
import kotlin.math.abs

fun main() {
    println(Day07.part1())
    println(Day07.part2())
}

object Day07 {
    private var input = File("/home/mendlock/.aoc/202107").readText().trim()

    fun part1(): Any {
        val startPositions = ints(input)
        return (startPositions.minOrNull()!!..startPositions.maxOrNull()!!).minOf { sp ->
            startPositions.sumOf { abs(it - sp) }
        }
    }

    fun part2(): Any {
        val startPos = ints(input)
        return (startPos.minOrNull()!!..startPos.maxOrNull()!!).minOf { p ->
            startPos.sumOf { (abs(it - p) + 1) * abs(it - p) / 2 }
        }
    }
}




