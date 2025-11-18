package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Project struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var projects = []{name}{}

func getAllProjects(c *gin.Context) {
    c.JSON(http.StatusOK, projects)
}

func getProjectByID(c *gin.Context) {
    id := c.Param("id")
    // Find Project by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Project"})
}

func createProject(c *gin.Context) {
    var newProject Project
    if err := c.BindJSON(&newProject); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    projects = append(projects, newProject)
    c.JSON(http.StatusCreated, newProject)
}

func updateProject(c *gin.Context) {
    id := c.Param("id")
    var updatedProject Project
    if err := c.BindJSON(&updatedProject); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedProject)
}

func deleteProject(c *gin.Context) {
    id := c.Param("id")
    // Delete Project
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/project", getAllProjects)
        api.GET("/project/:id", getProjectByID)
        api.POST("/project", createProject)
        api.PUT("/project/:id", updateProject)
        api.DELETE("/project/:id", deleteProject)
    }

    r.Run(":8080")
}
