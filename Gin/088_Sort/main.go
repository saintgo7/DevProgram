package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Sort struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var sorts = []{name}{}

func getAllSorts(c *gin.Context) {
    c.JSON(http.StatusOK, sorts)
}

func getSortByID(c *gin.Context) {
    id := c.Param("id")
    // Find Sort by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Sort"})
}

func createSort(c *gin.Context) {
    var newSort Sort
    if err := c.BindJSON(&newSort); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    sorts = append(sorts, newSort)
    c.JSON(http.StatusCreated, newSort)
}

func updateSort(c *gin.Context) {
    id := c.Param("id")
    var updatedSort Sort
    if err := c.BindJSON(&updatedSort); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSort)
}

func deleteSort(c *gin.Context) {
    id := c.Param("id")
    // Delete Sort
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/sort", getAllSorts)
        api.GET("/sort/:id", getSortByID)
        api.POST("/sort", createSort)
        api.PUT("/sort/:id", updateSort)
        api.DELETE("/sort/:id", deleteSort)
    }

    r.Run(":8080")
}
