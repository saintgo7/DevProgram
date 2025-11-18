package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Account struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var accounts = []{name}{}

func getAllAccounts(c *gin.Context) {
    c.JSON(http.StatusOK, accounts)
}

func getAccountByID(c *gin.Context) {
    id := c.Param("id")
    // Find Account by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Account"})
}

func createAccount(c *gin.Context) {
    var newAccount Account
    if err := c.BindJSON(&newAccount); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    accounts = append(accounts, newAccount)
    c.JSON(http.StatusCreated, newAccount)
}

func updateAccount(c *gin.Context) {
    id := c.Param("id")
    var updatedAccount Account
    if err := c.BindJSON(&updatedAccount); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAccount)
}

func deleteAccount(c *gin.Context) {
    id := c.Param("id")
    // Delete Account
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/account", getAllAccounts)
        api.GET("/account/:id", getAccountByID)
        api.POST("/account", createAccount)
        api.PUT("/account/:id", updateAccount)
        api.DELETE("/account/:id", deleteAccount)
    }

    r.Run(":8080")
}
