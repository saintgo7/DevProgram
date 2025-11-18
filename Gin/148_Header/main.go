package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Header struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var headers = []{name}{}

func getAllHeaders(c *gin.Context) {
    c.JSON(http.StatusOK, headers)
}

func getHeaderByID(c *gin.Context) {
    id := c.Param("id")
    // Find Header by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Header"})
}

func createHeader(c *gin.Context) {
    var newHeader Header
    if err := c.BindJSON(&newHeader); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    headers = append(headers, newHeader)
    c.JSON(http.StatusCreated, newHeader)
}

func updateHeader(c *gin.Context) {
    id := c.Param("id")
    var updatedHeader Header
    if err := c.BindJSON(&updatedHeader); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedHeader)
}

func deleteHeader(c *gin.Context) {
    id := c.Param("id")
    // Delete Header
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/header", getAllHeaders)
        api.GET("/header/:id", getHeaderByID)
        api.POST("/header", createHeader)
        api.PUT("/header/:id", updateHeader)
        api.DELETE("/header/:id", deleteHeader)
    }

    r.Run(":8080")
}
