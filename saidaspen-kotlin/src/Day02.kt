import java.io.File

fun main() {
    println(Day02.part1())
    println(Day02.part2())
}

object Day02 {
    private var input = File("/home/mendlock/.aoc/202102").readText()

    fun part1(): Any {
        var z = 0L
        var d = 0L
        input.lines().map { it.split(" ") }.map {
            when (it[0]) {
                "forward" -> z += it[1].toLong()
                "down" -> d += it[1].toLong()
                "up" -> d -= it[1].toLong()
            }
        }
        return z * d
    }

    fun part2(): Any {
        var z = 0L
        var d = 0L
        var aim = 0L
        input.lines().map { it.split(" ") }.map {
            when (it[0]) {
                "forward" -> {
                    z += it[1].toLong()
                    d += aim * it[1].toLong()
                }
                "down" -> aim += it[1].toLong()
                "up" -> aim -= it[1].toLong()
            }
        }
        return z * d
    }
}

