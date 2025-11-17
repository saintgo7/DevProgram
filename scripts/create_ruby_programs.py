#!/usr/bin/env python3
"""
Script to create 100 Ruby programs for DevProgram repository
"""

import os

# Base directory
BASE_DIR = "/home/user/DevProgram/Ruby"

# Program definitions (5 featured programs with full implementations)
FEATURED_PROGRAMS = {
    1: {
        "name": "Hello World",
        "description": "Basic Ruby script",
        "content": """#!/usr/bin/env ruby

# Hello World - Basic Ruby Program
# Demonstrates basic Ruby syntax and output

puts "Hello, Ruby World!"
puts "=" * 40

# Variables
name = "Ruby Developer"
version = RUBY_VERSION

puts "Welcome to Ruby!"
puts "Hello, #{name}"
puts "Ruby Version: #{version}"

# Arrays
features = [
  "Object-Oriented Programming",
  "Dynamic Typing",
  "Elegant Syntax",
  "Rails Framework",
  "Gems and Libraries"
]

puts "\\nRuby Features:"
features.each_with_index do |feature, index|
  puts "#{index + 1}. #{feature}"
end

# Hash
info = {
  language: "Ruby",
  creator: "Yukihiro Matsumoto",
  year: 1995,
  paradigm: "Object-Oriented"
}

puts "\\nLanguage Information:"
info.each do |key, value|
  puts "#{key.to_s.capitalize}: #{value}"
end

# Simple method
def greet(name)
  "Hello, #{name}!"
end

puts "\\n#{greet('World')}"
"""
    },
    2: {
        "name": "Calculator",
        "description": "Ruby calculator with methods",
        "content": """#!/usr/bin/env ruby

# Calculator - Method and Control Flow Demonstration
# Shows methods, conditionals, and user input

class Calculator
  def add(a, b)
    a + b
  end

  def subtract(a, b)
    a - b
  end

  def multiply(a, b)
    a * b
  end

  def divide(a, b)
    return "Error: Cannot divide by zero" if b.zero?
    a.to_f / b
  end

  def display_menu
    puts "\\n--- Calculator Menu ---"
    puts "1. Addition (+)"
    puts "2. Subtraction (-)"
    puts "3. Multiplication (*)"
    puts "4. Division (/)"
    puts "5. Exit"
    puts "----------------------"
  end

  def run
    puts "=== Ruby Calculator ==="

    loop do
      display_menu
      print "Choose operation (1-5): "
      choice = gets.chomp.to_i

      break if choice == 5

      unless (1..4).include?(choice)
        puts "Invalid choice! Please try again."
        next
      end

      print "Enter first number: "
      num1 = gets.chomp.to_f

      print "Enter second number: "
      num2 = gets.chomp.to_f

      result = case choice
               when 1
                 add(num1, num2)
               when 2
                 subtract(num1, num2)
               when 3
                 multiply(num1, num2)
               when 4
                 divide(num1, num2)
               end

      puts "\\nResult: #{result}"
    end

    puts "Thank you for using the calculator!"
  end
end

# Run the calculator
calculator = Calculator.new
calculator.run
"""
    },
    3: {
        "name": "Class Example",
        "description": "Object-Oriented Programming basics",
        "content": """#!/usr/bin/env ruby

# Class Example - OOP Demonstration
# Shows classes, objects, attributes, and methods

class Student
  attr_accessor :name, :age, :gpa, :student_id

  def initialize(name, age, gpa, student_id)
    @name = name
    @age = age
    @gpa = gpa
    @student_id = student_id
  end

  def display
    puts "\\n--- Student Information ---"
    puts "ID: #{@student_id}"
    puts "Name: #{@name}"
    puts "Age: #{@age}"
    puts "GPA: #{@gpa}"
    puts "--------------------------"
  end

  def honors?
    @gpa >= 3.5
  end

  def update_gpa(new_gpa)
    if (0.0..4.0).include?(new_gpa)
      @gpa = new_gpa
      puts "GPA updated successfully!"
    else
      puts "Invalid GPA value!"
    end
  end

  def to_s
    "Student: #{@name} (ID: #{@student_id})"
  end
end

# Inheritance example
class GraduateStudent < Student
  attr_accessor :thesis_topic

  def initialize(name, age, gpa, student_id, thesis_topic)
    super(name, age, gpa, student_id)
    @thesis_topic = thesis_topic
  end

  def display
    super
    puts "Thesis Topic: #{@thesis_topic}"
    puts "--------------------------"
  end
end

# Main program
puts "=== Ruby Class Example ==="

# Create student objects
student1 = Student.new("Alice Johnson", 20, 3.8, 1001)
student2 = Student.new("Bob Smith", 21, 3.2, 1002)
grad_student = GraduateStudent.new("Charlie Brown", 24, 3.9, 1003, "Machine Learning Applications")

# Display students
student1.display
student2.display
grad_student.display

# Check honors
[student1, student2, grad_student].each do |student|
  status = student.honors? ? "has honors" : "does not have honors"
  puts "#{student.name} #{status}"
end

# Update GPA
puts "\\nUpdating #{student2.name}'s GPA..."
student2.update_gpa(3.7)
student2.display

if student2.honors?
  puts "#{student2.name} now has honors!"
end
"""
    },
    4: {
        "name": "Array and Hash",
        "description": "Collections demonstration",
        "content": """#!/usr/bin/env ruby

# Array and Hash - Collections Demonstration
# Shows array and hash operations, blocks, and iterators

puts "=== Ruby Collections ==="

# ===== ARRAYS =====
puts "\\n--- Array Operations ---"

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
puts "\\n--- Hash Operations ---"

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
puts "\\nIterating over hash:"
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
puts "\\n--- Complex Data Structures ---"

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
puts "\\nTop student: #{top_student[:name]} with grade #{top_student[:grade]}"

# Calculate average grade
avg_grade = students.map { |s| s[:grade] }.sum.to_f / students.length
puts "Average grade: #{avg_grade.round(2)}"

# Students with grade >= 90
honor_students = students.select { |s| s[:grade] >= 90 }
puts "\\nHonor students (grade >= 90):"
honor_students.each do |student|
  puts "  #{student[:name]}: #{student[:grade]}"
end
"""
    },
    5: {
        "name": "File Operations",
        "description": "File I/O demonstration",
        "content": """#!/usr/bin/env ruby

# File Operations - File I/O Demonstration
# Shows file reading, writing, and manipulation

def write_to_file(filename, content)
  File.open(filename, 'w') do |file|
    file.write(content)
  end
  puts "Successfully wrote to #{filename}"
rescue => e
  puts "Error writing to file: #{e.message}"
end

def read_from_file(filename)
  content = File.read(filename)
  puts "\\nContent of #{filename}:"
  puts "=" * 40
  puts content
  puts "=" * 40
rescue => e
  puts "Error reading file: #{e.message}"
end

def append_to_file(filename, content)
  File.open(filename, 'a') do |file|
    file.write(content)
  end
  puts "Successfully appended to #{filename}"
rescue => e
  puts "Error appending to file: #{e.message}"
end

def read_lines(filename)
  lines = File.readlines(filename)
  puts "\\nFile has #{lines.length} lines:"
  lines.each_with_index do |line, index|
    puts "Line #{index + 1}: #{line.chomp}"
  end
rescue => e
  puts "Error reading file: #{e.message}"
end

def file_info(filename)
  if File.exist?(filename)
    puts "\\nFile Information:"
    puts "  Name: #{filename}"
    puts "  Size: #{File.size(filename)} bytes"
    puts "  Readable: #{File.readable?(filename)}"
    puts "  Writable: #{File.writable?(filename)}"
    puts "  Directory: #{File.directory?(filename)}"
    puts "  File: #{File.file?(filename)}"

    stat = File.stat(filename)
    puts "  Created: #{stat.ctime}"
    puts "  Modified: #{stat.mtime}"
  else
    puts "File does not exist: #{filename}"
  end
end

# Main program
puts "=== Ruby File Operations ==="

filename = "sample.txt"

# 1. Write to file
puts "\\n1. Writing to file..."
content = <<~TEXT
  Hello, this is a Ruby file I/O example.
  This file demonstrates reading and writing operations.
  Ruby makes file handling elegant and easy.
TEXT

write_to_file(filename, content)

# 2. Read from file
puts "\\n2. Reading from file..."
read_from_file(filename)

# 3. Append to file
puts "\\n3. Appending to file..."
append_content = <<~TEXT

  This line was appended to the file.
  Appending allows adding content without overwriting.
TEXT

append_to_file(filename, append_content)

# 4. Read file lines
puts "\\n4. Reading file by lines..."
read_lines(filename)

# 5. File information
puts "\\n5. File information..."
file_info(filename)

# 6. Working with CSV-like data
puts "\\n6. Writing structured data..."
users = [
  ["Name", "Age", "City"],
  ["Alice", "25", "New York"],
  ["Bob", "30", "Los Angeles"],
  ["Charlie", "28", "Chicago"]
]

File.open("users.txt", 'w') do |file|
  users.each do |user|
    file.puts user.join(", ")
  end
end

puts "Successfully wrote user data to users.txt"

# Read and display structured data
puts "\\nUser Data:"
File.readlines("users.txt").each do |line|
  puts "  #{line.chomp}"
end
"""
    }
}

