import Foundation

func process(_ x: Int, operation: (Int) -> Int) -> Int {
    return operation(x)
}

print("=== Functional Programming 044 ===")

// Closures
let add: (Int, Int) -> Int = { $0 + $1 }
let multiply: (Int, Int) -> Int = { $0 * $1 }

print("Add: \(add(5, 3))")
print("Multiply: \(multiply(5, 3))")

// Higher-order functions
let result1 = process(10) { $0 * 2 }
let result2 = process(10) { $0 * $0 }

print("Process 1: \(result1)")
print("Process 2: \(result2)")

// Chaining
let list = [1, 2, 3, 4, 5]
let result = list
    .filter { $0 % 2 == 0 }
    .map { $0 * $0 }
    .reduce(0, +)
print("Result: \(result)")
