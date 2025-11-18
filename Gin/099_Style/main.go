package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Style struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var styles = []{name}{}

func getAllStyles(c *gin.Context) {
    c.JSON(http.StatusOK, styles)
}

func getStyleByID(c *gin.Context) {
    id := c.Param("id")
    // Find Style by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Style"})
}

func createStyle(c *gin.Context) {
    var newStyle Style
    if err := c.BindJSON(&newStyle); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    styles = append(styles, newStyle)
    c.JSON(http.StatusCreated, newStyle)
}

func updateStyle(c *gin.Context) {
    id := c.Param("id")
    var updatedStyle Style
    if err := c.BindJSON(&updatedStyle); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedStyle)
}

func deleteStyle(c *gin.Context) {
    id := c.Param("id")
    // Delete Style
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/style", getAllStyles)
        api.GET("/style/:id", getStyleByID)
        api.POST("/style", createStyle)
        api.PUT("/style/:id", updateStyle)
        api.DELETE("/style/:id", deleteStyle)
    }

    r.Run(":8080")
}
