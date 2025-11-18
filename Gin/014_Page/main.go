package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Page struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var pages = []{name}{}

func getAllPages(c *gin.Context) {
    c.JSON(http.StatusOK, pages)
}

func getPageByID(c *gin.Context) {
    id := c.Param("id")
    // Find Page by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Page"})
}

func createPage(c *gin.Context) {
    var newPage Page
    if err := c.BindJSON(&newPage); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    pages = append(pages, newPage)
    c.JSON(http.StatusCreated, newPage)
}

func updatePage(c *gin.Context) {
    id := c.Param("id")
    var updatedPage Page
    if err := c.BindJSON(&updatedPage); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPage)
}

func deletePage(c *gin.Context) {
    id := c.Param("id")
    // Delete Page
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/page", getAllPages)
        api.GET("/page/:id", getPageByID)
        api.POST("/page", createPage)
        api.PUT("/page/:id", updatePage)
        api.DELETE("/page/:id", deletePage)
    }

    r.Run(":8080")
}
