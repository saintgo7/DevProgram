package main

import (
    "fmt"
    "os"
)

func main() {
    fmt.Println("=== Command Line Arguments ===")

    if len(os.Args) < 2 {
        fmt.Println("Usage: program <arg1> <arg2> ...")
        return
    }

    fmt.Printf("Program name: %s\n", os.Args[0])
    fmt.Printf("Arguments: %d\n", len(os.Args)-1)

    for i, arg := range os.Args[1:] {
        fmt.Printf("  Arg %d: %s\n", i+1, arg)
    }
}
