import Foundation

var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original array: \(numbers)")

// Filter
let evenNumbers = numbers.filter { $0 % 2 == 0 }
print("Even numbers: \(evenNumbers)")

// Map
let squared = numbers.map { $0 * $0 }
print("Squared: \(squared)")

// Reduce
let sum = numbers.reduce(0, +)
print("Sum: \(sum)")

// Contains
print("Contains 5: \(numbers.contains(5))")

// Sort
let sorted = numbers.sorted(by: >)
print("Sorted descending: \(sorted)")
