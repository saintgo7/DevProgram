package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Like struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var likes = []{name}{}

func getAllLikes(c *gin.Context) {
    c.JSON(http.StatusOK, likes)
}

func getLikeByID(c *gin.Context) {
    id := c.Param("id")
    // Find Like by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Like"})
}

func createLike(c *gin.Context) {
    var newLike Like
    if err := c.BindJSON(&newLike); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    likes = append(likes, newLike)
    c.JSON(http.StatusCreated, newLike)
}

func updateLike(c *gin.Context) {
    id := c.Param("id")
    var updatedLike Like
    if err := c.BindJSON(&updatedLike); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedLike)
}

func deleteLike(c *gin.Context) {
    id := c.Param("id")
    // Delete Like
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/like", getAllLikes)
        api.GET("/like/:id", getLikeByID)
        api.POST("/like", createLike)
        api.PUT("/like/:id", updateLike)
        api.DELETE("/like/:id", deleteLike)
    }

    r.Run(":8080")
}
