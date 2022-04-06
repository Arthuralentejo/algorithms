fun recursiveFactorial (input : Int) : Int {
    return if (input >= 1)
        input * recursiveFactorial(input - 1)
    else
        1
}