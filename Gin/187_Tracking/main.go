package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Tracking struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var trackings = []{name}{}

func getAllTrackings(c *gin.Context) {
    c.JSON(http.StatusOK, trackings)
}

func getTrackingByID(c *gin.Context) {
    id := c.Param("id")
    // Find Tracking by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Tracking"})
}

func createTracking(c *gin.Context) {
    var newTracking Tracking
    if err := c.BindJSON(&newTracking); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    trackings = append(trackings, newTracking)
    c.JSON(http.StatusCreated, newTracking)
}

func updateTracking(c *gin.Context) {
    id := c.Param("id")
    var updatedTracking Tracking
    if err := c.BindJSON(&updatedTracking); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedTracking)
}

func deleteTracking(c *gin.Context) {
    id := c.Param("id")
    // Delete Tracking
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/tracking", getAllTrackings)
        api.GET("/tracking/:id", getTrackingByID)
        api.POST("/tracking", createTracking)
        api.PUT("/tracking/:id", updateTracking)
        api.DELETE("/tracking/:id", deleteTracking)
    }

    r.Run(":8080")
}
