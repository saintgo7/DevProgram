package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Signing struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var signings = []{name}{}

func getAllSignings(c *gin.Context) {
    c.JSON(http.StatusOK, signings)
}

func getSigningByID(c *gin.Context) {
    id := c.Param("id")
    // Find Signing by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Signing"})
}

func createSigning(c *gin.Context) {
    var newSigning Signing
    if err := c.BindJSON(&newSigning); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    signings = append(signings, newSigning)
    c.JSON(http.StatusCreated, newSigning)
}

func updateSigning(c *gin.Context) {
    id := c.Param("id")
    var updatedSigning Signing
    if err := c.BindJSON(&updatedSigning); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSigning)
}

func deleteSigning(c *gin.Context) {
    id := c.Param("id")
    // Delete Signing
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/signing", getAllSignings)
        api.GET("/signing/:id", getSigningByID)
        api.POST("/signing", createSigning)
        api.PUT("/signing/:id", updateSigning)
        api.DELETE("/signing/:id", deleteSigning)
    }

    r.Run(":8080")
}
