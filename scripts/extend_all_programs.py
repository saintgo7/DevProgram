#!/usr/bin/env python3
"""
Script to extend Ruby and C++ programs (101-200) and create C and Scala (1-100)
"""

import os

def extend_ruby_programs():
    """Add Ruby programs 101-200 (Rails focus)"""
    BASE_DIR = "/home/user/DevProgram/Ruby"

    programs = [
        # 101-120: Rails Basics
        "Rails Route Config", "Rails Controller CRUD", "Rails Model ActiveRecord", "Rails View ERB", "Rails Form Helper",
        "Rails Migration", "Rails Seeder", "Rails Validation", "Rails Callback", "Rails Association",
        "Rails Scope", "Rails Query", "Rails Join", "Rails Include", "Rails Eager Loading",
        "Rails Pagination", "Rails Search", "Rails Filter", "Rails Sort", "Rails Authentication",

        # 121-140: Rails Advanced
        "Rails Devise", "Rails CanCanCan", "Rails Pundit", "Rails ActionCable", "Rails ActiveJob",
        "Rails Mailer", "Rails Sidekiq", "Rails Redis", "Rails Caching", "Rails Fragment Cache",
        "Rails Session", "Rails Cookie", "Rails Flash", "Rails CSRF", "Rails API",
        "Rails Serializer", "Rails CORS", "Rails JWT", "Rails OAuth", "Rails GraphQL",

        # 141-160: Rails Features
        "Rails File Upload", "Rails ActiveStorage", "Rails ImageProcessing", "Rails ActionText", "Rails ActionMailbox",
        "Rails WebSocket", "Rails Turbo", "Rails Stimulus", "Rails Hotwire", "Rails ViewComponent",
        "Rails Concern", "Rails Service Object", "Rails Decorator", "Rails Presenter", "Rails Form Object",
        "Rails Query Object", "Rails Policy Object", "Rails Observer Pattern", "Rails Repository Pattern", "Rails Factory Pattern",

        # 161-180: Rails Testing & Tools
        "Rails RSpec Model", "Rails RSpec Controller", "Rails RSpec Request", "Rails RSpec Feature", "Rails FactoryBot",
        "Rails Faker", "Rails VCR", "Rails SimpleCov", "Rails Capybara", "Rails Selenium",
        "Rails Minitest", "Rails Fixture", "Rails Mock", "Rails Stub", "Rails TDD",
        "Rails BDD", "Rails Integration Test", "Rails System Test", "Rails Performance Test", "Rails Security Test",

        # 181-200: Rails Ecosystem
        "Rails Webpack", "Rails Importmap", "Rails Sprockets", "Rails Asset Pipeline", "Rails Tailwind",
        "Rails Bootstrap", "Rails SCSS", "Rails PostCSS", "Rails JavaScript", "Rails CoffeeScript",
        "Rails Rake Task", "Rails Generator", "Rails Engine", "Rails Gem Creation", "Rails Docker",
        "Rails Heroku Deploy", "Rails AWS Deploy", "Rails Capistrano", "Rails CI CD", "Rails Monitoring"
    ]

    for i in range(101, 201):
        program_name = programs[i - 101]
        program_dir = os.path.join(BASE_DIR, f"{i:03d}_Program")
        os.makedirs(program_dir, exist_ok=True)

        content = f"""#!/usr/bin/env ruby

# {program_name}
# Program {i:03d}

puts "=== {program_name} ==="
puts "This is a Ruby on Rails program demonstrating {program_name.lower()}."

# Implement the program logic here...
"""

        file_path = os.path.join(program_dir, "main.rb")
        with open(file_path, "w") as f:
            f.write(content)
        os.chmod(file_path, 0o755)

        gemfile_content = f"""# Gemfile for {program_name}

source 'https://rubygems.org'

ruby '>= 3.0.0'

gem 'rails', '~> 7.0'
"""
        with open(os.path.join(program_dir, "Gemfile"), "w") as f:
            f.write(gemfile_content)

    print(f"✓ Created Ruby programs 101-200 (Rails focus)")

