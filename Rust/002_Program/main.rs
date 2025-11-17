use std::env;

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
