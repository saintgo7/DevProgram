package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Table struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var tables = []{name}{}

func getAllTables(c *gin.Context) {
    c.JSON(http.StatusOK, tables)
}

func getTableByID(c *gin.Context) {
    id := c.Param("id")
    // Find Table by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Table"})
}

func createTable(c *gin.Context) {
    var newTable Table
    if err := c.BindJSON(&newTable); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    tables = append(tables, newTable)
    c.JSON(http.StatusCreated, newTable)
}

func updateTable(c *gin.Context) {
    id := c.Param("id")
    var updatedTable Table
    if err := c.BindJSON(&updatedTable); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedTable)
}

func deleteTable(c *gin.Context) {
    id := c.Param("id")
    // Delete Table
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/table", getAllTables)
        api.GET("/table/:id", getTableByID)
        api.POST("/table", createTable)
        api.PUT("/table/:id", updateTable)
        api.DELETE("/table/:id", deleteTable)
    }

    r.Run(":8080")
}
