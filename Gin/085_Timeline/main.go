package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Timeline struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var timelines = []{name}{}

func getAllTimelines(c *gin.Context) {
    c.JSON(http.StatusOK, timelines)
}

func getTimelineByID(c *gin.Context) {
    id := c.Param("id")
    // Find Timeline by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Timeline"})
}

func createTimeline(c *gin.Context) {
    var newTimeline Timeline
    if err := c.BindJSON(&newTimeline); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    timelines = append(timelines, newTimeline)
    c.JSON(http.StatusCreated, newTimeline)
}

func updateTimeline(c *gin.Context) {
    id := c.Param("id")
    var updatedTimeline Timeline
    if err := c.BindJSON(&updatedTimeline); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedTimeline)
}

func deleteTimeline(c *gin.Context) {
    id := c.Param("id")
    // Delete Timeline
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/timeline", getAllTimelines)
        api.GET("/timeline/:id", getTimelineByID)
        api.POST("/timeline", createTimeline)
        api.PUT("/timeline/:id", updateTimeline)
        api.DELETE("/timeline/:id", deleteTimeline)
    }

    r.Run(":8080")
}
