package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Favorite struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var favorites = []{name}{}

func getAllFavorites(c *gin.Context) {
    c.JSON(http.StatusOK, favorites)
}

func getFavoriteByID(c *gin.Context) {
    id := c.Param("id")
    // Find Favorite by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Favorite"})
}

func createFavorite(c *gin.Context) {
    var newFavorite Favorite
    if err := c.BindJSON(&newFavorite); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    favorites = append(favorites, newFavorite)
    c.JSON(http.StatusCreated, newFavorite)
}

func updateFavorite(c *gin.Context) {
    id := c.Param("id")
    var updatedFavorite Favorite
    if err := c.BindJSON(&updatedFavorite); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedFavorite)
}

func deleteFavorite(c *gin.Context) {
    id := c.Param("id")
    // Delete Favorite
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/favorite", getAllFavorites)
        api.GET("/favorite/:id", getFavoriteByID)
        api.POST("/favorite", createFavorite)
        api.PUT("/favorite/:id", updateFavorite)
        api.DELETE("/favorite/:id", deleteFavorite)
    }

    r.Run(":8080")
}
