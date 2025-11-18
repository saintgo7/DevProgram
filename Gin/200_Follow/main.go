package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Follow struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var follows = []{name}{}

func getAllFollows(c *gin.Context) {
    c.JSON(http.StatusOK, follows)
}

func getFollowByID(c *gin.Context) {
    id := c.Param("id")
    // Find Follow by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Follow"})
}

func createFollow(c *gin.Context) {
    var newFollow Follow
    if err := c.BindJSON(&newFollow); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    follows = append(follows, newFollow)
    c.JSON(http.StatusCreated, newFollow)
}

func updateFollow(c *gin.Context) {
    id := c.Param("id")
    var updatedFollow Follow
    if err := c.BindJSON(&updatedFollow); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedFollow)
}

func deleteFollow(c *gin.Context) {
    id := c.Param("id")
    // Delete Follow
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/follow", getAllFollows)
        api.GET("/follow/:id", getFollowByID)
        api.POST("/follow", createFollow)
        api.PUT("/follow/:id", updateFollow)
        api.DELETE("/follow/:id", deleteFollow)
    }

    r.Run(":8080")
}
