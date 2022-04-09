fun inverter(input : List<Any>) : List<Any> {
    return input.indices.map { i -> input[input.size - 1 - i] }
}