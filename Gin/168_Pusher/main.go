package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Pusher struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var pushers = []{name}{}

func getAllPushers(c *gin.Context) {
    c.JSON(http.StatusOK, pushers)
}

func getPusherByID(c *gin.Context) {
    id := c.Param("id")
    // Find Pusher by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Pusher"})
}

func createPusher(c *gin.Context) {
    var newPusher Pusher
    if err := c.BindJSON(&newPusher); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    pushers = append(pushers, newPusher)
    c.JSON(http.StatusCreated, newPusher)
}

func updatePusher(c *gin.Context) {
    id := c.Param("id")
    var updatedPusher Pusher
    if err := c.BindJSON(&updatedPusher); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPusher)
}

func deletePusher(c *gin.Context) {
    id := c.Param("id")
    // Delete Pusher
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/pusher", getAllPushers)
        api.GET("/pusher/:id", getPusherByID)
        api.POST("/pusher", createPusher)
        api.PUT("/pusher/:id", updatePusher)
        api.DELETE("/pusher/:id", deletePusher)
    }

    r.Run(":8080")
}
