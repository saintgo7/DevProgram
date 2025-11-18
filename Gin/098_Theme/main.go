package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Theme struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var themes = []{name}{}

func getAllThemes(c *gin.Context) {
    c.JSON(http.StatusOK, themes)
}

func getThemeByID(c *gin.Context) {
    id := c.Param("id")
    // Find Theme by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Theme"})
}

func createTheme(c *gin.Context) {
    var newTheme Theme
    if err := c.BindJSON(&newTheme); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    themes = append(themes, newTheme)
    c.JSON(http.StatusCreated, newTheme)
}

func updateTheme(c *gin.Context) {
    id := c.Param("id")
    var updatedTheme Theme
    if err := c.BindJSON(&updatedTheme); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedTheme)
}

func deleteTheme(c *gin.Context) {
    id := c.Param("id")
    // Delete Theme
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/theme", getAllThemes)
        api.GET("/theme/:id", getThemeByID)
        api.POST("/theme", createTheme)
        api.PUT("/theme/:id", updateTheme)
        api.DELETE("/theme/:id", deleteTheme)
    }

    r.Run(":8080")
}
