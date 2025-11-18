package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Seeder struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var seeders = []{name}{}

func getAllSeeders(c *gin.Context) {
    c.JSON(http.StatusOK, seeders)
}

func getSeederByID(c *gin.Context) {
    id := c.Param("id")
    // Find Seeder by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Seeder"})
}

func createSeeder(c *gin.Context) {
    var newSeeder Seeder
    if err := c.BindJSON(&newSeeder); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    seeders = append(seeders, newSeeder)
    c.JSON(http.StatusCreated, newSeeder)
}

func updateSeeder(c *gin.Context) {
    id := c.Param("id")
    var updatedSeeder Seeder
    if err := c.BindJSON(&updatedSeeder); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSeeder)
}

func deleteSeeder(c *gin.Context) {
    id := c.Param("id")
    // Delete Seeder
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/seeder", getAllSeeders)
        api.GET("/seeder/:id", getSeederByID)
        api.POST("/seeder", createSeeder)
        api.PUT("/seeder/:id", updateSeeder)
        api.DELETE("/seeder/:id", deleteSeeder)
    }

    r.Run(":8080")
}
