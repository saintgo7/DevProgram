package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Event struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var events = []{name}{}

func getAllEvents(c *gin.Context) {
    c.JSON(http.StatusOK, events)
}

func getEventByID(c *gin.Context) {
    id := c.Param("id")
    // Find Event by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Event"})
}

func createEvent(c *gin.Context) {
    var newEvent Event
    if err := c.BindJSON(&newEvent); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    events = append(events, newEvent)
    c.JSON(http.StatusCreated, newEvent)
}

func updateEvent(c *gin.Context) {
    id := c.Param("id")
    var updatedEvent Event
    if err := c.BindJSON(&updatedEvent); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedEvent)
}

func deleteEvent(c *gin.Context) {
    id := c.Param("id")
    // Delete Event
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/event", getAllEvents)
        api.GET("/event/:id", getEventByID)
        api.POST("/event", createEvent)
        api.PUT("/event/:id", updateEvent)
        api.DELETE("/event/:id", deleteEvent)
    }

    r.Run(":8080")
}
