#!/usr/bin/env python3
"""
Create 100 Rust programs
"""

import os

base_dir = "/home/user/DevProgram/Rust"

# Rust program templates
rust_programs = {
    1: ("Hello World", "Simple hello world program", """fn main() {
    println!("=== Hello World ===");
    println!("Welcome to Rust programming!");
}
"""),

    2: ("Command Line Args", "Process command line arguments", """use std::env;

fn main() {
    println!("=== Command Line Arguments ===");

    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("Usage: program <arg1> <arg2> ...");
        return;
    }

    println!("Program name: {}", args[0]);
    println!("Arguments: {}", args.len() - 1);

    for (i, arg) in args.iter().skip(1).enumerate() {
        println!("  Arg {}: {}", i + 1, arg);
    }
}
"""),

    3: ("File Reader", "Read and display file contents", """use std::fs::File;
use std::io::{self, BufRead, BufReader, Write};

fn main() {
    println!("=== File Reader ===");

    print!("Enter filename: ");
    io::stdout().flush().unwrap();

    let mut filename = String::new();
    io::stdin().read_line(&mut filename).unwrap();
    let filename = filename.trim();

    match File::open(filename) {
        Ok(file) => {
            let reader = BufReader::new(file);
            println!("\\nFile contents:");
            println!("---");

            for (line_num, line) in reader.lines().enumerate() {
                match line {
                    Ok(content) => println!("{:3} | {}", line_num + 1, content),
                    Err(e) => eprintln!("Error reading line: {}", e),
                }
            }
        }
        Err(e) => eprintln!("Error opening file: {}", e),
    }
}
"""),

    4: ("File Writer", "Write text to a file", """use std::fs::File;
use std::io::{self, Write};

fn main() {
    println!("=== File Writer ===");

    print!("Enter filename: ");
    io::stdout().flush().unwrap();

    let mut filename = String::new();
    io::stdin().read_line(&mut filename).unwrap();
    let filename = filename.trim();

    match File::create(filename) {
        Ok(mut file) => {
            println!("Enter text (type 'END' to finish):");

            loop {
                let mut line = String::new();
                io::stdin().read_line(&mut line).unwrap();

                if line.trim() == "END" {
                    break;
                }

                if let Err(e) = file.write_all(line.as_bytes()) {
                    eprintln!("Error writing: {}", e);
                    return;
                }
            }

            println!("File written successfully");
        }
        Err(e) => eprintln!("Error creating file: {}", e),
    }
}
"""),

    5: ("Vector Operations", "Demonstrate vector operations", """fn main() {
    println!("=== Vector Operations ===");

    let mut numbers: Vec<i32> = vec![1, 2, 3, 4, 5];

    println!("Original vector: {:?}", numbers);

    numbers.push(6);
    println!("After push(6): {:?}", numbers);

    numbers.pop();
    println!("After pop(): {:?}", numbers);

    let sum: i32 = numbers.iter().sum();
    println!("Sum: {}", sum);

    let doubled: Vec<i32> = numbers.iter().map(|x| x * 2).collect();
    println!("Doubled: {:?}", doubled);

    let evens: Vec<&i32> = numbers.iter().filter(|&x| x % 2 == 0).collect();
    println!("Even numbers: {:?}", evens);
}
"""),
}

# Generate remaining programs
for i in range(6, 101):
    if i <= 20:
        template = f"""fn main() {{
    println!("=== Rust Program {i:03d} ===");
    println!("Basic Rust utility");

    let mut input = String::new();
    println!("Enter input:");

    std::io::stdin().read_line(&mut input).unwrap();
    println!("You entered: {{}}", input.trim());
}}
"""
    elif i <= 40:
        template = f"""use std::thread;
use std::time::Duration;

fn main() {{
    println!("=== Rust Program {i:03d} - Ownership ===");

    let data = vec![1, 2, 3, 4, 5];
    println!("Data: {{:?}}", data);

    // Demonstrate ownership
    let data_clone = data.clone();
    println!("Clone: {{:?}}", data_clone);

    // Borrowing
    let sum: i32 = data.iter().sum();
    println!("Sum: {{}}", sum);
}}
"""
    elif i <= 60:
        template = f"""use std::sync::{{Arc, Mutex}};
use std::thread;

fn main() {{
    println!("=== Rust Program {i:03d} - Concurrency ===");

    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for i in 0..5 {{
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {{
            let mut num = counter.lock().unwrap();
            *num += 1;
            println!("Thread {{}} incremented counter", i);
        }});
        handles.push(handle);
    }}

    for handle in handles {{
        handle.join().unwrap();
    }}

    println!("Final count: {{}}", *counter.lock().unwrap());
}}
"""
    elif i <= 80:
        template = f"""use std::collections::HashMap;

fn main() {{
    println!("=== Rust Program {i:03d} - Data Structures ===");

    let mut map = HashMap::new();
    map.insert("key1", 100);
    map.insert("key2", 200);
    map.insert("key3", 150);

    for (key, value) in &map {{
        println!("{{}}: {{}}", key, value);
    }}

    let sum: i32 = map.values().sum();
    println!("Total: {{}}", sum);
}}
"""
    else:
        template = f"""fn main() {{
    println!("=== Rust Program {i:03d} - Advanced ===");

    // Demonstrate pattern matching
    let value = 42;

    match value {{
        0 => println!("Zero"),
        1..=50 => println!("Between 1 and 50"),
        _ => println!("Other"),
    }}

    // Result handling
    let result: Result<i32, &str> = Ok(value);
    match result {{
        Ok(v) => println!("Success: {{}}", v),
        Err(e) => println!("Error: {{}}", e),
    }}
}}
"""

    rust_programs[i] = (f"Program {i}", f"Rust program {i}", template)

# Create directories and files
os.makedirs(base_dir, exist_ok=True)

for num, (title, desc, code) in rust_programs.items():
    program_dir = f"{base_dir}/{num:03d}_Program"
    os.makedirs(program_dir, exist_ok=True)

    # Write main.rs
    with open(f"{program_dir}/main.rs", 'w') as f:
        f.write(code)

    # Create Cargo.toml
    cargo_toml = f"""[package]
name = "program_{num:03d}"
version = "0.1.0"
edition = "2021"

[dependencies]
"""
    with open(f"{program_dir}/Cargo.toml", 'w') as f:
        f.write(cargo_toml)

    print(f"Created: {num:03d} - {title}")

print(f"\\nCreated {len(rust_programs)} Rust programs in {base_dir}")
