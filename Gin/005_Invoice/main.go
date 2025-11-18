package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Invoice struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var invoices = []{name}{}

func getAllInvoices(c *gin.Context) {
    c.JSON(http.StatusOK, invoices)
}

func getInvoiceByID(c *gin.Context) {
    id := c.Param("id")
    // Find Invoice by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Invoice"})
}

func createInvoice(c *gin.Context) {
    var newInvoice Invoice
    if err := c.BindJSON(&newInvoice); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    invoices = append(invoices, newInvoice)
    c.JSON(http.StatusCreated, newInvoice)
}

func updateInvoice(c *gin.Context) {
    id := c.Param("id")
    var updatedInvoice Invoice
    if err := c.BindJSON(&updatedInvoice); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedInvoice)
}

func deleteInvoice(c *gin.Context) {
    id := c.Param("id")
    // Delete Invoice
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/invoice", getAllInvoices)
        api.GET("/invoice/:id", getInvoiceByID)
        api.POST("/invoice", createInvoice)
        api.PUT("/invoice/:id", updateInvoice)
        api.DELETE("/invoice/:id", deleteInvoice)
    }

    r.Run(":8080")
}
