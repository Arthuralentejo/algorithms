// Atm simulator


fun main() {
    val value = 59
    val bankNotes: Map<Int, Int> = withdrawal(value)
    println(bankNotes.toString())
}


fun withdrawal(input: Int): Map<Int, Int> {
    var value = input
    val notes = mutableListOf(100, 50, 20, 10, 5, 2)
    val withDrawed = mutableMapOf<Int, Int>()
    while (value > 0) {
        val currentNote = notes.first()
        if (currentNote <= value) {

            if (withDrawed.containsKey(currentNote)) {
                withDrawed[currentNote] = withDrawed.getValue(currentNote) + 1
            } else {
                withDrawed[currentNote] = 1
            }
            value -= currentNote
        } else {

            notes.removeFirst()
        }

    }

    return withDrawed
}