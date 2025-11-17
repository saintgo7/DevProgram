fn main() {
    println!("=== Rust Program 015 ===");
    println!("Basic Rust utility");

    let mut input = String::new();
    println!("Enter input:");

    std::io::stdin().read_line(&mut input).unwrap();
    println!("You entered: {}", input.trim());
}
