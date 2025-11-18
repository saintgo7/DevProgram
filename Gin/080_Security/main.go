package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Security struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var securitys = []{name}{}

func getAllSecuritys(c *gin.Context) {
    c.JSON(http.StatusOK, securitys)
}

func getSecurityByID(c *gin.Context) {
    id := c.Param("id")
    // Find Security by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Security"})
}

func createSecurity(c *gin.Context) {
    var newSecurity Security
    if err := c.BindJSON(&newSecurity); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    securitys = append(securitys, newSecurity)
    c.JSON(http.StatusCreated, newSecurity)
}

func updateSecurity(c *gin.Context) {
    id := c.Param("id")
    var updatedSecurity Security
    if err := c.BindJSON(&updatedSecurity); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSecurity)
}

func deleteSecurity(c *gin.Context) {
    id := c.Param("id")
    // Delete Security
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/security", getAllSecuritys)
        api.GET("/security/:id", getSecurityByID)
        api.POST("/security", createSecurity)
        api.PUT("/security/:id", updateSecurity)
        api.DELETE("/security/:id", deleteSecurity)
    }

    r.Run(":8080")
}
