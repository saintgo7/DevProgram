package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Pagination struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var paginations = []{name}{}

func getAllPaginations(c *gin.Context) {
    c.JSON(http.StatusOK, paginations)
}

func getPaginationByID(c *gin.Context) {
    id := c.Param("id")
    // Find Pagination by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Pagination"})
}

func createPagination(c *gin.Context) {
    var newPagination Pagination
    if err := c.BindJSON(&newPagination); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    paginations = append(paginations, newPagination)
    c.JSON(http.StatusCreated, newPagination)
}

func updatePagination(c *gin.Context) {
    id := c.Param("id")
    var updatedPagination Pagination
    if err := c.BindJSON(&updatedPagination); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPagination)
}

func deletePagination(c *gin.Context) {
    id := c.Param("id")
    // Delete Pagination
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/pagination", getAllPaginations)
        api.GET("/pagination/:id", getPaginationByID)
        api.POST("/pagination", createPagination)
        api.PUT("/pagination/:id", updatePagination)
        api.DELETE("/pagination/:id", deletePagination)
    }

    r.Run(":8080")
}
