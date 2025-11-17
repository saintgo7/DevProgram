package main

import "fmt"

func main() {
    fmt.Println("=== Go Program 013 ===")
    fmt.Println("CLI utility program")

    var input string
    fmt.Print("Enter command: ")
    fmt.Scanln(&input)

    fmt.Printf("Processing: %s\n", input)
}
