import java.io.File

fun main() {
    println(Day14.part1())
    println(Day14.part2())
}

object Day14 {
    private var input = File("/home/mendlock/.aoc/202114").readText().trim()

    private val template = input.lines()[0]
    private val inserts = input.lines().drop(2).map { it.split("->") }.associate { it[0].trim() to it[1].trim() }

    fun part1(): Any {
        var curr = template
        repeat(10) {
            curr = curr[0] + curr.windowed(2).map {
                if (inserts.containsKey(it)) {
                    inserts[it]!! + it[1]
                } else {
                    it
                }
            }.joinToString("")
        }
        return curr.groupingBy { it }.eachCount().maxOf { it.value } - curr.groupingBy { it }.eachCount().minOf { it.value }
    }

    fun part2(): Any {
        var count = mutableMapOf<String, Long>()
        template.windowed(2).forEach { count[it] = count.getOrDefault(it, 0) + 1 }
        repeat(40) {
            val oldCount = count.entries.associate { it.key to it.value }
            count = mutableMapOf()
            oldCount.entries.forEach{
                val found = inserts[it.key]!!
                count[it.key[0] + found] = count.getOrDefault(it.key[0] + found, 0) + it.value
                count[found + it.key[1]] = count.getOrDefault(found + it.key[1], 0) + it.value
            }
        }
        val charCnt = mutableMapOf<Char, Long>()
        count.entries.forEach { charCnt[it.key[0]] = charCnt.getOrDefault(it.key[0], 0) + it.value }
        charCnt[template.last()] = charCnt[template.last()]!! + 1
        return charCnt.values.maxOrNull()!! - charCnt.values.minOrNull()!!
    }
}




