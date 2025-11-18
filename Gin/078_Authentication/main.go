package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Authentication struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var authentications = []{name}{}

func getAllAuthentications(c *gin.Context) {
    c.JSON(http.StatusOK, authentications)
}

func getAuthenticationByID(c *gin.Context) {
    id := c.Param("id")
    // Find Authentication by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Authentication"})
}

func createAuthentication(c *gin.Context) {
    var newAuthentication Authentication
    if err := c.BindJSON(&newAuthentication); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    authentications = append(authentications, newAuthentication)
    c.JSON(http.StatusCreated, newAuthentication)
}

func updateAuthentication(c *gin.Context) {
    id := c.Param("id")
    var updatedAuthentication Authentication
    if err := c.BindJSON(&updatedAuthentication); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAuthentication)
}

func deleteAuthentication(c *gin.Context) {
    id := c.Param("id")
    // Delete Authentication
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/authentication", getAllAuthentications)
        api.GET("/authentication/:id", getAuthenticationByID)
        api.POST("/authentication", createAuthentication)
        api.PUT("/authentication/:id", updateAuthentication)
        api.DELETE("/authentication/:id", deleteAuthentication)
    }

    r.Run(":8080")
}
