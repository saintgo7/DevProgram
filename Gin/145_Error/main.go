package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Error struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var errors = []{name}{}

func getAllErrors(c *gin.Context) {
    c.JSON(http.StatusOK, errors)
}

func getErrorByID(c *gin.Context) {
    id := c.Param("id")
    // Find Error by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Error"})
}

func createError(c *gin.Context) {
    var newError Error
    if err := c.BindJSON(&newError); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    errors = append(errors, newError)
    c.JSON(http.StatusCreated, newError)
}

func updateError(c *gin.Context) {
    id := c.Param("id")
    var updatedError Error
    if err := c.BindJSON(&updatedError); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedError)
}

func deleteError(c *gin.Context) {
    id := c.Param("id")
    // Delete Error
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/error", getAllErrors)
        api.GET("/error/:id", getErrorByID)
        api.POST("/error", createError)
        api.PUT("/error/:id", updateError)
        api.DELETE("/error/:id", deleteError)
    }

    r.Run(":8080")
}
