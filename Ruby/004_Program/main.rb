#!/usr/bin/env ruby

# Array and Hash - Collections Demonstration
# Shows array and hash operations, blocks, and iterators

puts "=== Ruby Collections ==="

# ===== ARRAYS =====
puts "\n--- Array Operations ---"

# Create array
numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
puts "Original array: #{numbers}"

# Array methods
puts "First element: #{numbers.first}"
puts "Last element: #{numbers.last}"
puts "Length: #{numbers.length}"
puts "Sum: #{numbers.sum}"
puts "Average: #{numbers.sum.to_f / numbers.length}"

# Sorting
puts "Sorted: #{numbers.sort}"
puts "Reverse sorted: #{numbers.sort.reverse}"

# Select (filter)
evens = numbers.select { |n| n.even? }
puts "Even numbers: #{evens}"

odds = numbers.select(&:odd?)
puts "Odd numbers: #{odds}"

# Map (transform)
squares = numbers.map { |n| n ** 2 }
puts "Squares: #{squares}"

doubled = numbers.map { |n| n * 2 }
puts "Doubled: #{doubled}"

# Reduce (accumulate)
product = numbers.reduce(:*)
puts "Product of all: #{product}"

# Find
first_even = numbers.find(&:even?)
puts "First even number: #{first_even}"

# Any? All?
puts "Any number > 5? #{numbers.any? { |n| n > 5 }}"
puts "All numbers > 0? #{numbers.all? { |n| n > 0 }}"

# ===== HASHES =====
puts "\n--- Hash Operations ---"

# Create hash
person = {
  name: "John Doe",
  age: 30,
  city: "New York",
  occupation: "Developer"
}

puts "Person hash: #{person}"

# Access values
puts "Name: #{person[:name]}"
puts "Age: #{person[:age]}"

# Add/Update
person[:email] = "john@example.com"
person[:age] = 31
puts "Updated hash: #{person}"

# Iterate
puts "\nIterating over hash:"
person.each do |key, value|
  puts "  #{key}: #{value}"
end

# Keys and Values
puts "Keys: #{person.keys}"
puts "Values: #{person.values}"

# Check for key
puts "Has email? #{person.key?(:email)}"
puts "Has phone? #{person.key?(:phone)}"

# ===== COMBINED OPERATIONS =====
puts "\n--- Complex Data Structures ---"

students = [
  { name: "Alice", grade: 95 },
  { name: "Bob", grade: 87 },
  { name: "Charlie", grade: 92 },
  { name: "Diana", grade: 88 }
]

puts "Students:"
students.each do |student|
  puts "  #{student[:name]}: #{student[:grade]}"
end

# Find top student
top_student = students.max_by { |s| s[:grade] }
puts "\nTop student: #{top_student[:name]} with grade #{top_student[:grade]}"

# Calculate average grade
avg_grade = students.map { |s| s[:grade] }.sum.to_f / students.length
puts "Average grade: #{avg_grade.round(2)}"

# Students with grade >= 90
honor_students = students.select { |s| s[:grade] >= 90 }
puts "\nHonor students (grade >= 90):"
honor_students.each do |student|
  puts "  #{student[:name]}: #{student[:grade]}"
end
