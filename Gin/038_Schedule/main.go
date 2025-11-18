package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Schedule struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var schedules = []{name}{}

func getAllSchedules(c *gin.Context) {
    c.JSON(http.StatusOK, schedules)
}

func getScheduleByID(c *gin.Context) {
    id := c.Param("id")
    // Find Schedule by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Schedule"})
}

func createSchedule(c *gin.Context) {
    var newSchedule Schedule
    if err := c.BindJSON(&newSchedule); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    schedules = append(schedules, newSchedule)
    c.JSON(http.StatusCreated, newSchedule)
}

func updateSchedule(c *gin.Context) {
    id := c.Param("id")
    var updatedSchedule Schedule
    if err := c.BindJSON(&updatedSchedule); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSchedule)
}

func deleteSchedule(c *gin.Context) {
    id := c.Param("id")
    // Delete Schedule
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/schedule", getAllSchedules)
        api.GET("/schedule/:id", getScheduleByID)
        api.POST("/schedule", createSchedule)
        api.PUT("/schedule/:id", updateSchedule)
        api.DELETE("/schedule/:id", deleteSchedule)
    }

    r.Run(":8080")
}
