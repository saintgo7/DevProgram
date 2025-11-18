package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Post struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var posts = []{name}{}

func getAllPosts(c *gin.Context) {
    c.JSON(http.StatusOK, posts)
}

func getPostByID(c *gin.Context) {
    id := c.Param("id")
    // Find Post by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Post"})
}

func createPost(c *gin.Context) {
    var newPost Post
    if err := c.BindJSON(&newPost); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    posts = append(posts, newPost)
    c.JSON(http.StatusCreated, newPost)
}

func updatePost(c *gin.Context) {
    id := c.Param("id")
    var updatedPost Post
    if err := c.BindJSON(&updatedPost); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPost)
}

func deletePost(c *gin.Context) {
    id := c.Param("id")
    // Delete Post
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/post", getAllPosts)
        api.GET("/post/:id", getPostByID)
        api.POST("/post", createPost)
        api.PUT("/post/:id", updatePost)
        api.DELETE("/post/:id", deletePost)
    }

    r.Run(":8080")
}
