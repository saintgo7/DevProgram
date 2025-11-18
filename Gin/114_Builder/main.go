package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Builder struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var builders = []{name}{}

func getAllBuilders(c *gin.Context) {
    c.JSON(http.StatusOK, builders)
}

func getBuilderByID(c *gin.Context) {
    id := c.Param("id")
    // Find Builder by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Builder"})
}

func createBuilder(c *gin.Context) {
    var newBuilder Builder
    if err := c.BindJSON(&newBuilder); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    builders = append(builders, newBuilder)
    c.JSON(http.StatusCreated, newBuilder)
}

func updateBuilder(c *gin.Context) {
    id := c.Param("id")
    var updatedBuilder Builder
    if err := c.BindJSON(&updatedBuilder); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedBuilder)
}

func deleteBuilder(c *gin.Context) {
    id := c.Param("id")
    // Delete Builder
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/builder", getAllBuilders)
        api.GET("/builder/:id", getBuilderByID)
        api.POST("/builder", createBuilder)
        api.PUT("/builder/:id", updateBuilder)
        api.DELETE("/builder/:id", deleteBuilder)
    }

    r.Run(":8080")
}
