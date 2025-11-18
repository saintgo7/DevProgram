package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Chart struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var charts = []{name}{}

func getAllCharts(c *gin.Context) {
    c.JSON(http.StatusOK, charts)
}

func getChartByID(c *gin.Context) {
    id := c.Param("id")
    // Find Chart by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Chart"})
}

func createChart(c *gin.Context) {
    var newChart Chart
    if err := c.BindJSON(&newChart); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    charts = append(charts, newChart)
    c.JSON(http.StatusCreated, newChart)
}

func updateChart(c *gin.Context) {
    id := c.Param("id")
    var updatedChart Chart
    if err := c.BindJSON(&updatedChart); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedChart)
}

func deleteChart(c *gin.Context) {
    id := c.Param("id")
    // Delete Chart
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/chart", getAllCharts)
        api.GET("/chart/:id", getChartByID)
        api.POST("/chart", createChart)
        api.PUT("/chart/:id", updateChart)
        api.DELETE("/chart/:id", deleteChart)
    }

    r.Run(":8080")
}
