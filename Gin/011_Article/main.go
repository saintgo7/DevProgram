package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Article struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var articles = []{name}{}

func getAllArticles(c *gin.Context) {
    c.JSON(http.StatusOK, articles)
}

func getArticleByID(c *gin.Context) {
    id := c.Param("id")
    // Find Article by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Article"})
}

func createArticle(c *gin.Context) {
    var newArticle Article
    if err := c.BindJSON(&newArticle); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    articles = append(articles, newArticle)
    c.JSON(http.StatusCreated, newArticle)
}

func updateArticle(c *gin.Context) {
    id := c.Param("id")
    var updatedArticle Article
    if err := c.BindJSON(&updatedArticle); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedArticle)
}

func deleteArticle(c *gin.Context) {
    id := c.Param("id")
    // Delete Article
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/article", getAllArticles)
        api.GET("/article/:id", getArticleByID)
        api.POST("/article", createArticle)
        api.PUT("/article/:id", updateArticle)
        api.DELETE("/article/:id", deleteArticle)
    }

    r.Run(":8080")
}
