package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Metric struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var metrics = []{name}{}

func getAllMetrics(c *gin.Context) {
    c.JSON(http.StatusOK, metrics)
}

func getMetricByID(c *gin.Context) {
    id := c.Param("id")
    // Find Metric by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Metric"})
}

func createMetric(c *gin.Context) {
    var newMetric Metric
    if err := c.BindJSON(&newMetric); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    metrics = append(metrics, newMetric)
    c.JSON(http.StatusCreated, newMetric)
}

func updateMetric(c *gin.Context) {
    id := c.Param("id")
    var updatedMetric Metric
    if err := c.BindJSON(&updatedMetric); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedMetric)
}

func deleteMetric(c *gin.Context) {
    id := c.Param("id")
    // Delete Metric
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/metric", getAllMetrics)
        api.GET("/metric/:id", getMetricByID)
        api.POST("/metric", createMetric)
        api.PUT("/metric/:id", updateMetric)
        api.DELETE("/metric/:id", deleteMetric)
    }

    r.Run(":8080")
}
