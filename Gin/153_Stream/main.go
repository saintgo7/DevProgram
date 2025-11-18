package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Stream struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var streams = []{name}{}

func getAllStreams(c *gin.Context) {
    c.JSON(http.StatusOK, streams)
}

func getStreamByID(c *gin.Context) {
    id := c.Param("id")
    // Find Stream by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Stream"})
}

func createStream(c *gin.Context) {
    var newStream Stream
    if err := c.BindJSON(&newStream); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    streams = append(streams, newStream)
    c.JSON(http.StatusCreated, newStream)
}

func updateStream(c *gin.Context) {
    id := c.Param("id")
    var updatedStream Stream
    if err := c.BindJSON(&updatedStream); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedStream)
}

func deleteStream(c *gin.Context) {
    id := c.Param("id")
    // Delete Stream
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/stream", getAllStreams)
        api.GET("/stream/:id", getStreamByID)
        api.POST("/stream", createStream)
        api.PUT("/stream/:id", updateStream)
        api.DELETE("/stream/:id", deleteStream)
    }

    r.Run(":8080")
}
