import java.util.*

fun ints(input: String) = "-?\\d+".toRegex(RegexOption.MULTILINE).findAll(input).map { it.value.toInt() }.toList()
typealias P<A, B> = Pair<A, B>
fun <E> MutableList<E>.rotate(i: Int) {
    Collections.rotate(this, i)
}