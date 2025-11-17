data class Person(
    val name: String,
    val age: Int,
    val email: String
)

fun main() {
    val person1 = Person("Alice", 30, "alice@example.com")
    val person2 = Person("Bob", 25, "bob@example.com")

    println("Person 1: $person1")
    println("Person 2: $person2")

    // Copy with modification
    val person3 = person1.copy(age = 31)
    println("Person 3: $person3")

    // Destructuring
    val (name, age, email) = person1
    println("Name: $name, Age: $age, Email: $email")
}
