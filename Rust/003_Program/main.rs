use std::fs::File;
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
            println!("\nFile contents:");
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
