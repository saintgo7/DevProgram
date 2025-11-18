package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Relationship struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var relationships = []{name}{}

func getAllRelationships(c *gin.Context) {
    c.JSON(http.StatusOK, relationships)
}

func getRelationshipByID(c *gin.Context) {
    id := c.Param("id")
    // Find Relationship by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Relationship"})
}

func createRelationship(c *gin.Context) {
    var newRelationship Relationship
    if err := c.BindJSON(&newRelationship); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    relationships = append(relationships, newRelationship)
    c.JSON(http.StatusCreated, newRelationship)
}

func updateRelationship(c *gin.Context) {
    id := c.Param("id")
    var updatedRelationship Relationship
    if err := c.BindJSON(&updatedRelationship); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedRelationship)
}

func deleteRelationship(c *gin.Context) {
    id := c.Param("id")
    // Delete Relationship
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/relationship", getAllRelationships)
        api.GET("/relationship/:id", getRelationshipByID)
        api.POST("/relationship", createRelationship)
        api.PUT("/relationship/:id", updateRelationship)
        api.DELETE("/relationship/:id", deleteRelationship)
    }

    r.Run(":8080")
}
