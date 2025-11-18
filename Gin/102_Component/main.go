package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Component struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var components = []{name}{}

func getAllComponents(c *gin.Context) {
    c.JSON(http.StatusOK, components)
}

func getComponentByID(c *gin.Context) {
    id := c.Param("id")
    // Find Component by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Component"})
}

func createComponent(c *gin.Context) {
    var newComponent Component
    if err := c.BindJSON(&newComponent); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    components = append(components, newComponent)
    c.JSON(http.StatusCreated, newComponent)
}

func updateComponent(c *gin.Context) {
    id := c.Param("id")
    var updatedComponent Component
    if err := c.BindJSON(&updatedComponent); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedComponent)
}

func deleteComponent(c *gin.Context) {
    id := c.Param("id")
    // Delete Component
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/component", getAllComponents)
        api.GET("/component/:id", getComponentByID)
        api.POST("/component", createComponent)
        api.PUT("/component/:id", updateComponent)
        api.DELETE("/component/:id", deleteComponent)
    }

    r.Run(":8080")
}
