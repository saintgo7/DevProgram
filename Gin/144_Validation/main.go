package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Validation struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var validations = []{name}{}

func getAllValidations(c *gin.Context) {
    c.JSON(http.StatusOK, validations)
}

func getValidationByID(c *gin.Context) {
    id := c.Param("id")
    // Find Validation by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Validation"})
}

func createValidation(c *gin.Context) {
    var newValidation Validation
    if err := c.BindJSON(&newValidation); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    validations = append(validations, newValidation)
    c.JSON(http.StatusCreated, newValidation)
}

func updateValidation(c *gin.Context) {
    id := c.Param("id")
    var updatedValidation Validation
    if err := c.BindJSON(&updatedValidation); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedValidation)
}

func deleteValidation(c *gin.Context) {
    id := c.Param("id")
    // Delete Validation
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/validation", getAllValidations)
        api.GET("/validation/:id", getValidationByID)
        api.POST("/validation", createValidation)
        api.PUT("/validation/:id", updateValidation)
        api.DELETE("/validation/:id", deleteValidation)
    }

    r.Run(":8080")
}
