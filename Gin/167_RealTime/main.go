package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type RealTime struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var realtimes = []{name}{}

func getAllRealTimes(c *gin.Context) {
    c.JSON(http.StatusOK, realtimes)
}

func getRealTimeByID(c *gin.Context) {
    id := c.Param("id")
    // Find RealTime by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "RealTime"})
}

func createRealTime(c *gin.Context) {
    var newRealTime RealTime
    if err := c.BindJSON(&newRealTime); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    realtimes = append(realtimes, newRealTime)
    c.JSON(http.StatusCreated, newRealTime)
}

func updateRealTime(c *gin.Context) {
    id := c.Param("id")
    var updatedRealTime RealTime
    if err := c.BindJSON(&updatedRealTime); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedRealTime)
}

func deleteRealTime(c *gin.Context) {
    id := c.Param("id")
    // Delete RealTime
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/realtime", getAllRealTimes)
        api.GET("/realtime/:id", getRealTimeByID)
        api.POST("/realtime", createRealTime)
        api.PUT("/realtime/:id", updateRealTime)
        api.DELETE("/realtime/:id", deleteRealTime)
    }

    r.Run(":8080")
}
