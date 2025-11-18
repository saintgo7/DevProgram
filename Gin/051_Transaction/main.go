package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Transaction struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var transactions = []{name}{}

func getAllTransactions(c *gin.Context) {
    c.JSON(http.StatusOK, transactions)
}

func getTransactionByID(c *gin.Context) {
    id := c.Param("id")
    // Find Transaction by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Transaction"})
}

func createTransaction(c *gin.Context) {
    var newTransaction Transaction
    if err := c.BindJSON(&newTransaction); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    transactions = append(transactions, newTransaction)
    c.JSON(http.StatusCreated, newTransaction)
}

func updateTransaction(c *gin.Context) {
    id := c.Param("id")
    var updatedTransaction Transaction
    if err := c.BindJSON(&updatedTransaction); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedTransaction)
}

func deleteTransaction(c *gin.Context) {
    id := c.Param("id")
    // Delete Transaction
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/transaction", getAllTransactions)
        api.GET("/transaction/:id", getTransactionByID)
        api.POST("/transaction", createTransaction)
        api.PUT("/transaction/:id", updateTransaction)
        api.DELETE("/transaction/:id", deleteTransaction)
    }

    r.Run(":8080")
}
