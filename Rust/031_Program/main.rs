use std::thread;
use std::time::Duration;

fn main() {
    println!("=== Rust Program 031 - Ownership ===");

    let data = vec![1, 2, 3, 4, 5];
    println!("Data: {:?}", data);

    // Demonstrate ownership
    let data_clone = data.clone();
    println!("Clone: {:?}", data_clone);

    // Borrowing
    let sum: i32 = data.iter().sum();
    println!("Sum: {}", sum);
}
