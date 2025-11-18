package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Session struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var sessions = []{name}{}

func getAllSessions(c *gin.Context) {
    c.JSON(http.StatusOK, sessions)
}

func getSessionByID(c *gin.Context) {
    id := c.Param("id")
    // Find Session by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Session"})
}

func createSession(c *gin.Context) {
    var newSession Session
    if err := c.BindJSON(&newSession); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    sessions = append(sessions, newSession)
    c.JSON(http.StatusCreated, newSession)
}

func updateSession(c *gin.Context) {
    id := c.Param("id")
    var updatedSession Session
    if err := c.BindJSON(&updatedSession); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSession)
}

func deleteSession(c *gin.Context) {
    id := c.Param("id")
    // Delete Session
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/session", getAllSessions)
        api.GET("/session/:id", getSessionByID)
        api.POST("/session", createSession)
        api.PUT("/session/:id", updateSession)
        api.DELETE("/session/:id", deleteSession)
    }

    r.Run(":8080")
}
