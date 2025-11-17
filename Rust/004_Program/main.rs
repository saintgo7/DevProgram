use std::fs::File;
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
