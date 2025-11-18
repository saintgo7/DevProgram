package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Analytics struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var analyticss = []{name}{}

func getAllAnalyticss(c *gin.Context) {
    c.JSON(http.StatusOK, analyticss)
}

func getAnalyticsByID(c *gin.Context) {
    id := c.Param("id")
    // Find Analytics by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Analytics"})
}

func createAnalytics(c *gin.Context) {
    var newAnalytics Analytics
    if err := c.BindJSON(&newAnalytics); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    analyticss = append(analyticss, newAnalytics)
    c.JSON(http.StatusCreated, newAnalytics)
}

func updateAnalytics(c *gin.Context) {
    id := c.Param("id")
    var updatedAnalytics Analytics
    if err := c.BindJSON(&updatedAnalytics); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAnalytics)
}

func deleteAnalytics(c *gin.Context) {
    id := c.Param("id")
    // Delete Analytics
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/analytics", getAllAnalyticss)
        api.GET("/analytics/:id", getAnalyticsByID)
        api.POST("/analytics", createAnalytics)
        api.PUT("/analytics/:id", updateAnalytics)
        api.DELETE("/analytics/:id", deleteAnalytics)
    }

    r.Run(":8080")
}
