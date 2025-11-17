fun main() {
    val numbers = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    println("Original list: $numbers")

    // Filter
    val evenNumbers = numbers.filter { it % 2 == 0 }
    println("Even numbers: $evenNumbers")

    // Map
    val squared = numbers.map { it * it }
    println("Squared: $squared")

    // Reduce
    val sum = numbers.reduce { acc, n -> acc + n }
    println("Sum: $sum")

    // Any, All, None
    println("Has even: ${numbers.any { it % 2 == 0 }}")
    println("All positive: ${numbers.all { it > 0 }}")
    println("None negative: ${numbers.none { it < 0 }}")
}
