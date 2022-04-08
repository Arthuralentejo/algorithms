// Atm simulator


fun main() {
    println("Withrawing: 59 in ${withdrawal(59).toString()} bank notes")
    println("Withrawing: 75 in ${withdrawal(75).toString()} bank notes")
    println("Withrawing: 157 in ${withdrawal(157).toString()} bank notes")
    println("Withrawing: 1998 in ${withdrawal(1998).toString()} bank notes")
}


fun withdrawal(input: Int): Map<Int, Int> {
    var value = input
    val notes = listOf(100, 50, 20, 10, 5, 2)
    val withDrawed = mutableMapOf<Int, Int>()
    var count = 0
    while (value >= notes.last()) {
        val note = notes[count]
        if (value >= note) {
            value -= note
            if (withDrawed.containsKey(note)) {
                withDrawed[note] = withDrawed.getValue(note) + 1
            } else {
                withDrawed[note] = 1
            }
        } else {
            count++
        }

    }

    return withDrawed
}