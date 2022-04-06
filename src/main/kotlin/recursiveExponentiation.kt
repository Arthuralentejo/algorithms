fun recursiveExponentiation (input: Int, exponent: Int) : Int {
    return if (exponent != 0 ){
        input * recursiveExponentiation(input, exponent-1)
    } else {
        1
    }
}