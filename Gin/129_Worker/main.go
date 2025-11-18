package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Worker struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var workers = []{name}{}

func getAllWorkers(c *gin.Context) {
    c.JSON(http.StatusOK, workers)
}

func getWorkerByID(c *gin.Context) {
    id := c.Param("id")
    // Find Worker by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Worker"})
}

func createWorker(c *gin.Context) {
    var newWorker Worker
    if err := c.BindJSON(&newWorker); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    workers = append(workers, newWorker)
    c.JSON(http.StatusCreated, newWorker)
}

func updateWorker(c *gin.Context) {
    id := c.Param("id")
    var updatedWorker Worker
    if err := c.BindJSON(&updatedWorker); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedWorker)
}

func deleteWorker(c *gin.Context) {
    id := c.Param("id")
    // Delete Worker
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/worker", getAllWorkers)
        api.GET("/worker/:id", getWorkerByID)
        api.POST("/worker", createWorker)
        api.PUT("/worker/:id", updateWorker)
        api.DELETE("/worker/:id", deleteWorker)
    }

    r.Run(":8080")
}
