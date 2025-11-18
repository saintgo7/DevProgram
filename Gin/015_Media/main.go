package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Media struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var medias = []{name}{}

func getAllMedias(c *gin.Context) {
    c.JSON(http.StatusOK, medias)
}

func getMediaByID(c *gin.Context) {
    id := c.Param("id")
    // Find Media by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Media"})
}

func createMedia(c *gin.Context) {
    var newMedia Media
    if err := c.BindJSON(&newMedia); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    medias = append(medias, newMedia)
    c.JSON(http.StatusCreated, newMedia)
}

func updateMedia(c *gin.Context) {
    id := c.Param("id")
    var updatedMedia Media
    if err := c.BindJSON(&updatedMedia); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedMedia)
}

func deleteMedia(c *gin.Context) {
    id := c.Param("id")
    // Delete Media
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/media", getAllMedias)
        api.GET("/media/:id", getMediaByID)
        api.POST("/media", createMedia)
        api.PUT("/media/:id", updateMedia)
        api.DELETE("/media/:id", deleteMedia)
    }

    r.Run(":8080")
}