def extend_cpp_programs():
    """Add C++ programs 101-200 (Game/System focus)"""
    BASE_DIR = "/home/user/DevProgram/CPP"

    programs = [
        # 101-120: Game Programming Basics
        "Game Loop", "Sprite Rendering", "Collision Detection", "Input Handler", "State Machine",
        "Entity Component System", "Scene Manager", "Resource Manager", "Audio Manager", "Animation System",
        "Particle System", "Physics Engine Basic", "Rigid Body", "Vector Math", "Matrix Transform",
        "Quaternion Rotation", "Camera System", "Viewport", "Frustum Culling", "Level Loading",

        # 121-140: Advanced Game Programming
        "Texture Atlas", "Sprite Batch", "Shader Programming", "Lighting System", "Shadow Mapping",
        "Normal Mapping", "Skeletal Animation", "Inverse Kinematics", "Pathfinding A*", "Behavior Tree",
        "Decision Tree", "Finite State Machine", "Event System", "Message Queue", "Command Pattern Game",
        "Object Pool", "Flyweight Pattern", "Spatial Partitioning", "Quadtree", "Octree",

        # 141-160: System Programming
        "Process Management", "Thread Pool", "Memory Pool", "Custom Allocator", "Garbage Collector",
        "Virtual Machine", "Bytecode Interpreter", "JIT Compiler", "Lexer", "Parser",
        "Abstract Syntax Tree", "Code Generator", "Optimizer", "Register Allocation", "Instruction Scheduler",
        "Cache Optimization", "SIMD Operations", "Intrinsics", "Assembly Integration", "Inline Assembly",

        # 161-180: Low-level Programming
        "System Call Wrapper", "File System", "Directory Walker", "Device Driver Sim", "Kernel Module",
        "Memory Mapped File", "Shared Memory", "Inter Process Communication", "Named Pipe", "Socket Programming",
        "TCP Server", "UDP Server", "HTTP Parser", "Network Protocol", "Packet Serialization",
        "Buffer Management", "Ring Buffer", "Lock-free Queue", "Atomic Operations Advanced", "Memory Barrier",

        # 181-200: Graphics & Multimedia
        "OpenGL Context", "Vertex Buffer", "Index Buffer", "Vertex Array Object", "Frame Buffer",
        "Render Target", "Compute Shader", "Ray Tracing", "Rasterization", "Mesh Loading",
        "OBJ Parser", "FBX Loader", "Image Decoder", "Audio Codec", "Video Decoder",
        "FFT Audio", "DSP Filter", "Compression", "Huffman Coding", "LZ77 Compression"
    ]

    for i in range(101, 201):
        program_name = programs[i - 101]
        program_dir = os.path.join(BASE_DIR, f"{i:03d}_Program")
        os.makedirs(program_dir, exist_ok=True)

        content = f"""#include <iostream>
#include <string>
using namespace std;

/**
 * {program_name}
 * Program {i:03d}
 */

int main() {{
    cout << "=== {program_name} ===" << endl;
    cout << "This is a C++ program demonstrating {program_name.lower()}." << endl;

    // Implement the program logic here...

    return 0;
}}
"""

        with open(os.path.join(program_dir, "main.cpp"), "w") as f:
            f.write(content)

        makefile_content = f"""# Makefile for {program_name}

CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O2
TARGET = program
SRC = main.cpp

all: $(TARGET)

$(TARGET): $(SRC)
\t$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

clean:
\trm -f $(TARGET)

run: $(TARGET)
\t./$(TARGET)

.PHONY: all clean run
"""
        with open(os.path.join(program_dir, "Makefile"), "w") as f:
            f.write(makefile_content)

    print(f"✓ Created C++ programs 101-200 (Game/System focus)")

def create_c_programs():
    """Create C programs 1-100 (System/Embedded)"""
    BASE_DIR = "/home/user/DevProgram/C"
    os.makedirs(BASE_DIR, exist_ok=True)

    programs = [
        # 1-20: Basics
        "Hello World", "Variables Types", "Operators", "Control Flow", "Loops",
        "Functions", "Arrays", "Strings", "Pointers", "Structures",
        "Unions", "Enums", "Typedef", "Preprocessor", "Macros",
        "File IO", "Command Line Args", "Dynamic Memory", "Malloc Free", "Calloc Realloc",

        # 21-40: Intermediate
        "Linked List", "Stack", "Queue", "Binary Tree", "Hash Table",
        "Sorting Algorithms", "Searching Algorithms", "Recursion", "Bit Manipulation", "Bitwise Operators",
        "Function Pointers", "Callback Functions", "Signal Handling", "Process Control", "Fork Exec",
        "Pipes", "Shared Memory IPC", "Message Queues", "Semaphores", "Mutex",

        # 41-60: System Programming
        "File Descriptor", "Dup Dup2", "Select Poll", "Epoll", "Socket Programming",
        "TCP Client", "TCP Server", "UDP Socket", "Unix Domain Socket", "Network Byte Order",
        "Endianness", "Memory Alignment", "Volatile Keyword", "Const Keyword", "Static Keyword",
        "Extern Keyword", "Inline Functions", "Variable Arguments", "Assembly Inline", "System Calls",

        # 61-80: Embedded
        "GPIO Control", "LED Blink", "Button Input", "PWM Control", "ADC Reading",
        "DAC Output", "UART Communication", "I2C Protocol", "SPI Protocol", "Timer Interrupt",
        "External Interrupt", "DMA Transfer", "Watchdog Timer", "Real Time Clock", "Power Management",
        "Sleep Modes", "Register Manipulation", "Bit Fields", "Memory Mapped IO", "Device Driver",

        # 81-100: Advanced
        "Bootloader", "Firmware Update", "Flash Programming", "EEPROM", "SD Card Interface",
        "LCD Display", "Seven Segment", "Keypad Matrix", "Sensor Reading", "Motor Control",
        "PID Controller", "State Machine Embedded", "RTOS Task", "Scheduler", "Context Switch",
        "Critical Section", "Atomic Operations C", "Lock Free Programming", "Bare Metal", "Cross Compilation"
    ]

    for i in range(1, 101):
        program_name = programs[i - 1]
        program_dir = os.path.join(BASE_DIR, f"{i:03d}_Program")
        os.makedirs(program_dir, exist_ok=True)

        content = f"""#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * {program_name}
 * Program {i:03d}
 */

int main(void) {{
    printf("=== {program_name} ===\\n");
    printf("This is a C program demonstrating {program_name.lower()}.\\n");

    // Implement the program logic here...

    return 0;
}}
"""

        with open(os.path.join(program_dir, "main.c"), "w") as f:
            f.write(content)

        makefile_content = f"""# Makefile for {program_name}

CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -O2
TARGET = program
SRC = main.c

all: $(TARGET)

$(TARGET): $(SRC)
\t$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

clean:
\trm -f $(TARGET)

run: $(TARGET)
\t./$(TARGET)

.PHONY: all clean run
"""
        with open(os.path.join(program_dir, "Makefile"), "w") as f:
            f.write(makefile_content)

    print(f"✓ Created C programs 1-100 (System/Embedded)")

