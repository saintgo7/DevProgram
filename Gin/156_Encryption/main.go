package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Encryption struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var encryptions = []{name}{}

func getAllEncryptions(c *gin.Context) {
    c.JSON(http.StatusOK, encryptions)
}

func getEncryptionByID(c *gin.Context) {
    id := c.Param("id")
    // Find Encryption by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Encryption"})
}

func createEncryption(c *gin.Context) {
    var newEncryption Encryption
    if err := c.BindJSON(&newEncryption); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    encryptions = append(encryptions, newEncryption)
    c.JSON(http.StatusCreated, newEncryption)
}

func updateEncryption(c *gin.Context) {
    id := c.Param("id")
    var updatedEncryption Encryption
    if err := c.BindJSON(&updatedEncryption); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedEncryption)
}

func deleteEncryption(c *gin.Context) {
    id := c.Param("id")
    // Delete Encryption
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/encryption", getAllEncryptions)
        api.GET("/encryption/:id", getEncryptionByID)
        api.POST("/encryption", createEncryption)
        api.PUT("/encryption/:id", updateEncryption)
        api.DELETE("/encryption/:id", deleteEncryption)
    }

    r.Run(":8080")
}
