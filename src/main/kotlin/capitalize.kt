fun capitalize (input: String): String {
    var capitalized = ""
    val wordsList = input.split(" ")
    wordsList.forEach { word ->
        word.forEach {char ->
            capitalized += if (word.indexOf(char) == 0){
                char.uppercaseChar()
            }else {
                char.lowercaseChar()
            }
        }
        capitalized += " "
    }

    return capitalized

}