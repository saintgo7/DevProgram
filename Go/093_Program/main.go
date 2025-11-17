package main

import (
    "fmt"
    "runtime"
)

func main() {
    fmt.Println("=== Go Program 093 - Advanced ===")

    fmt.Printf("Go version: %s\n", runtime.Version())
    fmt.Printf("OS: %s\n", runtime.GOOS)
    fmt.Printf("Architecture: %s\n", runtime.GOARCH)
    fmt.Printf("CPUs: %d\n", runtime.NumCPU())
    fmt.Printf("Goroutines: %d\n", runtime.NumGoroutine())
}
