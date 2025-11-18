package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Queue struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var queues = []{name}{}

func getAllQueues(c *gin.Context) {
    c.JSON(http.StatusOK, queues)
}

func getQueueByID(c *gin.Context) {
    id := c.Param("id")
    // Find Queue by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Queue"})
}

func createQueue(c *gin.Context) {
    var newQueue Queue
    if err := c.BindJSON(&newQueue); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    queues = append(queues, newQueue)
    c.JSON(http.StatusCreated, newQueue)
}

func updateQueue(c *gin.Context) {
    id := c.Param("id")
    var updatedQueue Queue
    if err := c.BindJSON(&updatedQueue); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedQueue)
}

func deleteQueue(c *gin.Context) {
    id := c.Param("id")
    // Delete Queue
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/queue", getAllQueues)
        api.GET("/queue/:id", getQueueByID)
        api.POST("/queue", createQueue)
        api.PUT("/queue/:id", updateQueue)
        api.DELETE("/queue/:id", deleteQueue)
    }

    r.Run(":8080")
}
