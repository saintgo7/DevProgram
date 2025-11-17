#!/usr/bin/env python3
"""
Create 100 Kotlin programs
"""

import os

base_dir = "/home/user/DevProgram/Kotlin"

# Kotlin program templates
kotlin_programs = {
    1: ("Hello World", "Basic Kotlin hello world", """fun main() {
    println("Hello, Kotlin!")
    println("Welcome to Kotlin Programming")
}
"""),

    2: ("Calculator", "Simple calculator", """fun main() {
    println("=== Kotlin Calculator ===")
    print("Enter first number: ")
    val num1 = readLine()?.toDoubleOrNull() ?: 0.0

    print("Enter operator (+, -, *, /): ")
    val operator = readLine() ?: "+"

    print("Enter second number: ")
    val num2 = readLine()?.toDoubleOrNull() ?: 0.0

    val result = when (operator) {
        "+" -> num1 + num2
        "-" -> num1 - num2
        "*" -> num1 * num2
        "/" -> if (num2 != 0.0) num1 / num2 else Double.NaN
        else -> Double.NaN
    }

    println("Result: $num1 $operator $num2 = $result")
}
"""),

    3: ("Data Classes", "Kotlin data class example", """data class Person(
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
"""),

    4: ("List Operations", "Kotlin list operations", """fun main() {
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
"""),

    5: ("Null Safety", "Kotlin null safety example", """fun main() {
    // Non-nullable type
    var name: String = "Kotlin"
    // name = null // This would cause compilation error

    // Nullable type
    var nullableName: String? = "Kotlin"
    nullableName = null

    // Safe call operator
    println("Length: ${nullableName?.length}")

    // Elvis operator
    val length = nullableName?.length ?: 0
    println("Length with default: $length")

    // let function
    nullableName?.let {
        println("Name is not null: $it")
    }

    nullableName = "Kotlin"
    nullableName?.let {
        println("Name is not null: $it")
    }

    // Not-null assertion
    // val len = nullableName!!.length // Use with caution
}
"""),
}

# Generate remaining programs (6-100)
for i in range(6, 101):
    if i <= 20:
        # Basic Kotlin Features
        code = f"""fun main() {{
    println("=== Kotlin Program {i:03d} ===")
    println("Demonstrating basic Kotlin features")

    // Variables
    val immutable = "Cannot be changed"
    var mutable = "Can be changed"

    // String interpolation
    println("Immutable: $immutable")
    println("Mutable: $mutable")

    // When expression
    val result = when (val x = {i}) {{
        in 1..10 -> "Single digit"
        in 11..99 -> "Double digit"
        else -> "Three or more digits"
    }}
    println("Result: $result")
}}
"""
    elif i <= 40:
        # Object-Oriented Programming
        code = f"""class Example{i:03d}(private val name: String) {{
    fun greet() {{
        println("Hello from $name!")
    }}

    fun display() {{
        println("This is example {i:03d}")
    }}
}}

fun main() {{
    val obj = Example{i:03d}("Kotlin OOP")
    obj.greet()
    obj.display()

    // Lambda expression
    val numbers = listOf(1, 2, 3, 4, 5)
    val doubled = numbers.map {{ it * 2 }}
    println("Doubled: $doubled")

    // Higher-order function
    val result = numbers.filter {{ it % 2 == 0 }}.map {{ it * it }}
    println("Even squared: $result")
}}
"""
    elif i <= 60:
        # Functional Programming
        code = f"""fun process(x: Int, operation: (Int) -> Int): Int {{
    return operation(x)
}}

fun main() {{
    println("=== Functional Programming {i:03d} ===")

    // Lambda expressions
    val add = {{ x: Int, y: Int -> x + y }}
    val multiply = {{ x: Int, y: Int -> x * y }}

    println("Add: ${{add(5, 3)}}")
    println("Multiply: ${{multiply(5, 3)}}")

    // Higher-order functions
    val result1 = process(10) {{ it * 2 }}
    val result2 = process(10) {{ it * it }}

    println("Process 1: $result1")
    println("Process 2: $result2")

    // Function composition
    val list = listOf(1, 2, 3, 4, 5)
    val result = list
        .filter {{ it % 2 == 0 }}
        .map {{ it * it }}
        .sum()
    println("Result: $result")
}}
"""
    elif i <= 80:
        # Collections and Sequences
        code = f"""fun main() {{
    println("=== Collections {i:03d} ===")

    // List
    val list = mutableListOf(1, 2, 3, 4, 5)
    list.add(6)
    println("List: $list")

    // Set
    val set = mutableSetOf(1, 2, 3, 3, 4)
    set.add(5)
    println("Set: $set")

    // Map
    val map = mutableMapOf(
        "a" to 1,
        "b" to 2,
        "c" to 3
    )
    map["d"] = 4
    println("Map: $map")

    // Iteration
    list.forEach {{ println("Item: $it") }}

    // Grouping
    val grouped = list.groupBy {{ it % 2 == 0 }}
    println("Grouped: $grouped")
}}
"""
    else:
        # Advanced Features
        code = f"""// Extension function
fun String.isPalindrome(): Boolean {{
    return this == this.reversed()
}}

// Sealed class
sealed class Result {{
    data class Success(val data: String) : Result()
    data class Error(val message: String) : Result()
    object Loading : Result()
}}

fun main() {{
    println("=== Advanced Kotlin {i:03d} ===")

    // Extension function usage
    val word = "radar"
    println("Is '$word' a palindrome? ${{word.isPalindrome()}}")

    // Sealed class usage
    val result: Result = Result.Success("Data loaded")

    when (result) {{
        is Result.Success -> println("Success: ${{result.data}}")
        is Result.Error -> println("Error: ${{result.message}}")
        Result.Loading -> println("Loading...")
    }}

    // Scope functions
    val numbers = mutableListOf(1, 2, 3, 4, 5)
    numbers.apply {{
        add(6)
        add(7)
    }}.also {{
        println("List: $it")
    }}
}}
"""

    kotlin_programs[i] = (f"Program {i}", f"Kotlin program {i}", code)

# Create directories and files
os.makedirs(base_dir, exist_ok=True)

for num, (title, desc, code) in kotlin_programs.items():
    program_dir = f"{base_dir}/{num:03d}_Program"
    os.makedirs(program_dir, exist_ok=True)

    # Write Main.kt
    with open(f"{program_dir}/Main.kt", 'w') as f:
        f.write(code)

    # Create build.gradle.kts for standalone execution
    build_gradle = f"""plugins {{
    kotlin("jvm") version "1.9.0"
    application
}}

group = "com.example"
version = "1.0.0"

repositories {{
    mavenCentral()
}}

dependencies {{
    implementation(kotlin("stdlib"))
}}

application {{
    mainClass.set("MainKt")
}}

tasks.withType<org.jetbrains.kotlin.gradle.tasks.KotlinCompile> {{
    kotlinOptions.jvmTarget = "11"
}}
"""

    with open(f"{program_dir}/build.gradle.kts", 'w') as f:
        f.write(build_gradle)

    print(f"Created: {num:03d} - {title}")

print(f"\nCreated {len(kotlin_programs)} Kotlin programs in {base_dir}")
