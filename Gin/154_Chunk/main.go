package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Chunk struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var chunks = []{name}{}

func getAllChunks(c *gin.Context) {
    c.JSON(http.StatusOK, chunks)
}

func getChunkByID(c *gin.Context) {
    id := c.Param("id")
    // Find Chunk by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Chunk"})
}

func createChunk(c *gin.Context) {
    var newChunk Chunk
    if err := c.BindJSON(&newChunk); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    chunks = append(chunks, newChunk)
    c.JSON(http.StatusCreated, newChunk)
}

func updateChunk(c *gin.Context) {
    id := c.Param("id")
    var updatedChunk Chunk
    if err := c.BindJSON(&updatedChunk); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedChunk)
}

func deleteChunk(c *gin.Context) {
    id := c.Param("id")
    // Delete Chunk
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/chunk", getAllChunks)
        api.GET("/chunk/:id", getChunkByID)
        api.POST("/chunk", createChunk)
        api.PUT("/chunk/:id", updateChunk)
        api.DELETE("/chunk/:id", deleteChunk)
    }

    r.Run(":8080")
}
