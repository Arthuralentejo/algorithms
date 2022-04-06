fun findGreater(input: List<Int>): Int{
    var bigger: Int = -1
    input.forEach { num ->
        if (num > bigger)  bigger = num
    }
    return bigger
}