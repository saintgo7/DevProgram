#!/usr/bin/env python3
"""
Create 100 Swift programs
"""

import os

base_dir = "/home/user/DevProgram/Swift"

# Swift program templates
swift_programs = {
    1: ("Hello World", "Basic Swift hello world", """import Foundation

print("Hello, Swift!")
print("Welcome to Swift Programming")
"""),

    2: ("Calculator", "Simple calculator", """import Foundation

print("=== Swift Calculator ===")
print("Enter first number: ", terminator: "")
let num1 = Double(readLine() ?? "0") ?? 0.0

print("Enter operator (+, -, *, /): ", terminator: "")
let op = readLine() ?? "+"

print("Enter second number: ", terminator: "")
let num2 = Double(readLine() ?? "0") ?? 0.0

var result: Double = 0.0

switch op {
case "+":
    result = num1 + num2
case "-":
    result = num1 - num2
case "*":
    result = num1 * num2
case "/":
    result = num2 != 0 ? num1 / num2 : 0
default:
    print("Invalid operator")
}

print("Result: \\(num1) \\(op) \\(num2) = \\(result)")
"""),

    3: ("Structs and Classes", "Swift structs and classes", """import Foundation

struct Person {
    var name: String
    var age: Int

    func introduce() {
        print("Hi, I'm \\(name) and I'm \\(age) years old")
    }
}

class Employee {
    var name: String
    var position: String

    init(name: String, position: String) {
        self.name = name
        self.position = position
    }

    func work() {
        print("\\(name) is working as \\(position)")
    }
}

let person = Person(name: "Alice", age: 30)
person.introduce()

let employee = Employee(name: "Bob", position: "Developer")
employee.work()
"""),

    4: ("Arrays and Collections", "Swift array operations", """import Foundation

var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original array: \\(numbers)")

// Filter
let evenNumbers = numbers.filter { $0 % 2 == 0 }
print("Even numbers: \\(evenNumbers)")

// Map
let squared = numbers.map { $0 * $0 }
print("Squared: \\(squared)")

// Reduce
let sum = numbers.reduce(0, +)
print("Sum: \\(sum)")

// Contains
print("Contains 5: \\(numbers.contains(5))")

// Sort
let sorted = numbers.sorted(by: >)
print("Sorted descending: \\(sorted)")
"""),

    5: ("Optionals", "Swift optional handling", """import Foundation

// Optional declaration
var optionalName: String? = "Swift"
var optionalAge: Int? = nil

// Optional binding
if let name = optionalName {
    print("Name is \\(name)")
} else {
    print("Name is nil")
}

// Optional chaining
let length = optionalName?.count
print("Length: \\(length ?? 0)")

// Nil coalescing operator
let actualName = optionalName ?? "Unknown"
print("Actual name: \\(actualName)")

// Guard statement
func greet(name: String?) {
    guard let unwrappedName = name else {
        print("No name provided")
        return
    }
    print("Hello, \\(unwrappedName)!")
}

greet(name: optionalName)
greet(name: nil)
"""),
}

