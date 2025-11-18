package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Wishlist struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var wishlists = []{name}{}

func getAllWishlists(c *gin.Context) {
    c.JSON(http.StatusOK, wishlists)
}

func getWishlistByID(c *gin.Context) {
    id := c.Param("id")
    // Find Wishlist by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Wishlist"})
}

func createWishlist(c *gin.Context) {
    var newWishlist Wishlist
    if err := c.BindJSON(&newWishlist); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    wishlists = append(wishlists, newWishlist)
    c.JSON(http.StatusCreated, newWishlist)
}

func updateWishlist(c *gin.Context) {
    id := c.Param("id")
    var updatedWishlist Wishlist
    if err := c.BindJSON(&updatedWishlist); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedWishlist)
}

func deleteWishlist(c *gin.Context) {
    id := c.Param("id")
    // Delete Wishlist
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/wishlist", getAllWishlists)
        api.GET("/wishlist/:id", getWishlistByID)
        api.POST("/wishlist", createWishlist)
        api.PUT("/wishlist/:id", updateWishlist)
        api.DELETE("/wishlist/:id", deleteWishlist)
    }

    r.Run(":8080")
}
