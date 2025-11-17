use std::collections::HashMap;

fn main() {
    println!("=== Rust Program 064 - Data Structures ===");

    let mut map = HashMap::new();
    map.insert("key1", 100);
    map.insert("key2", 200);
    map.insert("key3", 150);

    for (key, value) in &map {
        println!("{}: {}", key, value);
    }

    let sum: i32 = map.values().sum();
    println!("Total: {}", sum);
}
