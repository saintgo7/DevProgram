package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Template struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var templates = []{name}{}

func getAllTemplates(c *gin.Context) {
    c.JSON(http.StatusOK, templates)
}

func getTemplateByID(c *gin.Context) {
    id := c.Param("id")
    // Find Template by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Template"})
}

func createTemplate(c *gin.Context) {
    var newTemplate Template
    if err := c.BindJSON(&newTemplate); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    templates = append(templates, newTemplate)
    c.JSON(http.StatusCreated, newTemplate)
}

func updateTemplate(c *gin.Context) {
    id := c.Param("id")
    var updatedTemplate Template
    if err := c.BindJSON(&updatedTemplate); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedTemplate)
}

func deleteTemplate(c *gin.Context) {
    id := c.Param("id")
    // Delete Template
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/template", getAllTemplates)
        api.GET("/template/:id", getTemplateByID)
        api.POST("/template", createTemplate)
        api.PUT("/template/:id", updateTemplate)
        api.DELETE("/template/:id", deleteTemplate)
    }

    r.Run(":8080")
}
