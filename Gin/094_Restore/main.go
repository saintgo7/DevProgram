package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Restore struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var restores = []{name}{}

func getAllRestores(c *gin.Context) {
    c.JSON(http.StatusOK, restores)
}

func getRestoreByID(c *gin.Context) {
    id := c.Param("id")
    // Find Restore by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Restore"})
}

func createRestore(c *gin.Context) {
    var newRestore Restore
    if err := c.BindJSON(&newRestore); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    restores = append(restores, newRestore)
    c.JSON(http.StatusCreated, newRestore)
}

func updateRestore(c *gin.Context) {
    id := c.Param("id")
    var updatedRestore Restore
    if err := c.BindJSON(&updatedRestore); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedRestore)
}

func deleteRestore(c *gin.Context) {
    id := c.Param("id")
    // Delete Restore
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/restore", getAllRestores)
        api.GET("/restore/:id", getRestoreByID)
        api.POST("/restore", createRestore)
        api.PUT("/restore/:id", updateRestore)
        api.DELETE("/restore/:id", deleteRestore)
    }

    r.Run(":8080")
}
