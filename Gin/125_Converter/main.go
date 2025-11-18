package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Converter struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var converters = []{name}{}

func getAllConverters(c *gin.Context) {
    c.JSON(http.StatusOK, converters)
}

func getConverterByID(c *gin.Context) {
    id := c.Param("id")
    // Find Converter by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Converter"})
}

func createConverter(c *gin.Context) {
    var newConverter Converter
    if err := c.BindJSON(&newConverter); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    converters = append(converters, newConverter)
    c.JSON(http.StatusCreated, newConverter)
}

func updateConverter(c *gin.Context) {
    id := c.Param("id")
    var updatedConverter Converter
    if err := c.BindJSON(&updatedConverter); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedConverter)
}

func deleteConverter(c *gin.Context) {
    id := c.Param("id")
    // Delete Converter
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/converter", getAllConverters)
        api.GET("/converter/:id", getConverterByID)
        api.POST("/converter", createConverter)
        api.PUT("/converter/:id", updateConverter)
        api.DELETE("/converter/:id", deleteConverter)
    }

    r.Run(":8080")
}
