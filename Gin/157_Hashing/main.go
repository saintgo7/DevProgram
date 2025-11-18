package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Hashing struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var hashings = []{name}{}

func getAllHashings(c *gin.Context) {
    c.JSON(http.StatusOK, hashings)
}

func getHashingByID(c *gin.Context) {
    id := c.Param("id")
    // Find Hashing by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Hashing"})
}

func createHashing(c *gin.Context) {
    var newHashing Hashing
    if err := c.BindJSON(&newHashing); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    hashings = append(hashings, newHashing)
    c.JSON(http.StatusCreated, newHashing)
}

func updateHashing(c *gin.Context) {
    id := c.Param("id")
    var updatedHashing Hashing
    if err := c.BindJSON(&updatedHashing); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedHashing)
}

func deleteHashing(c *gin.Context) {
    id := c.Param("id")
    // Delete Hashing
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/hashing", getAllHashings)
        api.GET("/hashing/:id", getHashingByID)
        api.POST("/hashing", createHashing)
        api.PUT("/hashing/:id", updateHashing)
        api.DELETE("/hashing/:id", deleteHashing)
    }

    r.Run(":8080")
}
