package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Option struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var options = []{name}{}

func getAllOptions(c *gin.Context) {
    c.JSON(http.StatusOK, options)
}

func getOptionByID(c *gin.Context) {
    id := c.Param("id")
    // Find Option by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Option"})
}

func createOption(c *gin.Context) {
    var newOption Option
    if err := c.BindJSON(&newOption); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    options = append(options, newOption)
    c.JSON(http.StatusCreated, newOption)
}

func updateOption(c *gin.Context) {
    id := c.Param("id")
    var updatedOption Option
    if err := c.BindJSON(&updatedOption); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedOption)
}

func deleteOption(c *gin.Context) {
    id := c.Param("id")
    // Delete Option
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/option", getAllOptions)
        api.GET("/option/:id", getOptionByID)
        api.POST("/option", createOption)
        api.PUT("/option/:id", updateOption)
        api.DELETE("/option/:id", deleteOption)
    }

    r.Run(":8080")
}
