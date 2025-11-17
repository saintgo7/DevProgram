fn main() {
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
