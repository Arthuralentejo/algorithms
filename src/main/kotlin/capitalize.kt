fun capitalize (input: String): String {
    val sb = StringBuilder()
    input.split(" ").forEach { word ->
        sb.append(word.first().uppercaseChar()).append(word.substring(1)).append(" ")
    }
    return sb.toString()
}