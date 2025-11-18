package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Customer struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var customers = []{name}{}

func getAllCustomers(c *gin.Context) {
    c.JSON(http.StatusOK, customers)
}

func getCustomerByID(c *gin.Context) {
    id := c.Param("id")
    // Find Customer by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Customer"})
}

func createCustomer(c *gin.Context) {
    var newCustomer Customer
    if err := c.BindJSON(&newCustomer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    customers = append(customers, newCustomer)
    c.JSON(http.StatusCreated, newCustomer)
}

func updateCustomer(c *gin.Context) {
    id := c.Param("id")
    var updatedCustomer Customer
    if err := c.BindJSON(&updatedCustomer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCustomer)
}

func deleteCustomer(c *gin.Context) {
    id := c.Param("id")
    // Delete Customer
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/customer", getAllCustomers)
        api.GET("/customer/:id", getCustomerByID)
        api.POST("/customer", createCustomer)
        api.PUT("/customer/:id", updateCustomer)
        api.DELETE("/customer/:id", deleteCustomer)
    }

    r.Run(":8080")
}
