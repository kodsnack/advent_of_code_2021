import java.io.File
import kotlin.math.abs

fun main() {
    println(Day09.part1())
    println(Day09.part2())
}

object Day09 {
    private var input = File("/home/mendlock/.aoc/202109").readText().trim()

    fun part1() : Any {
        val map = toMap(input)
        val lowpoints = map.keys.filter { p ->  (neighborsSimple(p).mapNotNull { map[it] }.all { it.toString().toInt() > map[p].toString().toInt() })}
        return lowpoints.sumOf {map[it].toString().toInt() + 1  }
    }

    fun part2() : Any {
        val map = toMap(input)
        val flowsMap = map.keys.map { P(it, flowsTo2(it, map)) }.filter { it.second != null }.toMap()
        val toLowPoints = flowsMap.keys.map { findLp(it, flowsMap) }
        val basins = toLowPoints.groupBy { it.second }
        val topThree = basins.entries.map { it.value.size }.sortedByDescending { it }.take(3)
        return topThree[0] * topThree[1] * topThree[2]
    }

    private fun findLp(it: P<Int, Int>, flowsMap: Map<P<Int, Int>, Pair<Int, Int>?>): P<P<Int, Int>, P<Int, Int>> {
        var p = it
        while (flowsMap.containsKey(p)) {
            val n = flowsMap[p]!!
            if (p == n) {
                return P(it, p)
            }
            p = n
        }
        return P(it, p)
    }

    private fun flowsTo2(p: Pair<Int, Int>, map: MutableMap<Pair<Int, Int>, Char>): Pair<Int, Int>? {
        if (map[p].toString().toInt() == 9) {
            return null
        }
        val lowestN =  neighborsSimple(p)
            .filter { map[it] != null }
            .filter { it.first >= 0 && it.second >= 0 }
            .filter {  map[it].toString().toInt() != 9 }
            .minByOrNull { map[it].toString().toInt() }
        return if (map[lowestN].toString().toInt() < map[p].toString().toInt()) lowestN else p
    }

}




