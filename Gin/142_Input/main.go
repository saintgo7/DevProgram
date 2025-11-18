package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Input struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var inputs = []{name}{}

func getAllInputs(c *gin.Context) {
    c.JSON(http.StatusOK, inputs)
}

func getInputByID(c *gin.Context) {
    id := c.Param("id")
    // Find Input by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Input"})
}

func createInput(c *gin.Context) {
    var newInput Input
    if err := c.BindJSON(&newInput); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    inputs = append(inputs, newInput)
    c.JSON(http.StatusCreated, newInput)
}

func updateInput(c *gin.Context) {
    id := c.Param("id")
    var updatedInput Input
    if err := c.BindJSON(&updatedInput); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedInput)
}

func deleteInput(c *gin.Context) {
    id := c.Param("id")
    // Delete Input
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/input", getAllInputs)
        api.GET("/input/:id", getInputByID)
        api.POST("/input", createInput)
        api.PUT("/input/:id", updateInput)
        api.DELETE("/input/:id", deleteInput)
    }

    r.Run(":8080")
}
