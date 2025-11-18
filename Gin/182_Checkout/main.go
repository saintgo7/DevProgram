package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Checkout struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var checkouts = []{name}{}

func getAllCheckouts(c *gin.Context) {
    c.JSON(http.StatusOK, checkouts)
}

func getCheckoutByID(c *gin.Context) {
    id := c.Param("id")
    // Find Checkout by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Checkout"})
}

func createCheckout(c *gin.Context) {
    var newCheckout Checkout
    if err := c.BindJSON(&newCheckout); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    checkouts = append(checkouts, newCheckout)
    c.JSON(http.StatusCreated, newCheckout)
}

func updateCheckout(c *gin.Context) {
    id := c.Param("id")
    var updatedCheckout Checkout
    if err := c.BindJSON(&updatedCheckout); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCheckout)
}

func deleteCheckout(c *gin.Context) {
    id := c.Param("id")
    // Delete Checkout
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/checkout", getAllCheckouts)
        api.GET("/checkout/:id", getCheckoutByID)
        api.POST("/checkout", createCheckout)
        api.PUT("/checkout/:id", updateCheckout)
        api.DELETE("/checkout/:id", deleteCheckout)
    }

    r.Run(":8080")
}
