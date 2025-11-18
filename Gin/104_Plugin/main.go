package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Plugin struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var plugins = []{name}{}

func getAllPlugins(c *gin.Context) {
    c.JSON(http.StatusOK, plugins)
}

func getPluginByID(c *gin.Context) {
    id := c.Param("id")
    // Find Plugin by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Plugin"})
}

func createPlugin(c *gin.Context) {
    var newPlugin Plugin
    if err := c.BindJSON(&newPlugin); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    plugins = append(plugins, newPlugin)
    c.JSON(http.StatusCreated, newPlugin)
}

func updatePlugin(c *gin.Context) {
    id := c.Param("id")
    var updatedPlugin Plugin
    if err := c.BindJSON(&updatedPlugin); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPlugin)
}

func deletePlugin(c *gin.Context) {
    id := c.Param("id")
    // Delete Plugin
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/plugin", getAllPlugins)
        api.GET("/plugin/:id", getPluginByID)
        api.POST("/plugin", createPlugin)
        api.PUT("/plugin/:id", updatePlugin)
        api.DELETE("/plugin/:id", deletePlugin)
    }

    r.Run(":8080")
}
