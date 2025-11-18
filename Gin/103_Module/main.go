package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Module struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var modules = []{name}{}

func getAllModules(c *gin.Context) {
    c.JSON(http.StatusOK, modules)
}

func getModuleByID(c *gin.Context) {
    id := c.Param("id")
    // Find Module by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Module"})
}

func createModule(c *gin.Context) {
    var newModule Module
    if err := c.BindJSON(&newModule); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    modules = append(modules, newModule)
    c.JSON(http.StatusCreated, newModule)
}

func updateModule(c *gin.Context) {
    id := c.Param("id")
    var updatedModule Module
    if err := c.BindJSON(&updatedModule); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedModule)
}

func deleteModule(c *gin.Context) {
    id := c.Param("id")
    // Delete Module
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/module", getAllModules)
        api.GET("/module/:id", getModuleByID)
        api.POST("/module", createModule)
        api.PUT("/module/:id", updateModule)
        api.DELETE("/module/:id", deleteModule)
    }

    r.Run(":8080")
}
