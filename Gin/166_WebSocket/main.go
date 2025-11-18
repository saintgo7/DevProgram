package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type WebSocket struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var websockets = []{name}{}

func getAllWebSockets(c *gin.Context) {
    c.JSON(http.StatusOK, websockets)
}

func getWebSocketByID(c *gin.Context) {
    id := c.Param("id")
    // Find WebSocket by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "WebSocket"})
}

func createWebSocket(c *gin.Context) {
    var newWebSocket WebSocket
    if err := c.BindJSON(&newWebSocket); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    websockets = append(websockets, newWebSocket)
    c.JSON(http.StatusCreated, newWebSocket)
}

func updateWebSocket(c *gin.Context) {
    id := c.Param("id")
    var updatedWebSocket WebSocket
    if err := c.BindJSON(&updatedWebSocket); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedWebSocket)
}

func deleteWebSocket(c *gin.Context) {
    id := c.Param("id")
    // Delete WebSocket
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/websocket", getAllWebSockets)
        api.GET("/websocket/:id", getWebSocketByID)
        api.POST("/websocket", createWebSocket)
        api.PUT("/websocket/:id", updateWebSocket)
        api.DELETE("/websocket/:id", deleteWebSocket)
    }

    r.Run(":8080")
}
