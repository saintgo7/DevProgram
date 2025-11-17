package main

import (
    "fmt"
    "net/http"
    "io"
)

func main() {
    fmt.Println("=== Go Program 053 - Network ===")

    url := "https://example.com"
    fmt.Printf("Fetching: %s\n", url)

    resp, err := http.Get(url)
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }
    defer resp.Body.Close()

    body, _ := io.ReadAll(resp.Body)
    fmt.Printf("Status: %s\n", resp.Status)
    fmt.Printf("Content length: %d bytes\n", len(body))
}
