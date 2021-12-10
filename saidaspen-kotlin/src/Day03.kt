import java.io.File

fun main() {
    println(Day03.part1())
    println(Day03.part2())
}

object Day03 {
    private var input = File("/home/mendlock/.aoc/202103").readText().trim()

    fun part1(): Any {
        val lines = input.lines().size
        val gamma = StringBuilder()
        for (i in 0 until input.lines()[0].length) {
            val ones = input.lines().map { it.toCharArray()[i] }.count { it == '1' }
            gamma.append(if (ones > lines/2) '1' else '0')
        }
        return gamma.toString().toInt(2) * gamma.toString().toCharArray().map { if(it == '1') '0' else '1' }.joinToString("").toInt(2)
    }

    fun part2(): Any {
        var ogrLeft = input.lines()
        var co2scrubLeft = input.lines()
        for (i in 0 until input.lines()[0].length) {
            val ogrOnes = ogrLeft.map { it.toCharArray()[i] }.count { it == '1' }
            val ogrCrit = if (ogrOnes >= ogrLeft.size / 2) '1' else '0'
            if (ogrLeft.size > 1)
                ogrLeft = ogrLeft.filter { it.toCharArray()[i] == ogrCrit }
            val co2Ones = co2scrubLeft.map { it.toCharArray()[i] }.count { it == '1' }
            val co2Crit = if (co2Ones < co2scrubLeft.size / 2) '1' else '0'
            if (co2scrubLeft.size > 1)
                co2scrubLeft = co2scrubLeft.filter { it.toCharArray()[i] == co2Crit }
        }
        return ogrLeft[0].toInt(2) * co2scrubLeft[0].toInt(2)
    }
}