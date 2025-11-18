package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Video struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var videos = []{name}{}

func getAllVideos(c *gin.Context) {
    c.JSON(http.StatusOK, videos)
}

func getVideoByID(c *gin.Context) {
    id := c.Param("id")
    // Find Video by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Video"})
}

func createVideo(c *gin.Context) {
    var newVideo Video
    if err := c.BindJSON(&newVideo); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    videos = append(videos, newVideo)
    c.JSON(http.StatusCreated, newVideo)
}

func updateVideo(c *gin.Context) {
    id := c.Param("id")
    var updatedVideo Video
    if err := c.BindJSON(&updatedVideo); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedVideo)
}

func deleteVideo(c *gin.Context) {
    id := c.Param("id")
    // Delete Video
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/video", getAllVideos)
        api.GET("/video/:id", getVideoByID)
        api.POST("/video", createVideo)
        api.PUT("/video/:id", updateVideo)
        api.DELETE("/video/:id", deleteVideo)
    }

    r.Run(":8080")
}
