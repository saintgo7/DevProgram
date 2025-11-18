package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Database struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var databases = []{name}{}

func getAllDatabases(c *gin.Context) {
    c.JSON(http.StatusOK, databases)
}

func getDatabaseByID(c *gin.Context) {
    id := c.Param("id")
    // Find Database by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Database"})
}

func createDatabase(c *gin.Context) {
    var newDatabase Database
    if err := c.BindJSON(&newDatabase); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    databases = append(databases, newDatabase)
    c.JSON(http.StatusCreated, newDatabase)
}

func updateDatabase(c *gin.Context) {
    id := c.Param("id")
    var updatedDatabase Database
    if err := c.BindJSON(&updatedDatabase); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedDatabase)
}

func deleteDatabase(c *gin.Context) {
    id := c.Param("id")
    // Delete Database
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/database", getAllDatabases)
        api.GET("/database/:id", getDatabaseByID)
        api.POST("/database", createDatabase)
        api.PUT("/database/:id", updateDatabase)
        api.DELETE("/database/:id", deleteDatabase)
    }

    r.Run(":8080")
}
