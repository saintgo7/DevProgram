package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Sync struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var syncs = []{name}{}

func getAllSyncs(c *gin.Context) {
    c.JSON(http.StatusOK, syncs)
}

func getSyncByID(c *gin.Context) {
    id := c.Param("id")
    // Find Sync by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Sync"})
}

func createSync(c *gin.Context) {
    var newSync Sync
    if err := c.BindJSON(&newSync); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    syncs = append(syncs, newSync)
    c.JSON(http.StatusCreated, newSync)
}

func updateSync(c *gin.Context) {
    id := c.Param("id")
    var updatedSync Sync
    if err := c.BindJSON(&updatedSync); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSync)
}

func deleteSync(c *gin.Context) {
    id := c.Param("id")
    // Delete Sync
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/sync", getAllSyncs)
        api.GET("/sync/:id", getSyncByID)
        api.POST("/sync", createSync)
        api.PUT("/sync/:id", updateSync)
        api.DELETE("/sync/:id", deleteSync)
    }

    r.Run(":8080")
}
