fun phraseInverter(input: String): String {
    val words: List<String> = input.split(" ")
    val invertedWords = words.indices.map{
        words[words.size - 1 - it]
    }
    return invertedWords.joinToString(separator = " ")
}