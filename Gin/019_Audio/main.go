package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Audio struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var audios = []{name}{}

func getAllAudios(c *gin.Context) {
    c.JSON(http.StatusOK, audios)
}

func getAudioByID(c *gin.Context) {
    id := c.Param("id")
    // Find Audio by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Audio"})
}

func createAudio(c *gin.Context) {
    var newAudio Audio
    if err := c.BindJSON(&newAudio); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    audios = append(audios, newAudio)
    c.JSON(http.StatusCreated, newAudio)
}

func updateAudio(c *gin.Context) {
    id := c.Param("id")
    var updatedAudio Audio
    if err := c.BindJSON(&updatedAudio); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAudio)
}

func deleteAudio(c *gin.Context) {
    id := c.Param("id")
    // Delete Audio
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/audio", getAllAudios)
        api.GET("/audio/:id", getAudioByID)
        api.POST("/audio", createAudio)
        api.PUT("/audio/:id", updateAudio)
        api.DELETE("/audio/:id", deleteAudio)
    }

    r.Run(":8080")
}
