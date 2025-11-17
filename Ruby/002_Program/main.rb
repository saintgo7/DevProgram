#!/usr/bin/env ruby

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
    puts "\n--- Calculator Menu ---"
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

      puts "\nResult: #{result}"
    end

    puts "Thank you for using the calculator!"
  end
end

# Run the calculator
calculator = Calculator.new
calculator.run
