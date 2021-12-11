import java.io.File

fun main() {
    println(Day11.part1())
    println(Day11.part2())
}

object Day11 {
    private var input = File("/home/mendlock/.aoc/202111").readText().trim()

    fun part1(): Any {
        val lines = input.lines()
        val octs = mutableMapOf<P<Int, Int>, Int>()
        for (line in lines.indices) {
            val lineChars = lines[line].toCharArray()
            for (col in lineChars.indices) {
                octs[P(col, line)] = lineChars[col].toString().toInt()
            }
        }
        var flashes = 0
        var step = 1
        while (step <= 100) {
            octs.keys.forEach { octs.merge(it, 1, Int::plus) }
            // flashes
            val hasFlashed = mutableListOf<Pair<Int, Int>>()
            var toFlash: List<Pair<Int, Int>>
            flashes@ do {
                toFlash = octs.entries
                    .filter { it.value > 9 }
                    .map { it.key }
                    .filter { octs.containsKey(it) }
                    .filter { !hasFlashed.contains(it) }
                    .distinct()
                hasFlashed.addAll(toFlash)
                flashes += toFlash.size
                toFlash.flatMap { neighbors(it) }.filter { octs.containsKey(it) }
                    .forEach { octs.merge(it, 1, Int::plus) }
            } while (toFlash.isNotEmpty())
            // reset
            hasFlashed.forEach { octs[it] = 0 }
            step++
        }
        return flashes
    }

    fun part2(): Any {
        val lines = input.lines()
        val octs = mutableMapOf<P<Int, Int>, Int>()
        for (line in lines.indices) {
            val lineChars = lines[line].toCharArray()
            for (col in lineChars.indices) {
                octs[P(col, line)] = lineChars[col].toString().toInt()
            }
        }
        var flashes = 0
        var step = 1
        while (true) {
            octs.keys.forEach { octs.merge(it, 1, Int::plus) }
            // flashes
            val hasFlashed = mutableListOf<Pair<Int, Int>>()
            var toFlash: List<Pair<Int, Int>>
            flashes@ do {
                toFlash = octs.entries
                    .filter { it.value > 9 }
                    .map { it.key }
                    .filter { octs.containsKey(it) }
                    .filter { !hasFlashed.contains(it) }
                    .distinct()
                hasFlashed.addAll(toFlash)
                flashes += toFlash.size
                toFlash.flatMap { neighbors(it) }.filter { octs.containsKey(it) }
                    .forEach { octs.merge(it, 1, Int::plus) }
            } while (toFlash.isNotEmpty())
            // reset
            hasFlashed.forEach { octs[it] = 0 }
            if (hasFlashed.size == octs.size) {
                return step
            }
            step++
        }
    }
}




