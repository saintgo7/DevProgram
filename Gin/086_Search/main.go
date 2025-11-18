package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Search struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var searchs = []{name}{}

func getAllSearchs(c *gin.Context) {
    c.JSON(http.StatusOK, searchs)
}

func getSearchByID(c *gin.Context) {
    id := c.Param("id")
    // Find Search by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Search"})
}

func createSearch(c *gin.Context) {
    var newSearch Search
    if err := c.BindJSON(&newSearch); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    searchs = append(searchs, newSearch)
    c.JSON(http.StatusCreated, newSearch)
}

func updateSearch(c *gin.Context) {
    id := c.Param("id")
    var updatedSearch Search
    if err := c.BindJSON(&updatedSearch); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSearch)
}

func deleteSearch(c *gin.Context) {
    id := c.Param("id")
    // Delete Search
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/search", getAllSearchs)
        api.GET("/search/:id", getSearchByID)
        api.POST("/search", createSearch)
        api.PUT("/search/:id", updateSearch)
        api.DELETE("/search/:id", deleteSearch)
    }

    r.Run(":8080")
}
