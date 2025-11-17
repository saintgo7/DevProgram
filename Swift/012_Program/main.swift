import Foundation

print("=== Swift Program 012 ===")
print("Demonstrating basic Swift features")

// Variables and constants
let constant = "Cannot be changed"
var variable = "Can be changed"

print("Constant: \(constant)")
print("Variable: \(variable)")

// String interpolation
let programNumber = 12
print("This is program number \(programNumber)")

// Control flow
switch programNumber {
case 1...10:
    print("Single digit")
case 11...99:
    print("Double digit")
default:
    print("Three or more digits")
}
