package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Widget struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var widgets = []{name}{}

func getAllWidgets(c *gin.Context) {
    c.JSON(http.StatusOK, widgets)
}

func getWidgetByID(c *gin.Context) {
    id := c.Param("id")
    // Find Widget by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Widget"})
}

func createWidget(c *gin.Context) {
    var newWidget Widget
    if err := c.BindJSON(&newWidget); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    widgets = append(widgets, newWidget)
    c.JSON(http.StatusCreated, newWidget)
}

func updateWidget(c *gin.Context) {
    id := c.Param("id")
    var updatedWidget Widget
    if err := c.BindJSON(&updatedWidget); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedWidget)
}

func deleteWidget(c *gin.Context) {
    id := c.Param("id")
    // Delete Widget
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/widget", getAllWidgets)
        api.GET("/widget/:id", getWidgetByID)
        api.POST("/widget", createWidget)
        api.PUT("/widget/:id", updateWidget)
        api.DELETE("/widget/:id", deleteWidget)
    }

    r.Run(":8080")
}