# Generate remaining programs (6-100)
for i in range(6, 101):
    if i <= 20:
        # Basic Swift Features
        code = f"""import Foundation

print("=== Swift Program {i:03d} ===")
print("Demonstrating basic Swift features")

// Variables and constants
let constant = "Cannot be changed"
var variable = "Can be changed"

print("Constant: \\(constant)")
print("Variable: \\(variable)")

// String interpolation
let programNumber = {i}
print("This is program number \\(programNumber)")

// Control flow
switch programNumber {{
case 1...10:
    print("Single digit")
case 11...99:
    print("Double digit")
default:
    print("Three or more digits")
}}
"""
    elif i <= 40:
        # Object-Oriented Programming
        code = f"""import Foundation

class Example{i:03d} {{
    private var name: String

    init(name: String) {{
        self.name = name
    }}

    func greet() {{
        print("Hello from \\(name)!")
    }}

    func display() {{
        print("This is example {i:03d}")
    }}
}}

let obj = Example{i:03d}(name: "Swift OOP")
obj.greet()
obj.display()

// Closures
let numbers = [1, 2, 3, 4, 5]
let doubled = numbers.map {{ $0 * 2 }}
print("Doubled: \\(doubled)")

// Filter and map
let result = numbers.filter {{ $0 % 2 == 0 }}.map {{ $0 * $0 }}
print("Even squared: \\(result)")
"""
    elif i <= 60:
        # Functional Programming
        code = f"""import Foundation

func process(_ x: Int, operation: (Int) -> Int) -> Int {{
    return operation(x)
}}

print("=== Functional Programming {i:03d} ===")

// Closures
let add: (Int, Int) -> Int = {{ $0 + $1 }}
let multiply: (Int, Int) -> Int = {{ $0 * $1 }}

print("Add: \\(add(5, 3))")
print("Multiply: \\(multiply(5, 3))")

// Higher-order functions
let result1 = process(10) {{ $0 * 2 }}
let result2 = process(10) {{ $0 * $0 }}

print("Process 1: \\(result1)")
print("Process 2: \\(result2)")

// Chaining
let list = [1, 2, 3, 4, 5]
let result = list
    .filter {{ $0 % 2 == 0 }}
    .map {{ $0 * $0 }}
    .reduce(0, +)
print("Result: \\(result)")
"""
    elif i <= 80:
        # Collections and Protocols
        code = f"""import Foundation

print("=== Collections {i:03d} ===")

// Array
var array = [1, 2, 3, 4, 5]
array.append(6)
print("Array: \\(array)")

// Set
var set: Set = [1, 2, 3, 3, 4]
set.insert(5)
print("Set: \\(set)")

// Dictionary
var dict = [
    "a": 1,
    "b": 2,
    "c": 3
]
dict["d"] = 4
print("Dictionary: \\(dict)")

// Iteration
array.forEach {{ print("Item: \\($0)") }}

// Grouping
let grouped = Dictionary(grouping: array) {{ $0 % 2 == 0 }}
print("Grouped: \\(grouped)")
"""
    else:
        # Advanced Features
        code = f"""import Foundation

// Extension
extension String {{
    func isPalindrome() -> Bool {{
        return self == String(self.reversed())
    }}
}}

// Enum with associated values
enum Result {{
    case success(String)
    case error(String)
    case loading
}}

print("=== Advanced Swift {i:03d} ===")

// Extension usage
let word = "radar"
print("Is '\\(word)' a palindrome? \\(word.isPalindrome())")

// Enum usage
let result = Result.success("Data loaded")

switch result {{
case .success(let data):
    print("Success: \\(data)")
case .error(let message):
    print("Error: \\(message)")
case .loading:
    print("Loading...")
}}

// Generics
func swap<T>(_ a: inout T, _ b: inout T) {{
    let temp = a
    a = b
    b = temp
}}

var x = 5, y = 10
swap(&x, &y)
print("Swapped: x=\\(x), y=\\(y)")
"""

    swift_programs[i] = (f"Program {i}", f"Swift program {i}", code)

# Create directories and files
os.makedirs(base_dir, exist_ok=True)

for num, (title, desc, code) in swift_programs.items():
    program_dir = f"{base_dir}/{num:03d}_Program"
    os.makedirs(program_dir, exist_ok=True)

    # Write main.swift
    with open(f"{program_dir}/main.swift", 'w') as f:
        f.write(code)

    # Create Package.swift
    package_swift = f"""// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program{num:03d}",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program{num:03d}",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
"""

    with open(f"{program_dir}/Package.swift", 'w') as f:
        f.write(package_swift)

    print(f"Created: {num:03d} - {title}")

print(f"\nCreated {len(swift_programs)} Swift programs in {base_dir}")
