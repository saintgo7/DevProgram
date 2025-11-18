package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Layout struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var layouts = []{name}{}

func getAllLayouts(c *gin.Context) {
    c.JSON(http.StatusOK, layouts)
}

func getLayoutByID(c *gin.Context) {
    id := c.Param("id")
    // Find Layout by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Layout"})
}

func createLayout(c *gin.Context) {
    var newLayout Layout
    if err := c.BindJSON(&newLayout); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    layouts = append(layouts, newLayout)
    c.JSON(http.StatusCreated, newLayout)
}

func updateLayout(c *gin.Context) {
    id := c.Param("id")
    var updatedLayout Layout
    if err := c.BindJSON(&updatedLayout); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedLayout)
}

func deleteLayout(c *gin.Context) {
    id := c.Param("id")
    // Delete Layout
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/layout", getAllLayouts)
        api.GET("/layout/:id", getLayoutByID)
        api.POST("/layout", createLayout)
        api.PUT("/layout/:id", updateLayout)
        api.DELETE("/layout/:id", deleteLayout)
    }

    r.Run(":8080")
}
