package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Issue struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var issues = []{name}{}

func getAllIssues(c *gin.Context) {
    c.JSON(http.StatusOK, issues)
}

func getIssueByID(c *gin.Context) {
    id := c.Param("id")
    // Find Issue by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Issue"})
}

func createIssue(c *gin.Context) {
    var newIssue Issue
    if err := c.BindJSON(&newIssue); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    issues = append(issues, newIssue)
    c.JSON(http.StatusCreated, newIssue)
}

func updateIssue(c *gin.Context) {
    id := c.Param("id")
    var updatedIssue Issue
    if err := c.BindJSON(&updatedIssue); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedIssue)
}

func deleteIssue(c *gin.Context) {
    id := c.Param("id")
    // Delete Issue
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/issue", getAllIssues)
        api.GET("/issue/:id", getIssueByID)
        api.POST("/issue", createIssue)
        api.PUT("/issue/:id", updateIssue)
        api.DELETE("/issue/:id", deleteIssue)
    }

    r.Run(":8080")
}