def create_scala_programs():
    """Create Scala programs 1-100 (JVM Functional)"""
    BASE_DIR = "/home/user/DevProgram/Scala"
    os.makedirs(BASE_DIR, exist_ok=True)

    programs = [
        # 1-20: Basics
        "Hello World", "Variables Val Var", "Data Types", "String Operations", "Collections List",
        "Array Operations", "Tuples", "Option Type", "Pattern Matching", "Case Classes",
        "Functions", "Higher Order Functions", "Anonymous Functions", "Closures", "Currying",
        "Partial Functions", "Function Composition", "Recursion", "Tail Recursion", "For Comprehension",

        # 21-40: OOP
        "Classes", "Objects", "Inheritance", "Traits", "Abstract Classes",
        "Case Objects", "Companion Objects", "Apply Method", "Constructors", "Access Modifiers",
        "Getters Setters", "Overriding Methods", "Polymorphism", "Type Parameterization", "Variance",
        "Covariance", "Contravariance", "Type Bounds", "Context Bounds", "View Bounds",

        # 41-60: Functional Programming
        "Immutability", "Pure Functions", "Referential Transparency", "First Class Functions", "Map Function",
        "Filter Function", "Reduce Function", "Fold Left", "Fold Right", "FlatMap",
        "Monads", "For Expressions", "Functors", "Applicatives", "Monoids",
        "Either Type", "Try Success Failure", "Future Promise", "Lazy Evaluation", "Streams",

        # 61-80: Collections & Data Structures
        "List Operations", "Vector Collection", "Set Collection", "Map Collection", "Seq Collection",
        "Array Buffer", "List Buffer", "Queue Collection", "Stack Collection", "Tree Set",
        "Tree Map", "Mutable Collections", "Immutable Collections", "Parallel Collections", "Iterator",
        "Collection Hierarchy", "Traversable", "Iterable", "Seq Indexed", "LinearSeq",

        # 81-100: Advanced
        "Implicits", "Implicit Conversions", "Implicit Parameters", "Type Classes", "Akka Actors",
        "Akka Streams", "Play Framework", "Slick Database", "Cats Library", "Scalaz",
        "ScalaTest", "ScalaCheck", "Macros", "Reflection", "Annotations",
        "XML Processing", "JSON Parsing", "HTTP Client", "Concurrency", "Futures Async"
    ]

    for i in range(1, 101):
        program_name = programs[i - 1]
        program_dir = os.path.join(BASE_DIR, f"{i:03d}_Program")
        os.makedirs(program_dir, exist_ok=True)

        content = f"""object Program{i:03d} {{
  /**
   * {program_name}
   * Program {i:03d}
   */

  def main(args: Array[String]): Unit = {{
    println("=== {program_name} ===")
    println("This is a Scala program demonstrating {program_name.lower()}.")

    // Implement the program logic here...
  }}
}}
"""

        with open(os.path.join(program_dir, "Main.scala"), "w") as f:
            f.write(content)

        build_content = f"""name := "program-{i:03d}"
version := "1.0"
scalaVersion := "3.3.0"
"""
        with open(os.path.join(program_dir, "build.sbt"), "w") as f:
            f.write(build_content)

    print(f"✓ Created Scala programs 1-100 (JVM Functional)")

def main():
    print("Creating and extending programs...")
    print("=" * 60)

    extend_ruby_programs()
    extend_cpp_programs()
    create_c_programs()
    create_scala_programs()

    print("=" * 60)
    print("✓ All programs created successfully!")

if __name__ == "__main__":
    main()
