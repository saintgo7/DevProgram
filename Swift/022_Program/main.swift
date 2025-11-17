import Foundation

class Example022 {
    private var name: String

    init(name: String) {
        self.name = name
    }

    func greet() {
        print("Hello from \(name)!")
    }

    func display() {
        print("This is example 022")
    }
}

let obj = Example022(name: "Swift OOP")
obj.greet()
obj.display()

// Closures
let numbers = [1, 2, 3, 4, 5]
let doubled = numbers.map { $0 * 2 }
print("Doubled: \(doubled)")

// Filter and map
let result = numbers.filter { $0 % 2 == 0 }.map { $0 * $0 }
print("Even squared: \(result)")
