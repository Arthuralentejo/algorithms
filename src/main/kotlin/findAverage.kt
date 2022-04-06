fun findAverage(input : List<Int>) : Float {
    val sumTotal = input.reduce { count, number -> count + number }
    val size = input.size
    return (sumTotal / size).toFloat()
}