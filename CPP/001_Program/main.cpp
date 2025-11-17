#include <iostream>
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
    cout << "\nWelcome, " << name << "!" << endl;
    cout << "You are " << age << " years old." << endl;

    // Display C++ features
    cout << "\nC++ Features:" << endl;
    cout << "- Object-Oriented Programming" << endl;
    cout << "- Templates and Generics" << endl;
    cout << "- Standard Template Library" << endl;
    cout << "- Memory Management" << endl;
    cout << "- High Performance" << endl;

    return 0;
}
