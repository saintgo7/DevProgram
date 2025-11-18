package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Shipping struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var shippings = []{name}{}

func getAllShippings(c *gin.Context) {
    c.JSON(http.StatusOK, shippings)
}

func getShippingByID(c *gin.Context) {
    id := c.Param("id")
    // Find Shipping by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Shipping"})
}

func createShipping(c *gin.Context) {
    var newShipping Shipping
    if err := c.BindJSON(&newShipping); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    shippings = append(shippings, newShipping)
    c.JSON(http.StatusCreated, newShipping)
}

func updateShipping(c *gin.Context) {
    id := c.Param("id")
    var updatedShipping Shipping
    if err := c.BindJSON(&updatedShipping); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedShipping)
}

func deleteShipping(c *gin.Context) {
    id := c.Param("id")
    // Delete Shipping
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/shipping", getAllShippings)
        api.GET("/shipping/:id", getShippingByID)
        api.POST("/shipping", createShipping)
        api.PUT("/shipping/:id", updateShipping)
        api.DELETE("/shipping/:id", deleteShipping)
    }

    r.Run(":8080")
}
