package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Filter struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var filters = []{name}{}

func getAllFilters(c *gin.Context) {
    c.JSON(http.StatusOK, filters)
}

func getFilterByID(c *gin.Context) {
    id := c.Param("id")
    // Find Filter by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Filter"})
}

func createFilter(c *gin.Context) {
    var newFilter Filter
    if err := c.BindJSON(&newFilter); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    filters = append(filters, newFilter)
    c.JSON(http.StatusCreated, newFilter)
}

func updateFilter(c *gin.Context) {
    id := c.Param("id")
    var updatedFilter Filter
    if err := c.BindJSON(&updatedFilter); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedFilter)
}

func deleteFilter(c *gin.Context) {
    id := c.Param("id")
    // Delete Filter
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/filter", getAllFilters)
        api.GET("/filter/:id", getFilterByID)
        api.POST("/filter", createFilter)
        api.PUT("/filter/:id", updateFilter)
        api.DELETE("/filter/:id", deleteFilter)
    }

    r.Run(":8080")
}
