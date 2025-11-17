import Foundation

// Extension
extension String {
    func isPalindrome() -> Bool {
        return self == String(self.reversed())
    }
}

// Enum with associated values
enum Result {
    case success(String)
    case error(String)
    case loading
}

print("=== Advanced Swift 086 ===")

// Extension usage
let word = "radar"
print("Is '\(word)' a palindrome? \(word.isPalindrome())")

// Enum usage
let result = Result.success("Data loaded")

switch result {
case .success(let data):
    print("Success: \(data)")
case .error(let message):
    print("Error: \(message)")
case .loading:
    print("Loading...")
}

// Generics
func swap<T>(_ a: inout T, _ b: inout T) {
    let temp = a
    a = b
    b = temp
}

var x = 5, y = 10
swap(&x, &y)
print("Swapped: x=\(x), y=\(y)")
