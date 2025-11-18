package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Bookmark struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var bookmarks = []{name}{}

func getAllBookmarks(c *gin.Context) {
    c.JSON(http.StatusOK, bookmarks)
}

func getBookmarkByID(c *gin.Context) {
    id := c.Param("id")
    // Find Bookmark by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Bookmark"})
}

func createBookmark(c *gin.Context) {
    var newBookmark Bookmark
    if err := c.BindJSON(&newBookmark); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    bookmarks = append(bookmarks, newBookmark)
    c.JSON(http.StatusCreated, newBookmark)
}

func updateBookmark(c *gin.Context) {
    id := c.Param("id")
    var updatedBookmark Bookmark
    if err := c.BindJSON(&updatedBookmark); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedBookmark)
}

func deleteBookmark(c *gin.Context) {
    id := c.Param("id")
    // Delete Bookmark
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/bookmark", getAllBookmarks)
        api.GET("/bookmark/:id", getBookmarkByID)
        api.POST("/bookmark", createBookmark)
        api.PUT("/bookmark/:id", updateBookmark)
        api.DELETE("/bookmark/:id", deleteBookmark)
    }

    r.Run(":8080")
}
