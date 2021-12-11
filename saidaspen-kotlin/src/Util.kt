import java.util.*

fun ints(input: String) = "-?\\d+".toRegex(RegexOption.MULTILINE).findAll(input).map { it.value.toInt() }.toList()
typealias P<A, B> = Pair<A, B>
fun <E> MutableList<E>.rotate(i: Int) {
    Collections.rotate(this, i)
}

fun String.tr(transSource: String, transTarget: String): String {
    assert(transSource.length == transTarget.length)
    val translation = transSource.toCharArray().mapIndexed { i, v -> P(v, transTarget[i]) }.toMap()
    return tr(translation)
}
fun String.tr(translations: Map<Char, Char>) =  this.toCharArray().map { translations.getOrDefault(it, it) }.joinToString("")

fun String.sortChars() = this.toList().sorted().joinToString("")

fun <V> List<V>.permutations(): Sequence<List<V>> {
    val underlying = this
    val factorials = IntArray(underlying.size + 1)
    factorials[0] = 1
    for (i in 1..underlying.size) {
        factorials[i] = factorials[i - 1] * i
    }
    return sequence {
        for (i in 0 until factorials[underlying.size]) {
            val temp = mutableListOf<V>()
            temp.addAll(underlying)
            val onePermutation = mutableListOf<V>()
            var positionCode = i
            for (position in underlying.size downTo 1) {
                val selected = positionCode / factorials[position - 1]
                onePermutation.add(temp[selected])
                positionCode %= factorials[position - 1]
                temp.removeAt(selected)
            }
            yield(onePermutation)
        }
    }
}

fun toMap(input: String): MutableMap<P<Int, Int>, Char> {
    val lines = input.lines()
    val map = mutableMapOf<P<Int, Int>, Char>()
    for (line in lines.indices) {
        val lineChars = lines[line].toCharArray()
        for (col in lineChars.indices) {
            map[P(col, line)] = lineChars[col]
        }
    }
    return map
}
fun neighbors(i: P<Int, Int>) = listOf(
    i + P(-1, -1), i + P(-1, 0), i + P(-1, 1),
    i + P(0, -1), i + P(0, 1),
    i + P(1, -1), i + P(1, 0), i + P(1, 1))


fun neighborsSimple(i: P<Int, Int>) = listOf(
    i + P(-1, 0),
    i + P(0, -1),
    i + P(0, 1),
    i + P(1, 0))

operator fun Pair<Int, Int>.plus(that: Pair<Int, Int>) = Pair(this.first + that.first, this.second + that.second)
