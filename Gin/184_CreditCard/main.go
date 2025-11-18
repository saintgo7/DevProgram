package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type CreditCard struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var creditcards = []{name}{}

func getAllCreditCards(c *gin.Context) {
    c.JSON(http.StatusOK, creditcards)
}

func getCreditCardByID(c *gin.Context) {
    id := c.Param("id")
    // Find CreditCard by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "CreditCard"})
}

func createCreditCard(c *gin.Context) {
    var newCreditCard CreditCard
    if err := c.BindJSON(&newCreditCard); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    creditcards = append(creditcards, newCreditCard)
    c.JSON(http.StatusCreated, newCreditCard)
}

func updateCreditCard(c *gin.Context) {
    id := c.Param("id")
    var updatedCreditCard CreditCard
    if err := c.BindJSON(&updatedCreditCard); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCreditCard)
}

func deleteCreditCard(c *gin.Context) {
    id := c.Param("id")
    // Delete CreditCard
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/creditcard", getAllCreditCards)
        api.GET("/creditcard/:id", getCreditCardByID)
        api.POST("/creditcard", createCreditCard)
        api.PUT("/creditcard/:id", updateCreditCard)
        api.DELETE("/creditcard/:id", deleteCreditCard)
    }

    r.Run(":8080")
}
