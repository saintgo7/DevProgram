package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Customs struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var customss = []{name}{}

func getAllCustomss(c *gin.Context) {
    c.JSON(http.StatusOK, customss)
}

func getCustomsByID(c *gin.Context) {
    id := c.Param("id")
    // Find Customs by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Customs"})
}

func createCustoms(c *gin.Context) {
    var newCustoms Customs
    if err := c.BindJSON(&newCustoms); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    customss = append(customss, newCustoms)
    c.JSON(http.StatusCreated, newCustoms)
}

func updateCustoms(c *gin.Context) {
    id := c.Param("id")
    var updatedCustoms Customs
    if err := c.BindJSON(&updatedCustoms); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCustoms)
}

func deleteCustoms(c *gin.Context) {
    id := c.Param("id")
    // Delete Customs
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/customs", getAllCustomss)
        api.GET("/customs/:id", getCustomsByID)
        api.POST("/customs", createCustoms)
        api.PUT("/customs/:id", updateCustoms)
        api.DELETE("/customs/:id", deleteCustoms)
    }

    r.Run(":8080")
}
