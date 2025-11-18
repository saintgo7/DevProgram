package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Category struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var categorys = []{name}{}

func getAllCategorys(c *gin.Context) {
    c.JSON(http.StatusOK, categorys)
}

func getCategoryByID(c *gin.Context) {
    id := c.Param("id")
    // Find Category by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Category"})
}

func createCategory(c *gin.Context) {
    var newCategory Category
    if err := c.BindJSON(&newCategory); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    categorys = append(categorys, newCategory)
    c.JSON(http.StatusCreated, newCategory)
}

func updateCategory(c *gin.Context) {
    id := c.Param("id")
    var updatedCategory Category
    if err := c.BindJSON(&updatedCategory); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCategory)
}

func deleteCategory(c *gin.Context) {
    id := c.Param("id")
    // Delete Category
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/category", getAllCategorys)
        api.GET("/category/:id", getCategoryByID)
        api.POST("/category", createCategory)
        api.PUT("/category/:id", updateCategory)
        api.DELETE("/category/:id", deleteCategory)
    }

    r.Run(":8080")
}
