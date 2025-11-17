#!/usr/bin/env ruby

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
  puts "\nContent of #{filename}:"
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
  puts "\nFile has #{lines.length} lines:"
  lines.each_with_index do |line, index|
    puts "Line #{index + 1}: #{line.chomp}"
  end
rescue => e
  puts "Error reading file: #{e.message}"
end

def file_info(filename)
  if File.exist?(filename)
    puts "\nFile Information:"
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
puts "\n1. Writing to file..."
content = <<~TEXT
  Hello, this is a Ruby file I/O example.
  This file demonstrates reading and writing operations.
  Ruby makes file handling elegant and easy.
TEXT

write_to_file(filename, content)

# 2. Read from file
puts "\n2. Reading from file..."
read_from_file(filename)

# 3. Append to file
puts "\n3. Appending to file..."
append_content = <<~TEXT

  This line was appended to the file.
  Appending allows adding content without overwriting.
TEXT

append_to_file(filename, append_content)

# 4. Read file lines
puts "\n4. Reading file by lines..."
read_lines(filename)

# 5. File information
puts "\n5. File information..."
file_info(filename)

# 6. Working with CSV-like data
puts "\n6. Writing structured data..."
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
puts "\nUser Data:"
File.readlines("users.txt").each do |line|
  puts "  #{line.chomp}"
end
