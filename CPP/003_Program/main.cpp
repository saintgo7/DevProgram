#include <iostream>
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
        cout << "\n--- Student Information ---" << endl;
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
    cout << "\nUpdating student3 information..." << endl;
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
