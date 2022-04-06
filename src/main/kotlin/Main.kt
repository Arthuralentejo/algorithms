fun main() {

    val lista = mutableListOf<Int>(23, 59, 94, 23, 54, 34)
    val num = 5
    val exponent = 3
    val phrase = "the books is on the table and the table is on the floor"


    println("The greater number inside $lista is ${findGreater(lista)}\n")

    println("The arithmetic average of $lista is ${findAverage(lista)}\n")

    println("The inverted version of $lista is ${inverter(lista)}\n")

    println("The $lista organized in the descending order is ${descendingList(lista)}\n")

    println("The factorial of $num is ${recursiveFactorial(num)}\n")

    println("The number $num reaised to the power of $exponent is ${recursiveExponentiation(num, exponent)}\n")

    println("The capitalized version following phrase \n \"$phrase\" \nis \n \"${capitalize(phrase)}\" \n")

    println("\nThe following phrase \n \"$phrase\"\nwith the sequence of words inverted is\n \"${phraseInverter(phrase)}\" ")

    println("\nThere are \"${nonRepeatedWords(phrase)}\" non repeated words in the phrase \n\"$phrase\"\n ")





}