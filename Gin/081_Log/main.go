package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Log struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var logs = []{name}{}

func getAllLogs(c *gin.Context) {
    c.JSON(http.StatusOK, logs)
}

func getLogByID(c *gin.Context) {
    id := c.Param("id")
    // Find Log by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Log"})
}

func createLog(c *gin.Context) {
    var newLog Log
    if err := c.BindJSON(&newLog); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    logs = append(logs, newLog)
    c.JSON(http.StatusCreated, newLog)
}

func updateLog(c *gin.Context) {
    id := c.Param("id")
    var updatedLog Log
    if err := c.BindJSON(&updatedLog); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedLog)
}

func deleteLog(c *gin.Context) {
    id := c.Param("id")
    // Delete Log
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/log", getAllLogs)
        api.GET("/log/:id", getLogByID)
        api.POST("/log", createLog)
        api.PUT("/log/:id", updateLog)
        api.DELETE("/log/:id", deleteLog)
    }

    r.Run(":8080")
}
