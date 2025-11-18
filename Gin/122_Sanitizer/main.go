package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Sanitizer struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var sanitizers = []{name}{}

func getAllSanitizers(c *gin.Context) {
    c.JSON(http.StatusOK, sanitizers)
}

func getSanitizerByID(c *gin.Context) {
    id := c.Param("id")
    // Find Sanitizer by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Sanitizer"})
}

func createSanitizer(c *gin.Context) {
    var newSanitizer Sanitizer
    if err := c.BindJSON(&newSanitizer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    sanitizers = append(sanitizers, newSanitizer)
    c.JSON(http.StatusCreated, newSanitizer)
}

func updateSanitizer(c *gin.Context) {
    id := c.Param("id")
    var updatedSanitizer Sanitizer
    if err := c.BindJSON(&updatedSanitizer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSanitizer)
}

func deleteSanitizer(c *gin.Context) {
    id := c.Param("id")
    // Delete Sanitizer
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/sanitizer", getAllSanitizers)
        api.GET("/sanitizer/:id", getSanitizerByID)
        api.POST("/sanitizer", createSanitizer)
        api.PUT("/sanitizer/:id", updateSanitizer)
        api.DELETE("/sanitizer/:id", deleteSanitizer)
    }

    r.Run(":8080")
}
