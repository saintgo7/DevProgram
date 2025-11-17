fun main() {
    println("=== Collections 071 ===")

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
    list.forEach { println("Item: $it") }

    // Grouping
    val grouped = list.groupBy { it % 2 == 0 }
    println("Grouped: $grouped")
}
