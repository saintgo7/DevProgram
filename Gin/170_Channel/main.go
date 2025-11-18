package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Channel struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var channels = []{name}{}

func getAllChannels(c *gin.Context) {
    c.JSON(http.StatusOK, channels)
}

func getChannelByID(c *gin.Context) {
    id := c.Param("id")
    // Find Channel by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Channel"})
}

func createChannel(c *gin.Context) {
    var newChannel Channel
    if err := c.BindJSON(&newChannel); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    channels = append(channels, newChannel)
    c.JSON(http.StatusCreated, newChannel)
}

func updateChannel(c *gin.Context) {
    id := c.Param("id")
    var updatedChannel Channel
    if err := c.BindJSON(&updatedChannel); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedChannel)
}

func deleteChannel(c *gin.Context) {
    id := c.Param("id")
    // Delete Channel
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/channel", getAllChannels)
        api.GET("/channel/:id", getChannelByID)
        api.POST("/channel", createChannel)
        api.PUT("/channel/:id", updateChannel)
        api.DELETE("/channel/:id", deleteChannel)
    }

    r.Run(":8080")
}
