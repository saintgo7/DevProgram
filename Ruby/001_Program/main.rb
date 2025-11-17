#!/usr/bin/env ruby

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

puts "\nRuby Features:"
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

puts "\nLanguage Information:"
info.each do |key, value|
  puts "#{key.to_s.capitalize}: #{value}"
end

# Simple method
def greet(name)
  "Hello, #{name}!"
end

puts "\n#{greet('World')}"
