package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Association struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var associations = []{name}{}

func getAllAssociations(c *gin.Context) {
    c.JSON(http.StatusOK, associations)
}

func getAssociationByID(c *gin.Context) {
    id := c.Param("id")
    // Find Association by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Association"})
}

func createAssociation(c *gin.Context) {
    var newAssociation Association
    if err := c.BindJSON(&newAssociation); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    associations = append(associations, newAssociation)
    c.JSON(http.StatusCreated, newAssociation)
}

func updateAssociation(c *gin.Context) {
    id := c.Param("id")
    var updatedAssociation Association
    if err := c.BindJSON(&updatedAssociation); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAssociation)
}

func deleteAssociation(c *gin.Context) {
    id := c.Param("id")
    // Delete Association
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/association", getAllAssociations)
        api.GET("/association/:id", getAssociationByID)
        api.POST("/association", createAssociation)
        api.PUT("/association/:id", updateAssociation)
        api.DELETE("/association/:id", deleteAssociation)
    }

    r.Run(":8080")
}
