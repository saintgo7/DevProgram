package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Cache struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var caches = []{name}{}

func getAllCaches(c *gin.Context) {
    c.JSON(http.StatusOK, caches)
}

func getCacheByID(c *gin.Context) {
    id := c.Param("id")
    // Find Cache by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Cache"})
}

func createCache(c *gin.Context) {
    var newCache Cache
    if err := c.BindJSON(&newCache); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    caches = append(caches, newCache)
    c.JSON(http.StatusCreated, newCache)
}

func updateCache(c *gin.Context) {
    id := c.Param("id")
    var updatedCache Cache
    if err := c.BindJSON(&updatedCache); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCache)
}

func deleteCache(c *gin.Context) {
    id := c.Param("id")
    // Delete Cache
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/cache", getAllCaches)
        api.GET("/cache/:id", getCacheByID)
        api.POST("/cache", createCache)
        api.PUT("/cache/:id", updateCache)
        api.DELETE("/cache/:id", deleteCache)
    }

    r.Run(":8080")
}
