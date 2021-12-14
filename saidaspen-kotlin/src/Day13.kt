import java.io.File

fun main() {
    println(Day13.part1())
    Day13.part2()
}

object Day13 {
    private var input = File("/home/mendlock/.aoc/202113").readText().trim()

    fun part1(): Any {
        var dots = input.split("\n\n")[0].lines().map { P(ints(it)[0], ints(it)[1]) }.toSet()
        val folds = input.split("\n\n")[1].lines()
        val fold = folds[0].replace("fold along ", "")
        val dir = fold[0]
        val amt = ints(fold)[0]
        dots = if (dir == 'x') foldX(dots, amt) else foldY(dots, amt)
        return dots.size
    }

    fun part2() {
        var dots = input.split("\n\n")[0].lines().map { P(ints(it)[0], ints(it)[1]) }.toSet()
        val folds = input.split("\n\n")[1].lines()
        for (f in folds) {
            val fold = f.replace("fold along ", "")
            val dir = fold[0]
            val amt = ints(fold)[0]
            dots = if (dir == 'x') foldX(dots, amt) else foldY(dots, amt)
        }
        printMap(dots.associateWith { '#' })
    }

    private fun foldX(dots: Set<P<Int, Int>>, amt: Int) = dots.map {
        if (it.first <= amt) {
            it
        } else {
            P(amt - (it.first - amt), it.second)
        }
    }.distinct().toSet()


    private fun foldY(dots: Set<P<Int, Int>>, amt: Int) = dots.map {
        if (it.second <= amt) {
            it
        } else {
            val newY = amt - (it.second - amt)
            P(it.first, newY)
        }
    }.distinct().toSet()
}




