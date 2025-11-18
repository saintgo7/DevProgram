package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Tax struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var taxs = []{name}{}

func getAllTaxs(c *gin.Context) {
    c.JSON(http.StatusOK, taxs)
}

func getTaxByID(c *gin.Context) {
    id := c.Param("id")
    // Find Tax by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Tax"})
}

func createTax(c *gin.Context) {
    var newTax Tax
    if err := c.BindJSON(&newTax); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    taxs = append(taxs, newTax)
    c.JSON(http.StatusCreated, newTax)
}

func updateTax(c *gin.Context) {
    id := c.Param("id")
    var updatedTax Tax
    if err := c.BindJSON(&updatedTax); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedTax)
}

func deleteTax(c *gin.Context) {
    id := c.Param("id")
    // Delete Tax
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/tax", getAllTaxs)
        api.GET("/tax/:id", getTaxByID)
        api.POST("/tax", createTax)
        api.PUT("/tax/:id", updateTax)
        api.DELETE("/tax/:id", deleteTax)
    }

    r.Run(":8080")
}
