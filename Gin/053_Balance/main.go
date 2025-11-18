package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Balance struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var balances = []{name}{}

func getAllBalances(c *gin.Context) {
    c.JSON(http.StatusOK, balances)
}

func getBalanceByID(c *gin.Context) {
    id := c.Param("id")
    // Find Balance by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Balance"})
}

func createBalance(c *gin.Context) {
    var newBalance Balance
    if err := c.BindJSON(&newBalance); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    balances = append(balances, newBalance)
    c.JSON(http.StatusCreated, newBalance)
}

func updateBalance(c *gin.Context) {
    id := c.Param("id")
    var updatedBalance Balance
    if err := c.BindJSON(&updatedBalance); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedBalance)
}

func deleteBalance(c *gin.Context) {
    id := c.Param("id")
    // Delete Balance
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/balance", getAllBalances)
        api.GET("/balance/:id", getBalanceByID)
        api.POST("/balance", createBalance)
        api.PUT("/balance/:id", updateBalance)
        api.DELETE("/balance/:id", deleteBalance)
    }

    r.Run(":8080")
}
