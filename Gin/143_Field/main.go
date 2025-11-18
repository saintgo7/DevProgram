package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Field struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var fields = []{name}{}

func getAllFields(c *gin.Context) {
    c.JSON(http.StatusOK, fields)
}

func getFieldByID(c *gin.Context) {
    id := c.Param("id")
    // Find Field by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Field"})
}

func createField(c *gin.Context) {
    var newField Field
    if err := c.BindJSON(&newField); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    fields = append(fields, newField)
    c.JSON(http.StatusCreated, newField)
}

func updateField(c *gin.Context) {
    id := c.Param("id")
    var updatedField Field
    if err := c.BindJSON(&updatedField); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedField)
}

func deleteField(c *gin.Context) {
    id := c.Param("id")
    // Delete Field
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/field", getAllFields)
        api.GET("/field/:id", getFieldByID)
        api.POST("/field", createField)
        api.PUT("/field/:id", updateField)
        api.DELETE("/field/:id", deleteField)
    }

    r.Run(":8080")
}
