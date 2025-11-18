package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Payment struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var payments = []{name}{}

func getAllPayments(c *gin.Context) {
    c.JSON(http.StatusOK, payments)
}

func getPaymentByID(c *gin.Context) {
    id := c.Param("id")
    // Find Payment by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Payment"})
}

func createPayment(c *gin.Context) {
    var newPayment Payment
    if err := c.BindJSON(&newPayment); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    payments = append(payments, newPayment)
    c.JSON(http.StatusCreated, newPayment)
}

func updatePayment(c *gin.Context) {
    id := c.Param("id")
    var updatedPayment Payment
    if err := c.BindJSON(&updatedPayment); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPayment)
}

func deletePayment(c *gin.Context) {
    id := c.Param("id")
    // Delete Payment
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/payment", getAllPayments)
        api.GET("/payment/:id", getPaymentByID)
        api.POST("/payment", createPayment)
        api.PUT("/payment/:id", updatePayment)
        api.DELETE("/payment/:id", deletePayment)
    }

    r.Run(":8080")
}
