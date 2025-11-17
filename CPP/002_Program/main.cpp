#include <iostream>
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

        cout << "\nContinue? (y/n): ";
        cin >> continueCalc;

    } while (continueCalc == 'y' || continueCalc == 'Y');

    cout << "Thank you for using the calculator!" << endl;

    return 0;
}

void displayMenu() {
    cout << "\n--- Calculator Menu ---" << endl;
    cout << "+ : Addition" << endl;
    cout << "- : Subtraction" << endl;
    cout << "* : Multiplication" << endl;
    cout << "/ : Division" << endl;
    cout << "----------------------\n" << endl;
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