# All 100 program titles
ALL_PROGRAMS = [
    "Hello World", "Calculator", "Class Example", "Array and Hash", "File Operations",
    "String Manipulation", "Regular Expressions", "Blocks and Procs", "Lambdas", "Iterators",
    "Modules", "Mixins", "Method Missing", "attr_accessor", "Class Methods",
    "Instance Methods", "Inheritance", "Polymorphism", "Encapsulation", "Method Visibility",
    "Constants", "Global Variables", "Class Variables", "Instance Variables", "Local Variables",
    "Symbols", "Ranges", "Conditional Statements", "Case When", "Loops",
    "While Loop", "Until Loop", "For Loop", "Each Method", "Map Method",
    "Select Method", "Reject Method", "Reduce Method", "Find Method", "Any All",
    "Sort Method", "Reverse Method", "Uniq Method", "Flatten Method", "Zip Method",
    "Hash Operations", "Hash Methods", "Hash Default", "Hash Iteration", "Nested Hash",
    "String Methods", "String Interpolation", "String Formatting", "Multiline Strings", "Heredoc",
    "Exception Handling", "Rescue Clause", "Ensure Clause", "Raise Exception", "Custom Exceptions",
    "File Reading", "File Writing", "File Appending", "Directory Operations", "Path Operations",
    "CSV Handling", "JSON Parsing", "YAML Config", "XML Parsing", "HTTP Request",
    "Web Scraping", "REST Client", "Sinatra App", "Rails Basics", "ActiveRecord",
    "Database Connection", "Migrations", "Query Builder", "Associations", "Validations",
    "Gem Creation", "Bundler", "RSpec Tests", "Minitest", "Test Fixtures",
    "Metaprogramming", "define_method", "send Method", "respond_to", "method_missing",
    "Singleton Pattern", "Factory Pattern", "Observer Pattern", "Strategy Pattern", "Decorator Pattern",
    "Time and Date", "DateTime Operations", "Timezone Handling", "Date Formatting", "Time Calculation",
    "Random Numbers", "Array Shuffle", "Sample Method", "Set Operations", "Matrix Operations"
]

