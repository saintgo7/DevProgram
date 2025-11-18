package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Scheduler struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var schedulers = []{name}{}

func getAllSchedulers(c *gin.Context) {
    c.JSON(http.StatusOK, schedulers)
}

func getSchedulerByID(c *gin.Context) {
    id := c.Param("id")
    // Find Scheduler by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Scheduler"})
}

func createScheduler(c *gin.Context) {
    var newScheduler Scheduler
    if err := c.BindJSON(&newScheduler); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    schedulers = append(schedulers, newScheduler)
    c.JSON(http.StatusCreated, newScheduler)
}

func updateScheduler(c *gin.Context) {
    id := c.Param("id")
    var updatedScheduler Scheduler
    if err := c.BindJSON(&updatedScheduler); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedScheduler)
}

func deleteScheduler(c *gin.Context) {
    id := c.Param("id")
    // Delete Scheduler
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/scheduler", getAllSchedulers)
        api.GET("/scheduler/:id", getSchedulerByID)
        api.POST("/scheduler", createScheduler)
        api.PUT("/scheduler/:id", updateScheduler)
        api.DELETE("/scheduler/:id", deleteScheduler)
    }

    r.Run(":8080")
}
