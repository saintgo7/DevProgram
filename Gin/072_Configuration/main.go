package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Configuration struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var configurations = []{name}{}

func getAllConfigurations(c *gin.Context) {
    c.JSON(http.StatusOK, configurations)
}

func getConfigurationByID(c *gin.Context) {
    id := c.Param("id")
    // Find Configuration by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Configuration"})
}

func createConfiguration(c *gin.Context) {
    var newConfiguration Configuration
    if err := c.BindJSON(&newConfiguration); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    configurations = append(configurations, newConfiguration)
    c.JSON(http.StatusCreated, newConfiguration)
}

func updateConfiguration(c *gin.Context) {
    id := c.Param("id")
    var updatedConfiguration Configuration
    if err := c.BindJSON(&updatedConfiguration); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedConfiguration)
}

func deleteConfiguration(c *gin.Context) {
    id := c.Param("id")
    // Delete Configuration
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/configuration", getAllConfigurations)
        api.GET("/configuration/:id", getConfigurationByID)
        api.POST("/configuration", createConfiguration)
        api.PUT("/configuration/:id", updateConfiguration)
        api.DELETE("/configuration/:id", deleteConfiguration)
    }

    r.Run(":8080")
}
