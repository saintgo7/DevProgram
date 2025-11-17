import Foundation

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

print("Result: \(num1) \(op) \(num2) = \(result)")
