package main

import (
    "fmt"
    "os"
    "path/filepath"
)

func main() {
    fmt.Println("=== Directory Lister ===")

    var dirPath string
    fmt.Print("Enter directory path: ")
    fmt.Scanln(&dirPath)

    entries, err := os.ReadDir(dirPath)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }

    fmt.Printf("\nContents of %s:\n", dirPath)
    fmt.Println("---")

    fileCount := 0
    dirCount := 0

    for _, entry := range entries {
        info, _ := entry.Info()
        typeStr := "FILE"
        if entry.IsDir() {
            typeStr = "DIR "
            dirCount++
        } else {
            fileCount++
        }

        fmt.Printf("[%s] %-30s %10d bytes\n",
            typeStr, entry.Name(), info.Size())
    }

    fmt.Printf("\nTotal: %d files, %d directories\n", fileCount, dirCount)
}
