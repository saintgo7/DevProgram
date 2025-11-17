#!/usr/bin/env ruby

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
    puts "\n--- Student Information ---"
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
puts "\nUpdating #{student2.name}'s GPA..."
student2.update_gpa(3.7)
student2.display

if student2.honors?
  puts "#{student2.name} now has honors!"
end
