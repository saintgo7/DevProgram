fun main() {
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
