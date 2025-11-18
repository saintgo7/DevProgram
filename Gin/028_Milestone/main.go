package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Milestone struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var milestones = []{name}{}

func getAllMilestones(c *gin.Context) {
    c.JSON(http.StatusOK, milestones)
}

func getMilestoneByID(c *gin.Context) {
    id := c.Param("id")
    // Find Milestone by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Milestone"})
}

func createMilestone(c *gin.Context) {
    var newMilestone Milestone
    if err := c.BindJSON(&newMilestone); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    milestones = append(milestones, newMilestone)
    c.JSON(http.StatusCreated, newMilestone)
}

func updateMilestone(c *gin.Context) {
    id := c.Param("id")
    var updatedMilestone Milestone
    if err := c.BindJSON(&updatedMilestone); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedMilestone)
}

func deleteMilestone(c *gin.Context) {
    id := c.Param("id")
    // Delete Milestone
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/milestone", getAllMilestones)
        api.GET("/milestone/:id", getMilestoneByID)
        api.POST("/milestone", createMilestone)
        api.PUT("/milestone/:id", updateMilestone)
        api.DELETE("/milestone/:id", deleteMilestone)
    }

    r.Run(":8080")
}
