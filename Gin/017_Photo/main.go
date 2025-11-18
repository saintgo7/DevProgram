package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Photo struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var photos = []{name}{}

func getAllPhotos(c *gin.Context) {
    c.JSON(http.StatusOK, photos)
}

func getPhotoByID(c *gin.Context) {
    id := c.Param("id")
    // Find Photo by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Photo"})
}

func createPhoto(c *gin.Context) {
    var newPhoto Photo
    if err := c.BindJSON(&newPhoto); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    photos = append(photos, newPhoto)
    c.JSON(http.StatusCreated, newPhoto)
}

func updatePhoto(c *gin.Context) {
    id := c.Param("id")
    var updatedPhoto Photo
    if err := c.BindJSON(&updatedPhoto); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPhoto)
}

func deletePhoto(c *gin.Context) {
    id := c.Param("id")
    // Delete Photo
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/photo", getAllPhotos)
        api.GET("/photo/:id", getPhotoByID)
        api.POST("/photo", createPhoto)
        api.PUT("/photo/:id", updatePhoto)
        api.DELETE("/photo/:id", deletePhoto)
    }

    r.Run(":8080")
}
