package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Message struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var messages = []{name}{}

func getAllMessages(c *gin.Context) {
    c.JSON(http.StatusOK, messages)
}

func getMessageByID(c *gin.Context) {
    id := c.Param("id")
    // Find Message by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Message"})
}

func createMessage(c *gin.Context) {
    var newMessage Message
    if err := c.BindJSON(&newMessage); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    messages = append(messages, newMessage)
    c.JSON(http.StatusCreated, newMessage)
}

func updateMessage(c *gin.Context) {
    id := c.Param("id")
    var updatedMessage Message
    if err := c.BindJSON(&updatedMessage); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedMessage)
}

func deleteMessage(c *gin.Context) {
    id := c.Param("id")
    // Delete Message
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/message", getAllMessages)
        api.GET("/message/:id", getMessageByID)
        api.POST("/message", createMessage)
        api.PUT("/message/:id", updateMessage)
        api.DELETE("/message/:id", deleteMessage)
    }

    r.Run(":8080")
}
