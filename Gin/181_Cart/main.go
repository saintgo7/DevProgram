package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Cart struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var carts = []{name}{}

func getAllCarts(c *gin.Context) {
    c.JSON(http.StatusOK, carts)
}

func getCartByID(c *gin.Context) {
    id := c.Param("id")
    // Find Cart by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Cart"})
}

func createCart(c *gin.Context) {
    var newCart Cart
    if err := c.BindJSON(&newCart); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    carts = append(carts, newCart)
    c.JSON(http.StatusCreated, newCart)
}

func updateCart(c *gin.Context) {
    id := c.Param("id")
    var updatedCart Cart
    if err := c.BindJSON(&updatedCart); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCart)
}

func deleteCart(c *gin.Context) {
    id := c.Param("id")
    // Delete Cart
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/cart", getAllCarts)
        api.GET("/cart/:id", getCartByID)
        api.POST("/cart", createCart)
        api.PUT("/cart/:id", updateCart)
        api.DELETE("/cart/:id", deleteCart)
    }

    r.Run(":8080")
}
