package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Sprint struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var sprints = []{name}{}

func getAllSprints(c *gin.Context) {
    c.JSON(http.StatusOK, sprints)
}

func getSprintByID(c *gin.Context) {
    id := c.Param("id")
    // Find Sprint by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Sprint"})
}

func createSprint(c *gin.Context) {
    var newSprint Sprint
    if err := c.BindJSON(&newSprint); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    sprints = append(sprints, newSprint)
    c.JSON(http.StatusCreated, newSprint)
}

func updateSprint(c *gin.Context) {
    id := c.Param("id")
    var updatedSprint Sprint
    if err := c.BindJSON(&updatedSprint); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSprint)
}

func deleteSprint(c *gin.Context) {
    id := c.Param("id")
    // Delete Sprint
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/sprint", getAllSprints)
        api.GET("/sprint/:id", getSprintByID)
        api.POST("/sprint", createSprint)
        api.PUT("/sprint/:id", updateSprint)
        api.DELETE("/sprint/:id", deleteSprint)
    }

    r.Run(":8080")
}
