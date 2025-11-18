package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Schema struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var schemas = []{name}{}

func getAllSchemas(c *gin.Context) {
    c.JSON(http.StatusOK, schemas)
}

func getSchemaByID(c *gin.Context) {
    id := c.Param("id")
    // Find Schema by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Schema"})
}

func createSchema(c *gin.Context) {
    var newSchema Schema
    if err := c.BindJSON(&newSchema); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    schemas = append(schemas, newSchema)
    c.JSON(http.StatusCreated, newSchema)
}

func updateSchema(c *gin.Context) {
    id := c.Param("id")
    var updatedSchema Schema
    if err := c.BindJSON(&updatedSchema); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSchema)
}

func deleteSchema(c *gin.Context) {
    id := c.Param("id")
    // Delete Schema
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/schema", getAllSchemas)
        api.GET("/schema/:id", getSchemaByID)
        api.POST("/schema", createSchema)
        api.PUT("/schema/:id", updateSchema)
        api.DELETE("/schema/:id", deleteSchema)
    }

    r.Run(":8080")
}
