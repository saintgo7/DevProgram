package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Blog struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var blogs = []{name}{}

func getAllBlogs(c *gin.Context) {
    c.JSON(http.StatusOK, blogs)
}

func getBlogByID(c *gin.Context) {
    id := c.Param("id")
    // Find Blog by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Blog"})
}

func createBlog(c *gin.Context) {
    var newBlog Blog
    if err := c.BindJSON(&newBlog); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    blogs = append(blogs, newBlog)
    c.JSON(http.StatusCreated, newBlog)
}

func updateBlog(c *gin.Context) {
    id := c.Param("id")
    var updatedBlog Blog
    if err := c.BindJSON(&updatedBlog); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedBlog)
}

func deleteBlog(c *gin.Context) {
    id := c.Param("id")
    // Delete Blog
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/blog", getAllBlogs)
        api.GET("/blog/:id", getBlogByID)
        api.POST("/blog", createBlog)
        api.PUT("/blog/:id", updateBlog)
        api.DELETE("/blog/:id", deleteBlog)
    }

    r.Run(":8080")
}
