fn main() {
    println!("=== Rust Program 098 - Advanced ===");

    // Demonstrate pattern matching
    let value = 42;

    match value {
        0 => println!("Zero"),
        1..=50 => println!("Between 1 and 50"),
        _ => println!("Other"),
    }

    // Result handling
    let result: Result<i32, &str> = Ok(value);
    match result {
        Ok(v) => println!("Success: {}", v),
        Err(e) => println!("Error: {}", e),
    }
}
