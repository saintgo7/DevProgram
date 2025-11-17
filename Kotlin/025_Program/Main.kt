class Example025(private val name: String) {
    fun greet() {
        println("Hello from $name!")
    }

    fun display() {
        println("This is example 025")
    }
}

fun main() {
    val obj = Example025("Kotlin OOP")
    obj.greet()
    obj.display()

    // Lambda expression
    val numbers = listOf(1, 2, 3, 4, 5)
    val doubled = numbers.map { it * 2 }
    println("Doubled: $doubled")

    // Higher-order function
    val result = numbers.filter { it % 2 == 0 }.map { it * it }
    println("Even squared: $result")
}
