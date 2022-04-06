fun nonRepeatedWords(input: String): Int{
    val words = mutableMapOf<String,Int>()
    input.split(" ").forEach{
        if(words.containsKey(it)){
            words.remove(it)
        } else {
            words[it] = 1
        }
    }

    return words.size
}