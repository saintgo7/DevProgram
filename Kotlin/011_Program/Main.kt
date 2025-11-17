fun main() {
    println("=== Kotlin Program 011 ===")
    println("Demonstrating basic Kotlin features")

    // Variables
    val immutable = "Cannot be changed"
    var mutable = "Can be changed"

    // String interpolation
    println("Immutable: $immutable")
    println("Mutable: $mutable")

    // When expression
    val result = when (val x = 11) {
        in 1..10 -> "Single digit"
        in 11..99 -> "Double digit"
        else -> "Three or more digits"
    }
    println("Result: $result")
}
