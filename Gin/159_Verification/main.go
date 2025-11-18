package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Verification struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var verifications = []{name}{}

func getAllVerifications(c *gin.Context) {
    c.JSON(http.StatusOK, verifications)
}

func getVerificationByID(c *gin.Context) {
    id := c.Param("id")
    // Find Verification by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Verification"})
}

func createVerification(c *gin.Context) {
    var newVerification Verification
    if err := c.BindJSON(&newVerification); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    verifications = append(verifications, newVerification)
    c.JSON(http.StatusCreated, newVerification)
}

func updateVerification(c *gin.Context) {
    id := c.Param("id")
    var updatedVerification Verification
    if err := c.BindJSON(&updatedVerification); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedVerification)
}

func deleteVerification(c *gin.Context) {
    id := c.Param("id")
    // Delete Verification
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/verification", getAllVerifications)
        api.GET("/verification/:id", getVerificationByID)
        api.POST("/verification", createVerification)
        api.PUT("/verification/:id", updateVerification)
        api.DELETE("/verification/:id", deleteVerification)
    }

    r.Run(":8080")
}
