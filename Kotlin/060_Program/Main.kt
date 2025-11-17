fun process(x: Int, operation: (Int) -> Int): Int {
    return operation(x)
}

fun main() {
    println("=== Functional Programming 060 ===")

    // Lambda expressions
    val add = { x: Int, y: Int -> x + y }
    val multiply = { x: Int, y: Int -> x * y }

    println("Add: ${add(5, 3)}")
    println("Multiply: ${multiply(5, 3)}")

    // Higher-order functions
    val result1 = process(10) { it * 2 }
    val result2 = process(10) { it * it }

    println("Process 1: $result1")
    println("Process 2: $result2")

    // Function composition
    val list = listOf(1, 2, 3, 4, 5)
    val result = list
        .filter { it % 2 == 0 }
        .map { it * it }
        .sum()
    println("Result: $result")
}
