package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Album struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var albums = []{name}{}

func getAllAlbums(c *gin.Context) {
    c.JSON(http.StatusOK, albums)
}

func getAlbumByID(c *gin.Context) {
    id := c.Param("id")
    // Find Album by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Album"})
}

func createAlbum(c *gin.Context) {
    var newAlbum Album
    if err := c.BindJSON(&newAlbum); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    albums = append(albums, newAlbum)
    c.JSON(http.StatusCreated, newAlbum)
}

func updateAlbum(c *gin.Context) {
    id := c.Param("id")
    var updatedAlbum Album
    if err := c.BindJSON(&updatedAlbum); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAlbum)
}

func deleteAlbum(c *gin.Context) {
    id := c.Param("id")
    // Delete Album
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/album", getAllAlbums)
        api.GET("/album/:id", getAlbumByID)
        api.POST("/album", createAlbum)
        api.PUT("/album/:id", updateAlbum)
        api.DELETE("/album/:id", deleteAlbum)
    }

    r.Run(":8080")
}
