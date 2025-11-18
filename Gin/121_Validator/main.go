package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Validator struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var validators = []{name}{}

func getAllValidators(c *gin.Context) {
    c.JSON(http.StatusOK, validators)
}

func getValidatorByID(c *gin.Context) {
    id := c.Param("id")
    // Find Validator by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Validator"})
}

func createValidator(c *gin.Context) {
    var newValidator Validator
    if err := c.BindJSON(&newValidator); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    validators = append(validators, newValidator)
    c.JSON(http.StatusCreated, newValidator)
}

func updateValidator(c *gin.Context) {
    id := c.Param("id")
    var updatedValidator Validator
    if err := c.BindJSON(&updatedValidator); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedValidator)
}

func deleteValidator(c *gin.Context) {
    id := c.Param("id")
    // Delete Validator
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/validator", getAllValidators)
        api.GET("/validator/:id", getValidatorByID)
        api.POST("/validator", createValidator)
        api.PUT("/validator/:id", updateValidator)
        api.DELETE("/validator/:id", deleteValidator)
    }

    r.Run(":8080")
}
