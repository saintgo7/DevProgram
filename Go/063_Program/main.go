package main

import (
    "encoding/json"
    "fmt"
)

type Data struct {
    ID    int    `json:"id"`
    Name  string `json:"name"`
    Value int    `json:"value"`
}

func main() {
    fmt.Println("=== Go Program 063 - Data Processing ===")

    data := []Data{
        {1, "Item 1", 100},
        {2, "Item 2", 200},
        {3, "Item 3", 150},
    }

    jsonData, err := json.MarshalIndent(data, "", "  ")
    if err != nil {
        fmt.Printf("Error: %v\n", err)
        return
    }

    fmt.Println("JSON Output:")
    fmt.Println(string(jsonData))
}
