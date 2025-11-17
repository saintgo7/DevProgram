import Foundation

struct Person {
    var name: String
    var age: Int

    func introduce() {
        print("Hi, I'm \(name) and I'm \(age) years old")
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
        print("\(name) is working as \(position)")
    }
}

let person = Person(name: "Alice", age: 30)
person.introduce()

let employee = Employee(name: "Bob", position: "Developer")
employee.work()
