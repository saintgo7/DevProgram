package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Migration struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var migrations = []{name}{}

func getAllMigrations(c *gin.Context) {
    c.JSON(http.StatusOK, migrations)
}

func getMigrationByID(c *gin.Context) {
    id := c.Param("id")
    // Find Migration by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Migration"})
}

func createMigration(c *gin.Context) {
    var newMigration Migration
    if err := c.BindJSON(&newMigration); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    migrations = append(migrations, newMigration)
    c.JSON(http.StatusCreated, newMigration)
}

func updateMigration(c *gin.Context) {
    id := c.Param("id")
    var updatedMigration Migration
    if err := c.BindJSON(&updatedMigration); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedMigration)
}

func deleteMigration(c *gin.Context) {
    id := c.Param("id")
    // Delete Migration
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/migration", getAllMigrations)
        api.GET("/migration/:id", getMigrationByID)
        api.POST("/migration", createMigration)
        api.PUT("/migration/:id", updateMigration)
        api.DELETE("/migration/:id", deleteMigration)
    }

    r.Run(":8080")
}
