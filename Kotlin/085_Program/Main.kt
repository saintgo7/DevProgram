// Extension function
fun String.isPalindrome(): Boolean {
    return this == this.reversed()
}

// Sealed class
sealed class Result {
    data class Success(val data: String) : Result()
    data class Error(val message: String) : Result()
    object Loading : Result()
}

fun main() {
    println("=== Advanced Kotlin 085 ===")

    // Extension function usage
    val word = "radar"
    println("Is '$word' a palindrome? ${word.isPalindrome()}")

    // Sealed class usage
    val result: Result = Result.Success("Data loaded")

    when (result) {
        is Result.Success -> println("Success: ${result.data}")
        is Result.Error -> println("Error: ${result.message}")
        Result.Loading -> println("Loading...")
    }

    // Scope functions
    val numbers = mutableListOf(1, 2, 3, 4, 5)
    numbers.apply {
        add(6)
        add(7)
    }.also {
        println("List: $it")
    }
}
