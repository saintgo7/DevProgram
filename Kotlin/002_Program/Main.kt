fun main() {
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
