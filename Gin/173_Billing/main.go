package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Billing struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var billings = []{name}{}

func getAllBillings(c *gin.Context) {
    c.JSON(http.StatusOK, billings)
}

func getBillingByID(c *gin.Context) {
    id := c.Param("id")
    // Find Billing by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Billing"})
}

func createBilling(c *gin.Context) {
    var newBilling Billing
    if err := c.BindJSON(&newBilling); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    billings = append(billings, newBilling)
    c.JSON(http.StatusCreated, newBilling)
}

func updateBilling(c *gin.Context) {
    id := c.Param("id")
    var updatedBilling Billing
    if err := c.BindJSON(&updatedBilling); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedBilling)
}

func deleteBilling(c *gin.Context) {
    id := c.Param("id")
    // Delete Billing
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/billing", getAllBillings)
        api.GET("/billing/:id", getBillingByID)
        api.POST("/billing", createBilling)
        api.PUT("/billing/:id", updateBilling)
        api.DELETE("/billing/:id", deleteBilling)
    }

    r.Run(":8080")
}
