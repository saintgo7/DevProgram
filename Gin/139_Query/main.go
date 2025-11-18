package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Query struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var querys = []{name}{}

func getAllQuerys(c *gin.Context) {
    c.JSON(http.StatusOK, querys)
}

func getQueryByID(c *gin.Context) {
    id := c.Param("id")
    // Find Query by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Query"})
}

func createQuery(c *gin.Context) {
    var newQuery Query
    if err := c.BindJSON(&newQuery); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    querys = append(querys, newQuery)
    c.JSON(http.StatusCreated, newQuery)
}

func updateQuery(c *gin.Context) {
    id := c.Param("id")
    var updatedQuery Query
    if err := c.BindJSON(&updatedQuery); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedQuery)
}

func deleteQuery(c *gin.Context) {
    id := c.Param("id")
    // Delete Query
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/query", getAllQuerys)
        api.GET("/query/:id", getQueryByID)
        api.POST("/query", createQuery)
        api.PUT("/query/:id", updateQuery)
        api.DELETE("/query/:id", deleteQuery)
    }

    r.Run(":8080")
}
