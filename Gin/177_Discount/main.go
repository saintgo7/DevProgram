package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Discount struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var discounts = []{name}{}

func getAllDiscounts(c *gin.Context) {
    c.JSON(http.StatusOK, discounts)
}

func getDiscountByID(c *gin.Context) {
    id := c.Param("id")
    // Find Discount by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Discount"})
}

func createDiscount(c *gin.Context) {
    var newDiscount Discount
    if err := c.BindJSON(&newDiscount); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    discounts = append(discounts, newDiscount)
    c.JSON(http.StatusCreated, newDiscount)
}

func updateDiscount(c *gin.Context) {
    id := c.Param("id")
    var updatedDiscount Discount
    if err := c.BindJSON(&updatedDiscount); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedDiscount)
}

func deleteDiscount(c *gin.Context) {
    id := c.Param("id")
    // Delete Discount
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/discount", getAllDiscounts)
        api.GET("/discount/:id", getDiscountByID)
        api.POST("/discount", createDiscount)
        api.PUT("/discount/:id", updateDiscount)
        api.DELETE("/discount/:id", deleteDiscount)
    }

    r.Run(":8080")
}
