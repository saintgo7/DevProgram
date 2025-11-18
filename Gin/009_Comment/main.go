package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Comment struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var comments = []{name}{}

func getAllComments(c *gin.Context) {
    c.JSON(http.StatusOK, comments)
}

func getCommentByID(c *gin.Context) {
    id := c.Param("id")
    // Find Comment by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Comment"})
}

func createComment(c *gin.Context) {
    var newComment Comment
    if err := c.BindJSON(&newComment); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    comments = append(comments, newComment)
    c.JSON(http.StatusCreated, newComment)
}

func updateComment(c *gin.Context) {
    id := c.Param("id")
    var updatedComment Comment
    if err := c.BindJSON(&updatedComment); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedComment)
}

func deleteComment(c *gin.Context) {
    id := c.Param("id")
    // Delete Comment
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/comment", getAllComments)
        api.GET("/comment/:id", getCommentByID)
        api.POST("/comment", createComment)
        api.PUT("/comment/:id", updateComment)
        api.DELETE("/comment/:id", deleteComment)
    }

    r.Run(":8080")
}
