#include <iostream>
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
        cout << "\nContent of " << filename << ":" << endl;
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
    cout << "\n1. Writing to file..." << endl;
    string content = "Hello, this is a C++ file I/O example.\n";
    content += "This file demonstrates reading and writing operations.\n";
    content += "C++ makes file handling easy with fstream library.\n";

    writeToFile(filename, content);

    // Read from file
    cout << "\n2. Reading from file..." << endl;
    readFromFile(filename);

    // Append to file
    cout << "\n3. Appending to file..." << endl;
    string appendContent = "\nThis line was appended to the file.\n";
    appendContent += "Appending allows adding content without overwriting.\n";

    appendToFile(filename, appendContent);

    // Read again to see appended content
    cout << "\n4. Reading file after appending..." << endl;
    readFromFile(filename);

    // User input to file
    cout << "\n5. Adding user input to file..." << endl;
    cout << "Enter text to add to file (press Enter to finish): ";

    string userInput;
    getline(cin, userInput);

    if (!userInput.empty()) {
        appendToFile(filename, "\nUser input: " + userInput + "\n");
        readFromFile(filename);
    }

    return 0;
}
