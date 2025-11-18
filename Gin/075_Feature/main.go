package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Feature struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var features = []{name}{}

func getAllFeatures(c *gin.Context) {
    c.JSON(http.StatusOK, features)
}

func getFeatureByID(c *gin.Context) {
    id := c.Param("id")
    // Find Feature by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Feature"})
}

func createFeature(c *gin.Context) {
    var newFeature Feature
    if err := c.BindJSON(&newFeature); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    features = append(features, newFeature)
    c.JSON(http.StatusCreated, newFeature)
}

func updateFeature(c *gin.Context) {
    id := c.Param("id")
    var updatedFeature Feature
    if err := c.BindJSON(&updatedFeature); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedFeature)
}

func deleteFeature(c *gin.Context) {
    id := c.Param("id")
    // Delete Feature
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/feature", getAllFeatures)
        api.GET("/feature/:id", getFeatureByID)
        api.POST("/feature", createFeature)
        api.PUT("/feature/:id", updateFeature)
        api.DELETE("/feature/:id", deleteFeature)
    }

    r.Run(":8080")
}
