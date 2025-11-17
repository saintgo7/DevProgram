import Foundation

print("=== Collections 066 ===")

// Array
var array = [1, 2, 3, 4, 5]
array.append(6)
print("Array: \(array)")

// Set
var set: Set = [1, 2, 3, 3, 4]
set.insert(5)
print("Set: \(set)")

// Dictionary
var dict = [
    "a": 1,
    "b": 2,
    "c": 3
]
dict["d"] = 4
print("Dictionary: \(dict)")

// Iteration
array.forEach { print("Item: \($0)") }

// Grouping
let grouped = Dictionary(grouping: array) { $0 % 2 == 0 }
print("Grouped: \(grouped)")
