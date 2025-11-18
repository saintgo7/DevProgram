package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Model struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var models = []{name}{}

func getAllModels(c *gin.Context) {
    c.JSON(http.StatusOK, models)
}

func getModelByID(c *gin.Context) {
    id := c.Param("id")
    // Find Model by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Model"})
}

func createModel(c *gin.Context) {
    var newModel Model
    if err := c.BindJSON(&newModel); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    models = append(models, newModel)
    c.JSON(http.StatusCreated, newModel)
}

func updateModel(c *gin.Context) {
    id := c.Param("id")
    var updatedModel Model
    if err := c.BindJSON(&updatedModel); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedModel)
}

func deleteModel(c *gin.Context) {
    id := c.Param("id")
    // Delete Model
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/model", getAllModels)
        api.GET("/model/:id", getModelByID)
        api.POST("/model", createModel)
        api.PUT("/model/:id", updateModel)
        api.DELETE("/model/:id", deleteModel)
    }

    r.Run(":8080")
}
