package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Repository struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var repositorys = []{name}{}

func getAllRepositorys(c *gin.Context) {
    c.JSON(http.StatusOK, repositorys)
}

func getRepositoryByID(c *gin.Context) {
    id := c.Param("id")
    // Find Repository by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Repository"})
}

func createRepository(c *gin.Context) {
    var newRepository Repository
    if err := c.BindJSON(&newRepository); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    repositorys = append(repositorys, newRepository)
    c.JSON(http.StatusCreated, newRepository)
}

func updateRepository(c *gin.Context) {
    id := c.Param("id")
    var updatedRepository Repository
    if err := c.BindJSON(&updatedRepository); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedRepository)
}

func deleteRepository(c *gin.Context) {
    id := c.Param("id")
    // Delete Repository
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/repository", getAllRepositorys)
        api.GET("/repository/:id", getRepositoryByID)
        api.POST("/repository", createRepository)
        api.PUT("/repository/:id", updateRepository)
        api.DELETE("/repository/:id", deleteRepository)
    }

    r.Run(":8080")
}
