package main

import (
    "fmt"
    "os"
)

func main() {
    fmt.Println("=== File Writer ===")

    var filename string
    fmt.Print("Enter filename: ")
    fmt.Scanln(&filename)

    fmt.Println("Enter text (type 'END' on a new line to finish):")

    file, err := os.Create(filename)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    defer file.Close()

    var line string
    lineCount := 0

    for {
        fmt.Scanln(&line)
        if line == "END" {
            break
        }
        _, err := file.WriteString(line + "\n")
        if err != nil {
            fmt.Printf("Error writing: %v\n", err)
            return
        }
        lineCount++
    }

    fmt.Printf("\nWrote %d lines to %s\n", lineCount, filename)
}