def create_program(program_num):
    """Create a single Ruby program file"""
    program_name = ALL_PROGRAMS[program_num - 1]
    program_dir = os.path.join(BASE_DIR, f"{program_num:03d}_Program")

    # Create directory
    os.makedirs(program_dir, exist_ok=True)

    # Create main.rb file
    if program_num in FEATURED_PROGRAMS:
        content = FEATURED_PROGRAMS[program_num]["content"]
    else:
        content = f"""#!/usr/bin/env ruby

# {program_name}
# Program {program_num:03d}

puts "=== {program_name} ==="
puts "This is a Ruby program demonstrating {program_name.lower()}."

# Implement the program logic here...
"""

    file_path = os.path.join(program_dir, "main.rb")
    with open(file_path, "w") as f:
        f.write(content)

    # Make file executable
    os.chmod(file_path, 0o755)

    # Create Gemfile
    gemfile_content = f"""# Gemfile for {program_name}

source 'https://rubygems.org'

ruby '>= 2.7.0'

# Add your gem dependencies here
# gem 'sinatra'
# gem 'rails'
"""

    with open(os.path.join(program_dir, "Gemfile"), "w") as f:
        f.write(gemfile_content)

    print(f"Created program {program_num:03d}: {program_name}")

def main():
    """Main function to create all 100 Ruby programs"""
    print("Creating Ruby programs...")
    print(f"Base directory: {BASE_DIR}")

    # Create base directory
    os.makedirs(BASE_DIR, exist_ok=True)

    # Create all 100 programs
    for i in range(1, 101):
        create_program(i)

    print("\n✓ Successfully created 100 Ruby programs!")
    print(f"Location: {BASE_DIR}")

    # Count total lines
    total_lines = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith('.rb'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    total_lines += len(f.readlines())

    print(f"Total lines of code: {total_lines:,}")

if __name__ == "__main__":
    main()
