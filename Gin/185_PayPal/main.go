package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type PayPal struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var paypals = []{name}{}

func getAllPayPals(c *gin.Context) {
    c.JSON(http.StatusOK, paypals)
}

func getPayPalByID(c *gin.Context) {
    id := c.Param("id")
    // Find PayPal by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "PayPal"})
}

func createPayPal(c *gin.Context) {
    var newPayPal PayPal
    if err := c.BindJSON(&newPayPal); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    paypals = append(paypals, newPayPal)
    c.JSON(http.StatusCreated, newPayPal)
}

func updatePayPal(c *gin.Context) {
    id := c.Param("id")
    var updatedPayPal PayPal
    if err := c.BindJSON(&updatedPayPal); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPayPal)
}

func deletePayPal(c *gin.Context) {
    id := c.Param("id")
    // Delete PayPal
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/paypal", getAllPayPals)
        api.GET("/paypal/:id", getPayPalByID)
        api.POST("/paypal", createPayPal)
        api.PUT("/paypal/:id", updatePayPal)
        api.DELETE("/paypal/:id", deletePayPal)
    }

    r.Run(":8080")
}
