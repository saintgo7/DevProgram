package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Backup struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var backups = []{name}{}

func getAllBackups(c *gin.Context) {
    c.JSON(http.StatusOK, backups)
}

func getBackupByID(c *gin.Context) {
    id := c.Param("id")
    // Find Backup by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Backup"})
}

func createBackup(c *gin.Context) {
    var newBackup Backup
    if err := c.BindJSON(&newBackup); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    backups = append(backups, newBackup)
    c.JSON(http.StatusCreated, newBackup)
}

func updateBackup(c *gin.Context) {
    id := c.Param("id")
    var updatedBackup Backup
    if err := c.BindJSON(&updatedBackup); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedBackup)
}

func deleteBackup(c *gin.Context) {
    id := c.Param("id")
    // Delete Backup
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/backup", getAllBackups)
        api.GET("/backup/:id", getBackupByID)
        api.POST("/backup", createBackup)
        api.PUT("/backup/:id", updateBackup)
        api.DELETE("/backup/:id", deleteBackup)
    }

    r.Run(":8080")
}
