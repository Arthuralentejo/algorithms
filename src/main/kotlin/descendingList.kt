fun descendingList (input: MutableList<Int>): List<Int> {
    val descending: MutableList<Int> = mutableListOf()
    for (i in input.indices ){
        descending.add(input.removeAt(input.indexOf(input.maxOrNull())))
    }
    return descending
}