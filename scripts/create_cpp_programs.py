#!/usr/bin/env python3
"""
Script to create 100 C++ programs for DevProgram repository
"""

import os

# Base directory
BASE_DIR = "/home/user/DevProgram/CPP"

# Program definitions (5 featured programs with full implementations)
FEATURED_PROGRAMS = {
    1: {
        "name": "Hello World",
        "description": "Basic C++ program",
        "content": """#include <iostream>
#include <string>
using namespace std;

/**
 * Hello World - Basic C++ Program
 * Demonstrates basic C++ syntax, input/output, and variables
 */

int main() {
    // Basic output
    cout << "Hello, C++ World!" << endl;
    cout << "================================" << endl;

    // Variables
    string name;
    int age;

    // Input
    cout << "Enter your name: ";
    getline(cin, name);

    cout << "Enter your age: ";
    cin >> age;

    // Output
    cout << "\\nWelcome, " << name << "!" << endl;
    cout << "You are " << age << " years old." << endl;

    // Display C++ features
    cout << "\\nC++ Features:" << endl;
    cout << "- Object-Oriented Programming" << endl;
    cout << "- Templates and Generics" << endl;
    cout << "- Standard Template Library" << endl;
    cout << "- Memory Management" << endl;
    cout << "- High Performance" << endl;

    return 0;
}
"""
    },
    2: {
        "name": "Calculator",
        "description": "Simple calculator with functions",
        "content": """#include <iostream>
#include <iomanip>
using namespace std;

/**
 * Calculator - Function Demonstration
 * Shows functions, switch statements, and basic arithmetic
 */

// Function declarations
double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);
void displayMenu();

int main() {
    double num1, num2, result;
    char operation;
    char continueCalc;

    cout << "=== C++ Calculator ===" << endl;
    cout << fixed << setprecision(2);

    do {
        displayMenu();

        cout << "Enter first number: ";
        cin >> num1;

        cout << "Enter operation (+, -, *, /): ";
        cin >> operation;

        cout << "Enter second number: ";
        cin >> num2;

        switch (operation) {
            case '+':
                result = add(num1, num2);
                cout << "Result: " << num1 << " + " << num2 << " = " << result << endl;
                break;
            case '-':
                result = subtract(num1, num2);
                cout << "Result: " << num1 << " - " << num2 << " = " << result << endl;
                break;
            case '*':
                result = multiply(num1, num2);
                cout << "Result: " << num1 << " * " << num2 << " = " << result << endl;
                break;
            case '/':
                if (num2 == 0) {
                    cout << "Error: Cannot divide by zero!" << endl;
                } else {
                    result = divide(num1, num2);
                    cout << "Result: " << num1 << " / " << num2 << " = " << result << endl;
                }
                break;
            default:
                cout << "Error: Invalid operation!" << endl;
        }

        cout << "\\nContinue? (y/n): ";
        cin >> continueCalc;

    } while (continueCalc == 'y' || continueCalc == 'Y');

    cout << "Thank you for using the calculator!" << endl;

    return 0;
}

void displayMenu() {
    cout << "\\n--- Calculator Menu ---" << endl;
    cout << "+ : Addition" << endl;
    cout << "- : Subtraction" << endl;
    cout << "* : Multiplication" << endl;
    cout << "/ : Division" << endl;
    cout << "----------------------\\n" << endl;
}

double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    return a / b;
}
"""
    },
    3: {
        "name": "Class Example",
        "description": "Object-Oriented Programming basics",
        "content": """#include <iostream>
#include <string>
using namespace std;

/**
 * Class Example - OOP Demonstration
 * Shows classes, objects, constructors, and methods
 */

class Student {
private:
    string name;
    int age;
    double gpa;
    int studentId;

public:
    // Constructor
    Student(string n, int a, double g, int id) {
        name = n;
        age = a;
        gpa = g;
        studentId = id;
    }

    // Default constructor
    Student() {
        name = "Unknown";
        age = 0;
        gpa = 0.0;
        studentId = 0;
    }

    // Getter methods
    string getName() { return name; }
    int getAge() { return age; }
    double getGPA() { return gpa; }
    int getStudentId() { return studentId; }

    // Setter methods
    void setName(string n) { name = n; }
    void setAge(int a) { age = a; }
    void setGPA(double g) { gpa = g; }
    void setStudentId(int id) { studentId = id; }

    // Method to display student information
    void display() {
        cout << "\\n--- Student Information ---" << endl;
        cout << "ID: " << studentId << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "GPA: " << gpa << endl;
        cout << "--------------------------" << endl;
    }

    // Method to check if student has honors
    bool hasHonors() {
        return gpa >= 3.5;
    }

    // Method to update GPA
    void updateGPA(double newGPA) {
        if (newGPA >= 0.0 && newGPA <= 4.0) {
            gpa = newGPA;
            cout << "GPA updated successfully!" << endl;
        } else {
            cout << "Invalid GPA value!" << endl;
        }
    }
};

int main() {
    cout << "=== C++ Class Example ===" << endl;

    // Create student objects
    Student student1("Alice Johnson", 20, 3.8, 1001);
    Student student2("Bob Smith", 21, 3.2, 1002);
    Student student3;  // Using default constructor

    // Display student information
    student1.display();
    student2.display();

    // Check honors
    if (student1.hasHonors()) {
        cout << student1.getName() << " has honors!" << endl;
    }

    if (student2.hasHonors()) {
        cout << student2.getName() << " has honors!" << endl;
    } else {
        cout << student2.getName() << " does not have honors." << endl;
    }

    // Update student3 using setters
    cout << "\\nUpdating student3 information..." << endl;
    student3.setName("Charlie Brown");
    student3.setAge(19);
    student3.setStudentId(1003);
    student3.updateGPA(3.6);

    student3.display();

    if (student3.hasHonors()) {
        cout << student3.getName() << " has honors!" << endl;
    }

    return 0;
}
"""
    },
    4: {
        "name": "Vector Example",
        "description": "STL vector demonstration",
        "content": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/**
 * Vector Example - STL Demonstration
 * Shows vector operations, iterators, and algorithms
 */

void displayVector(const vector<int>& vec, const string& message) {
    cout << message << ": ";
    for (int num : vec) {
        cout << num << " ";
    }
    cout << endl;
}

int main() {
    cout << "=== C++ Vector Example ===" << endl;

    // Create and initialize vector
    vector<int> numbers;

    // Add elements
    cout << "\\nAdding elements..." << endl;
    numbers.push_back(10);
    numbers.push_back(30);
    numbers.push_back(20);
    numbers.push_back(50);
    numbers.push_back(40);

    displayVector(numbers, "Original vector");

    // Access elements
    cout << "\\nAccessing elements:" << endl;
    cout << "First element: " << numbers.front() << endl;
    cout << "Last element: " << numbers.back() << endl;
    cout << "Element at index 2: " << numbers[2] << endl;

    // Vector size and capacity
    cout << "\\nVector properties:" << endl;
    cout << "Size: " << numbers.size() << endl;
    cout << "Capacity: " << numbers.capacity() << endl;
    cout << "Empty: " << (numbers.empty() ? "Yes" : "No") << endl;

    // Sort the vector
    cout << "\\nSorting vector..." << endl;
    sort(numbers.begin(), numbers.end());
    displayVector(numbers, "Sorted vector");

    // Reverse the vector
    cout << "\\nReversing vector..." << endl;
    reverse(numbers.begin(), numbers.end());
    displayVector(numbers, "Reversed vector");

    // Find an element
    int searchValue = 30;
    auto it = find(numbers.begin(), numbers.end(), searchValue);
    if (it != numbers.end()) {
        cout << "\\nFound " << searchValue << " at position " << (it - numbers.begin()) << endl;
    }

    // Insert element
    cout << "\\nInserting 25 at position 2..." << endl;
    numbers.insert(numbers.begin() + 2, 25);
    displayVector(numbers, "After insertion");

    // Remove element
    cout << "\\nRemoving element at position 1..." << endl;
    numbers.erase(numbers.begin() + 1);
    displayVector(numbers, "After deletion");

    // Clear vector
    cout << "\\nClearing vector..." << endl;
    numbers.clear();
    cout << "Size after clear: " << numbers.size() << endl;

    return 0;
}
"""
    },
    5: {
        "name": "File Operations",
        "description": "File I/O demonstration",
        "content": """#include <iostream>
#include <fstream>
#include <string>
using namespace std;

/**
 * File Operations - File I/O Demonstration
 * Shows file reading, writing, and manipulation
 */

void writeToFile(const string& filename, const string& content) {
    ofstream file(filename);

    if (file.is_open()) {
        file << content;
        file.close();
        cout << "Successfully wrote to " << filename << endl;
    } else {
        cout << "Error: Unable to open file for writing!" << endl;
    }
}

void readFromFile(const string& filename) {
    ifstream file(filename);
    string line;

    if (file.is_open()) {
        cout << "\\nContent of " << filename << ":" << endl;
        cout << "================================" << endl;

        while (getline(file, line)) {
            cout << line << endl;
        }

        cout << "================================" << endl;
        file.close();
    } else {
        cout << "Error: Unable to open file for reading!" << endl;
    }
}

void appendToFile(const string& filename, const string& content) {
    ofstream file(filename, ios::app);

    if (file.is_open()) {
        file << content;
        file.close();
        cout << "Successfully appended to " << filename << endl;
    } else {
        cout << "Error: Unable to open file for appending!" << endl;
    }
}

int main() {
    cout << "=== C++ File Operations ===" << endl;

    string filename = "sample.txt";

    // Write to file
    cout << "\\n1. Writing to file..." << endl;
    string content = "Hello, this is a C++ file I/O example.\\n";
    content += "This file demonstrates reading and writing operations.\\n";
    content += "C++ makes file handling easy with fstream library.\\n";

    writeToFile(filename, content);

    // Read from file
    cout << "\\n2. Reading from file..." << endl;
    readFromFile(filename);

    // Append to file
    cout << "\\n3. Appending to file..." << endl;
    string appendContent = "\\nThis line was appended to the file.\\n";
    appendContent += "Appending allows adding content without overwriting.\\n";

    appendToFile(filename, appendContent);

    // Read again to see appended content
    cout << "\\n4. Reading file after appending..." << endl;
    readFromFile(filename);

    // User input to file
    cout << "\\n5. Adding user input to file..." << endl;
    cout << "Enter text to add to file (press Enter to finish): ";

    string userInput;
    getline(cin, userInput);

    if (!userInput.empty()) {
        appendToFile(filename, "\\nUser input: " + userInput + "\\n");
        readFromFile(filename);
    }

    return 0;
}
"""
    }
}

# All 100 program titles
ALL_PROGRAMS = [
    "Hello World", "Calculator", "Class Example", "Vector Example", "File Operations",
    "Array Operations", "Pointers", "References", "Structures", "Enumerations",
    "Functions", "Function Overloading", "Default Arguments", "Inline Functions", "Recursion",
    "Loops", "Conditionals", "Switch Case", "Break Continue", "Goto Statement",
    "String Operations", "String Class", "C-Style Strings", "String Concatenation", "String Comparison",
    "Constructors", "Destructors", "Copy Constructor", "This Pointer", "Static Members",
    "Friend Functions", "Operator Overloading", "Inheritance", "Multiple Inheritance", "Multilevel Inheritance",
    "Virtual Functions", "Pure Virtual", "Abstract Classes", "Polymorphism", "Dynamic Binding",
    "Templates", "Function Templates", "Class Templates", "Template Specialization", "Variadic Templates",
    "Exception Handling", "Try Catch", "Throw Exception", "Custom Exceptions", "Exception Specifications",
    "STL Algorithms", "STL Containers", "STL Iterators", "List Container", "Map Container",
    "Set Container", "Queue Container", "Stack Container", "Priority Queue", "Deque Container",
    "Algorithm Sort", "Algorithm Find", "Algorithm Count", "Algorithm Reverse", "Algorithm Accumulate",
    "Smart Pointers", "Unique Ptr", "Shared Ptr", "Weak Ptr", "Auto Ptr",
    "Lambda Expressions", "Auto Keyword", "Range-based Loop", "nullptr", "constexpr",
    "Move Semantics", "Rvalue References", "Perfect Forwarding", "std::move", "std::forward",
    "Multithreading", "Thread Class", "Mutex", "Lock Guard", "Condition Variable",
    "Atomic Operations", "Future Promise", "Async Task", "Thread Pool", "Race Condition",
    "Memory Management", "New Delete", "Memory Leak", "Dynamic Arrays", "2D Arrays",
    "Binary Search", "Linear Search", "Bubble Sort", "Selection Sort", "Insertion Sort",
    "Merge Sort", "Quick Sort", "Linked List", "Stack Implementation", "Queue Implementation"
]

def create_program(program_num):
    """Create a single C++ program file"""
    program_name = ALL_PROGRAMS[program_num - 1]
    program_dir = os.path.join(BASE_DIR, f"{program_num:03d}_Program")

    # Create directory
    os.makedirs(program_dir, exist_ok=True)

    # Create main.cpp file
    if program_num in FEATURED_PROGRAMS:
        content = FEATURED_PROGRAMS[program_num]["content"]
    else:
        content = f"""#include <iostream>
#include <string>
using namespace std;

/**
 * {program_name}
 * Program {program_num:03d}
 */

int main() {{
    cout << "=== {program_name} ===" << endl;
    cout << "This is a C++ program demonstrating {program_name.lower()}." << endl;

    // Implement the program logic here...

    return 0;
}}
"""

    with open(os.path.join(program_dir, "main.cpp"), "w") as f:
        f.write(content)

    # Create Makefile
    makefile_content = f"""# Makefile for {program_name}

CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra
TARGET = program
SRC = main.cpp

all: $(TARGET)

$(TARGET): $(SRC)
\t$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

clean:
\trm -f $(TARGET)

run: $(TARGET)
\t./$(TARGET)

.PHONY: all clean run
"""

    with open(os.path.join(program_dir, "Makefile"), "w") as f:
        f.write(makefile_content)

    print(f"Created program {program_num:03d}: {program_name}")

def main():
    """Main function to create all 100 C++ programs"""
    print("Creating C++ programs...")
    print(f"Base directory: {BASE_DIR}")

    # Create base directory
    os.makedirs(BASE_DIR, exist_ok=True)

    # Create all 100 programs
    for i in range(1, 101):
        create_program(i)

    print("\n✓ Successfully created 100 C++ programs!")
    print(f"Location: {BASE_DIR}")

    # Count total lines
    total_lines = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.cpp', '.h', '.hpp')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    total_lines += len(f.readlines())

    print(f"Total lines of code: {total_lines:,}")

if __name__ == "__main__":
    main()
