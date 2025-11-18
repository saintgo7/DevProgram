package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Transformer struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var transformers = []{name}{}

func getAllTransformers(c *gin.Context) {
    c.JSON(http.StatusOK, transformers)
}

func getTransformerByID(c *gin.Context) {
    id := c.Param("id")
    // Find Transformer by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Transformer"})
}

func createTransformer(c *gin.Context) {
    var newTransformer Transformer
    if err := c.BindJSON(&newTransformer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    transformers = append(transformers, newTransformer)
    c.JSON(http.StatusCreated, newTransformer)
}

func updateTransformer(c *gin.Context) {
    id := c.Param("id")
    var updatedTransformer Transformer
    if err := c.BindJSON(&updatedTransformer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedTransformer)
}

func deleteTransformer(c *gin.Context) {
    id := c.Param("id")
    // Delete Transformer
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/transformer", getAllTransformers)
        api.GET("/transformer/:id", getTransformerByID)
        api.POST("/transformer", createTransformer)
        api.PUT("/transformer/:id", updateTransformer)
        api.DELETE("/transformer/:id", deleteTransformer)
    }

    r.Run(":8080")
}
