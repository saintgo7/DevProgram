package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Criteria struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var criterias = []{name}{}

func getAllCriterias(c *gin.Context) {
    c.JSON(http.StatusOK, criterias)
}

func getCriteriaByID(c *gin.Context) {
    id := c.Param("id")
    // Find Criteria by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Criteria"})
}

func createCriteria(c *gin.Context) {
    var newCriteria Criteria
    if err := c.BindJSON(&newCriteria); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    criterias = append(criterias, newCriteria)
    c.JSON(http.StatusCreated, newCriteria)
}

func updateCriteria(c *gin.Context) {
    id := c.Param("id")
    var updatedCriteria Criteria
    if err := c.BindJSON(&updatedCriteria); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCriteria)
}

func deleteCriteria(c *gin.Context) {
    id := c.Param("id")
    // Delete Criteria
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/criteria", getAllCriterias)
        api.GET("/criteria/:id", getCriteriaByID)
        api.POST("/criteria", createCriteria)
        api.PUT("/criteria/:id", updateCriteria)
        api.DELETE("/criteria/:id", deleteCriteria)
    }

    r.Run(":8080")
}
