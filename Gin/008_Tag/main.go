package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Tag struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var tags = []{name}{}

func getAllTags(c *gin.Context) {
    c.JSON(http.StatusOK, tags)
}

func getTagByID(c *gin.Context) {
    id := c.Param("id")
    // Find Tag by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Tag"})
}

func createTag(c *gin.Context) {
    var newTag Tag
    if err := c.BindJSON(&newTag); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    tags = append(tags, newTag)
    c.JSON(http.StatusCreated, newTag)
}

func updateTag(c *gin.Context) {
    id := c.Param("id")
    var updatedTag Tag
    if err := c.BindJSON(&updatedTag); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedTag)
}

func deleteTag(c *gin.Context) {
    id := c.Param("id")
    // Delete Tag
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/tag", getAllTags)
        api.GET("/tag/:id", getTagByID)
        api.POST("/tag", createTag)
        api.PUT("/tag/:id", updateTag)
        api.DELETE("/tag/:id", deleteTag)
    }

    r.Run(":8080")
}
