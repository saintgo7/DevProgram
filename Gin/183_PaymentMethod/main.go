package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type PaymentMethod struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var paymentmethods = []{name}{}

func getAllPaymentMethods(c *gin.Context) {
    c.JSON(http.StatusOK, paymentmethods)
}

func getPaymentMethodByID(c *gin.Context) {
    id := c.Param("id")
    // Find PaymentMethod by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "PaymentMethod"})
}

func createPaymentMethod(c *gin.Context) {
    var newPaymentMethod PaymentMethod
    if err := c.BindJSON(&newPaymentMethod); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    paymentmethods = append(paymentmethods, newPaymentMethod)
    c.JSON(http.StatusCreated, newPaymentMethod)
}

func updatePaymentMethod(c *gin.Context) {
    id := c.Param("id")
    var updatedPaymentMethod PaymentMethod
    if err := c.BindJSON(&updatedPaymentMethod); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPaymentMethod)
}

func deletePaymentMethod(c *gin.Context) {
    id := c.Param("id")
    // Delete PaymentMethod
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/paymentmethod", getAllPaymentMethods)
        api.GET("/paymentmethod/:id", getPaymentMethodByID)
        api.POST("/paymentmethod", createPaymentMethod)
        api.PUT("/paymentmethod/:id", updatePaymentMethod)
        api.DELETE("/paymentmethod/:id", deletePaymentMethod)
    }

    r.Run(":8080")
}
