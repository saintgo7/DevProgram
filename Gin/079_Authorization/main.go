package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Authorization struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var authorizations = []{name}{}

func getAllAuthorizations(c *gin.Context) {
    c.JSON(http.StatusOK, authorizations)
}

func getAuthorizationByID(c *gin.Context) {
    id := c.Param("id")
    // Find Authorization by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Authorization"})
}

func createAuthorization(c *gin.Context) {
    var newAuthorization Authorization
    if err := c.BindJSON(&newAuthorization); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    authorizations = append(authorizations, newAuthorization)
    c.JSON(http.StatusCreated, newAuthorization)
}

func updateAuthorization(c *gin.Context) {
    id := c.Param("id")
    var updatedAuthorization Authorization
    if err := c.BindJSON(&updatedAuthorization); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAuthorization)
}

func deleteAuthorization(c *gin.Context) {
    id := c.Param("id")
    // Delete Authorization
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/authorization", getAllAuthorizations)
        api.GET("/authorization/:id", getAuthorizationByID)
        api.POST("/authorization", createAuthorization)
        api.PUT("/authorization/:id", updateAuthorization)
        api.DELETE("/authorization/:id", deleteAuthorization)
    }

    r.Run(":8080")
}
