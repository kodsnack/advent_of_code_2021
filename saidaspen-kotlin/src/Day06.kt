import java.io.File

fun main() {
    println(Day06.part1())
    println(Day06.part2())
}

object Day06 {
    private var input = File("/home/mendlock/.aoc/202106").readText().trim()
    private val fish = ints(input).toMutableList()
    fun part1() = simulateFish(fish, 80)
    fun part2() = simulateFish(fish, 256)

    private fun simulateFish(fish: MutableList<Int>, days: Int): Long {
        val list = MutableList<Long>(9) { 0 }
        fish.forEach { list[it]++ }
        repeat(days) {
            list.rotate(-1)
            list[6] += list[8]
        }
        return list.sum()
    }
}




