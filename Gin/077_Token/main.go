package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Token struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var tokens = []{name}{}

func getAllTokens(c *gin.Context) {
    c.JSON(http.StatusOK, tokens)
}

func getTokenByID(c *gin.Context) {
    id := c.Param("id")
    // Find Token by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Token"})
}

func createToken(c *gin.Context) {
    var newToken Token
    if err := c.BindJSON(&newToken); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    tokens = append(tokens, newToken)
    c.JSON(http.StatusCreated, newToken)
}

func updateToken(c *gin.Context) {
    id := c.Param("id")
    var updatedToken Token
    if err := c.BindJSON(&updatedToken); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedToken)
}

func deleteToken(c *gin.Context) {
    id := c.Param("id")
    // Delete Token
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/token", getAllTokens)
        api.GET("/token/:id", getTokenByID)
        api.POST("/token", createToken)
        api.PUT("/token/:id", updateToken)
        api.DELETE("/token/:id", deleteToken)
    }

    r.Run(":8080")
}
