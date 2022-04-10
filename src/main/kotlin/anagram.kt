fun isAnagram(str: String, str_compare: String): Boolean {
    if (str.length != str_compare.length) return false

    //Creating map of letters
    val anagram: MutableMap<Char, Int> = mutableMapOf<Char, Int>()
    str.replace(" ", "").lowercase().toCharArray().forEach { char ->
        if (anagram.containsKey(char)) {
            anagram[char] = anagram.getValue(char) + 1
        } else {
            anagram[char] = 1
        }
    }

    //Removing equal letters from map
    str_compare.replace(" ", "").lowercase().toCharArray().forEach { char ->
        if (anagram.containsKey(char)) {
            anagram[char] = anagram.getValue(char) - 1
            if (anagram[char] == 0) {
                anagram.remove(char)
            }
        }
    }

    return anagram.isEmpty()
}