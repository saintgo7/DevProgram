import Foundation

// Optional declaration
var optionalName: String? = "Swift"
var optionalAge: Int? = nil

// Optional binding
if let name = optionalName {
    print("Name is \(name)")
} else {
    print("Name is nil")
}

// Optional chaining
let length = optionalName?.count
print("Length: \(length ?? 0)")

// Nil coalescing operator
let actualName = optionalName ?? "Unknown"
print("Actual name: \(actualName)")

// Guard statement
func greet(name: String?) {
    guard let unwrappedName = name else {
        print("No name provided")
        return
    }
    print("Hello, \(unwrappedName)!")
}

greet(name: optionalName)
greet(name: nil)
