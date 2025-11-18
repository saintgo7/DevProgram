package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Buffer struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var buffers = []{name}{}

func getAllBuffers(c *gin.Context) {
    c.JSON(http.StatusOK, buffers)
}

func getBufferByID(c *gin.Context) {
    id := c.Param("id")
    // Find Buffer by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Buffer"})
}

func createBuffer(c *gin.Context) {
    var newBuffer Buffer
    if err := c.BindJSON(&newBuffer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    buffers = append(buffers, newBuffer)
    c.JSON(http.StatusCreated, newBuffer)
}

func updateBuffer(c *gin.Context) {
    id := c.Param("id")
    var updatedBuffer Buffer
    if err := c.BindJSON(&updatedBuffer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedBuffer)
}

func deleteBuffer(c *gin.Context) {
    id := c.Param("id")
    // Delete Buffer
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/buffer", getAllBuffers)
        api.GET("/buffer/:id", getBufferByID)
        api.POST("/buffer", createBuffer)
        api.PUT("/buffer/:id", updateBuffer)
        api.DELETE("/buffer/:id", deleteBuffer)
    }

    r.Run(":8080")
}
