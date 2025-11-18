package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Statement struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var statements = []{name}{}

func getAllStatements(c *gin.Context) {
    c.JSON(http.StatusOK, statements)
}

func getStatementByID(c *gin.Context) {
    id := c.Param("id")
    // Find Statement by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Statement"})
}

func createStatement(c *gin.Context) {
    var newStatement Statement
    if err := c.BindJSON(&newStatement); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    statements = append(statements, newStatement)
    c.JSON(http.StatusCreated, newStatement)
}

func updateStatement(c *gin.Context) {
    id := c.Param("id")
    var updatedStatement Statement
    if err := c.BindJSON(&updatedStatement); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedStatement)
}

func deleteStatement(c *gin.Context) {
    id := c.Param("id")
    // Delete Statement
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/statement", getAllStatements)
        api.GET("/statement/:id", getStatementByID)
        api.POST("/statement", createStatement)
        api.PUT("/statement/:id", updateStatement)
        api.DELETE("/statement/:id", deleteStatement)
    }

    r.Run(":8080")
}
