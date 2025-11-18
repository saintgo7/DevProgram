package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Dashboard struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var dashboards = []{name}{}

func getAllDashboards(c *gin.Context) {
    c.JSON(http.StatusOK, dashboards)
}

func getDashboardByID(c *gin.Context) {
    id := c.Param("id")
    // Find Dashboard by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Dashboard"})
}

func createDashboard(c *gin.Context) {
    var newDashboard Dashboard
    if err := c.BindJSON(&newDashboard); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    dashboards = append(dashboards, newDashboard)
    c.JSON(http.StatusCreated, newDashboard)
}

func updateDashboard(c *gin.Context) {
    id := c.Param("id")
    var updatedDashboard Dashboard
    if err := c.BindJSON(&updatedDashboard); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedDashboard)
}

func deleteDashboard(c *gin.Context) {
    id := c.Param("id")
    // Delete Dashboard
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/dashboard", getAllDashboards)
        api.GET("/dashboard/:id", getDashboardByID)
        api.POST("/dashboard", createDashboard)
        api.PUT("/dashboard/:id", updateDashboard)
        api.DELETE("/dashboard/:id", deleteDashboard)
    }

    r.Run(":8080")
}
