#include <iostream>
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
    cout << "\nAdding elements..." << endl;
    numbers.push_back(10);
    numbers.push_back(30);
    numbers.push_back(20);
    numbers.push_back(50);
    numbers.push_back(40);

    displayVector(numbers, "Original vector");

    // Access elements
    cout << "\nAccessing elements:" << endl;
    cout << "First element: " << numbers.front() << endl;
    cout << "Last element: " << numbers.back() << endl;
    cout << "Element at index 2: " << numbers[2] << endl;

    // Vector size and capacity
    cout << "\nVector properties:" << endl;
    cout << "Size: " << numbers.size() << endl;
    cout << "Capacity: " << numbers.capacity() << endl;
    cout << "Empty: " << (numbers.empty() ? "Yes" : "No") << endl;

    // Sort the vector
    cout << "\nSorting vector..." << endl;
    sort(numbers.begin(), numbers.end());
    displayVector(numbers, "Sorted vector");

    // Reverse the vector
    cout << "\nReversing vector..." << endl;
    reverse(numbers.begin(), numbers.end());
    displayVector(numbers, "Reversed vector");

    // Find an element
    int searchValue = 30;
    auto it = find(numbers.begin(), numbers.end(), searchValue);
    if (it != numbers.end()) {
        cout << "\nFound " << searchValue << " at position " << (it - numbers.begin()) << endl;
    }

    // Insert element
    cout << "\nInserting 25 at position 2..." << endl;
    numbers.insert(numbers.begin() + 2, 25);
    displayVector(numbers, "After insertion");

    // Remove element
    cout << "\nRemoving element at position 1..." << endl;
    numbers.erase(numbers.begin() + 1);
    displayVector(numbers, "After deletion");

    // Clear vector
    cout << "\nClearing vector..." << endl;
    numbers.clear();
    cout << "Size after clear: " << numbers.size() << endl;

    return 0;
}
