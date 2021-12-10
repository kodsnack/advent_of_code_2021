import java.io.File

fun main() {
    println(Day04.part1())
    println(Day04.part2())
}

object Day04 {
    private var input = File("/home/mendlock/.aoc/202104").readText().trim()

    private val numbers = ints(input.lines().take(1)[0])
    private val boards = toBoards()

    fun part1(): Any {
        val marked = mutableMapOf<Int, MutableList<P<Int, Int>>>()
        for (num in numbers) {
            //mark
            for ((i, b) in boards.withIndex()) {
                val e = b.entries.firstOrNull { it.value == num }
                if (e != null) {
                    val markedList = marked.getOrDefault(i, mutableListOf())
                    markedList.add(e.key)
                    marked[i] = markedList
                }
            }

            // score
            for ((i, b) in boards.withIndex()) {
                var hasWon = false
                if (marked[i] != null && marked[i]!!.size >= 5) {
                    for (row in 0 until 5) {
                        hasWon = hasWon || marked[i]!!.count { it.first == row } == 5
                    }
                    for (col in 0 until 5) {
                        hasWon = hasWon || marked[i]!!.count { it.second == col } == 5
                    }
                }
                if (hasWon) {
                    return b.filter { !marked[i]!!.contains(it.key) }.map { it.value }.sum() * num
                }
            }
        }
        return "NO WINNER"
    }

    fun part2(): Any {
        val marked = mutableMapOf<Int, MutableList<P<Int, Int>>>()
        val winners = mutableListOf<P<Int, Int>>()
        for (num in numbers) {
            //mark
            for ((i, b) in boards.withIndex()) {
                val e = b.entries.firstOrNull { it.value == num }
                if (e != null) {
                    val markedList = marked.getOrDefault(i, mutableListOf())
                    markedList.add(e.key)
                    marked[i] = markedList
                }
            }

            for ((i, b) in boards.withIndex()) {
                var hasWon = false
                if (marked[i] != null && marked[i]!!.size >= 5 && !winners.map { it.first }.contains(i)) {
                    for (row in 0 until 5) {
                        hasWon = hasWon || marked[i]!!.count { it.first == row } == 5
                    }
                    for (col in 0 until 5) {
                        hasWon = hasWon || marked[i]!!.count { it.second == col } == 5
                    }
                }
                if (hasWon) {
                    winners.add(P(i, b.filter { !marked[i]!!.contains(it.key) }.map { it.value }.sum() * num))
                }
            }
        }

        return winners.last().second
    }

    private fun toBoards(): MutableList<MutableMap<P<Int, Int>, Int>> {
        val boards = mutableListOf<String>()
        var board = ""
        val lines = input.lines().drop(2)
        for (i in lines.indices) {
            if (lines[i].isEmpty()) {
                boards.add(board)
                board = ""
            } else {
                board += lines[i] + "\n"
            }
        }
        val tmp = mutableListOf<MutableMap<P<Int, Int>, Int>>()
        boards.forEach{ b ->
            val numbers = ints(b)
            val bMap = mutableMapOf<P<Int, Int>, Int>()
            for (row in 0 until 5) {
                for (col in 0 until 5) {
                    bMap[P(row, col)] = numbers[row*5+col]
                }
            }
            assert(bMap.size == 25)
            tmp.add(bMap)
        }
        return tmp
    }

}
