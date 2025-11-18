package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Calendar struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var calendars = []{name}{}

func getAllCalendars(c *gin.Context) {
    c.JSON(http.StatusOK, calendars)
}

func getCalendarByID(c *gin.Context) {
    id := c.Param("id")
    // Find Calendar by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Calendar"})
}

func createCalendar(c *gin.Context) {
    var newCalendar Calendar
    if err := c.BindJSON(&newCalendar); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    calendars = append(calendars, newCalendar)
    c.JSON(http.StatusCreated, newCalendar)
}

func updateCalendar(c *gin.Context) {
    id := c.Param("id")
    var updatedCalendar Calendar
    if err := c.BindJSON(&updatedCalendar); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCalendar)
}

func deleteCalendar(c *gin.Context) {
    id := c.Param("id")
    // Delete Calendar
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/calendar", getAllCalendars)
        api.GET("/calendar/:id", getCalendarByID)
        api.POST("/calendar", createCalendar)
        api.PUT("/calendar/:id", updateCalendar)
        api.DELETE("/calendar/:id", deleteCalendar)
    }

    r.Run(":8080")
}
