fun main() {
    println(isPalidrome("Adias a data da saida"))
}



fun isPalidrome(input: String): Boolean{
    if (input.isEmpty()) return false
    var equal = true
    var count = 0
    val word = input.lowercase().replace(" ","")
    val inverted = word.reversed()        //without reversed -> word.indices.map { i -> word[word.length - 1 - i]}
    while (equal && count < word.length ) {
        if (inverted[count] != word[count]){
            equal = false
        }
        count ++
    }
    return equal
}