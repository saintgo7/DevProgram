package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Broadcast struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var broadcasts = []{name}{}

func getAllBroadcasts(c *gin.Context) {
    c.JSON(http.StatusOK, broadcasts)
}

func getBroadcastByID(c *gin.Context) {
    id := c.Param("id")
    // Find Broadcast by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Broadcast"})
}

func createBroadcast(c *gin.Context) {
    var newBroadcast Broadcast
    if err := c.BindJSON(&newBroadcast); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    broadcasts = append(broadcasts, newBroadcast)
    c.JSON(http.StatusCreated, newBroadcast)
}

func updateBroadcast(c *gin.Context) {
    id := c.Param("id")
    var updatedBroadcast Broadcast
    if err := c.BindJSON(&updatedBroadcast); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedBroadcast)
}

func deleteBroadcast(c *gin.Context) {
    id := c.Param("id")
    // Delete Broadcast
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/broadcast", getAllBroadcasts)
        api.GET("/broadcast/:id", getBroadcastByID)
        api.POST("/broadcast", createBroadcast)
        api.PUT("/broadcast/:id", updateBroadcast)
        api.DELETE("/broadcast/:id", deleteBroadcast)
    }

    r.Run(":8080")
}
