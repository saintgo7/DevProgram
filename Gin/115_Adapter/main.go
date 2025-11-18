package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Adapter struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var adapters = []{name}{}

func getAllAdapters(c *gin.Context) {
    c.JSON(http.StatusOK, adapters)
}

func getAdapterByID(c *gin.Context) {
    id := c.Param("id")
    // Find Adapter by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Adapter"})
}

func createAdapter(c *gin.Context) {
    var newAdapter Adapter
    if err := c.BindJSON(&newAdapter); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    adapters = append(adapters, newAdapter)
    c.JSON(http.StatusCreated, newAdapter)
}

func updateAdapter(c *gin.Context) {
    id := c.Param("id")
    var updatedAdapter Adapter
    if err := c.BindJSON(&updatedAdapter); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAdapter)
}

func deleteAdapter(c *gin.Context) {
    id := c.Param("id")
    // Delete Adapter
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/adapter", getAllAdapters)
        api.GET("/adapter/:id", getAdapterByID)
        api.POST("/adapter", createAdapter)
        api.PUT("/adapter/:id", updateAdapter)
        api.DELETE("/adapter/:id", deleteAdapter)
    }

    r.Run(":8080")
}
