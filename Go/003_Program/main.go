package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    fmt.Println("=== File Reader ===")

    var filename string
    fmt.Print("Enter filename: ")
    fmt.Scanln(&filename)

    file, err := os.Open(filename)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    lineNum := 1

    fmt.Println("\nFile contents:")
    fmt.Println("---")

    for scanner.Scan() {
        fmt.Printf("%3d | %s\n", lineNum, scanner.Text())
        lineNum++
    }

    if err := scanner.Err(); err != nil {
        fmt.Printf("Error reading file: %v\n", err)
    }

    fmt.Printf("\nTotal lines: %d\n", lineNum-1)
}
