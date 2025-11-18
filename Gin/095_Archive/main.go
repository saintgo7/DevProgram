package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Archive struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var archives = []{name}{}

func getAllArchives(c *gin.Context) {
    c.JSON(http.StatusOK, archives)
}

func getArchiveByID(c *gin.Context) {
    id := c.Param("id")
    // Find Archive by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Archive"})
}

func createArchive(c *gin.Context) {
    var newArchive Archive
    if err := c.BindJSON(&newArchive); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    archives = append(archives, newArchive)
    c.JSON(http.StatusCreated, newArchive)
}

func updateArchive(c *gin.Context) {
    id := c.Param("id")
    var updatedArchive Archive
    if err := c.BindJSON(&updatedArchive); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedArchive)
}

func deleteArchive(c *gin.Context) {
    id := c.Param("id")
    // Delete Archive
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/archive", getAllArchives)
        api.GET("/archive/:id", getArchiveByID)
        api.POST("/archive", createArchive)
        api.PUT("/archive/:id", updateArchive)
        api.DELETE("/archive/:id", deleteArchive)
    }

    r.Run(":8080")
}
