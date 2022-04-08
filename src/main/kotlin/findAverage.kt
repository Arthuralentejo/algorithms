fun findAverage(input : List<Int>) : Double {
    val sumTotal = input.reduce { count, number -> count + number }
    val size = input.size
    return sumTotal/size.toDouble()
}