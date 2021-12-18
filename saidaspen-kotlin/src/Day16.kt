import java.io.File
import java.lang.RuntimeException
import java.util.*

fun main() {
    println(Day16.part1())
    println(Day16.part2())
}

object Day16 {
    private var input = File("/home/mendlock/.aoc/202116").readText().trim()

    fun part1(): Any {
        val decoder = PacketDecoder()
        decoder.decode(input)
        return decoder.versionSum
    }

    fun part2(): Any {
        val decoder = PacketDecoder()
        return decoder.decode(input)
    }
}

class PacketDecoder {
    private var stack = mutableListOf<Long>()
    var versionSum = 0

    fun decode(hex: String): Long {
        var binIn = hex.toCharArray().toList().joinToString("") { Integer.parseInt(it.toString(), 16).toBinary(4) }
        fun take(n: Int): String {
            val tmp = binIn.take(n)
            binIn = binIn.drop(n)
            return tmp
        }

        fun readPackage(): Int {
            val leftBefore = binIn.length
            val version = take(3).toInt(2)
            versionSum += version
            val typeId = take(3).toInt(2)
            if (typeId == 4) {  // Literal value
                var tmp = ""
                var continueFlag: String
                do {
                    continueFlag = take(1)
                    tmp += take(4)
                } while (continueFlag == "1")
                stack.add(tmp.toLong(2))
            } else {
                val lenTypeId = take(1)
                var subPackages = 0
                if (lenTypeId == "0") {
                    val packageLength = take(15).toInt(2)
                    var tRead = 0
                    while (tRead < packageLength) {
                        tRead += readPackage()
                        subPackages++
                    }
                } else {
                    val numberOfSubPackages = take(11).toInt(2)
                    repeat(numberOfSubPackages) {
                        readPackage()
                        subPackages++
                    }
                }

                val operands = stack.takeLast(subPackages)
                stack = stack.dropLast(subPackages).toMutableList()
                val value: Long = when (typeId) {
                    0 -> operands.sumOf { it }
                    1 -> operands.fold(1L){ acc, i -> acc * i}
                    2 -> operands.minOf { it }
                    3 -> operands.maxOf { it }
                    5 -> if (operands[0] > operands[1]) 1 else 0
                    6 -> if (operands[0] < operands[1]) 1 else 0
                    7 -> if (operands[0] == operands[1]) 1 else 0
                    else -> throw RuntimeException("Unsupported type $typeId")
                }
                stack.add(value)
            }
            return leftBefore - binIn.length
        }
        while (binIn.any { it == '1' }) {
            readPackage()
        }
        return stack[0]
    }
}




