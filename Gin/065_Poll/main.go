package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Poll struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var polls = []{name}{}

func getAllPolls(c *gin.Context) {
    c.JSON(http.StatusOK, polls)
}

func getPollByID(c *gin.Context) {
    id := c.Param("id")
    // Find Poll by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Poll"})
}

func createPoll(c *gin.Context) {
    var newPoll Poll
    if err := c.BindJSON(&newPoll); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    polls = append(polls, newPoll)
    c.JSON(http.StatusCreated, newPoll)
}

func updatePoll(c *gin.Context) {
    id := c.Param("id")
    var updatedPoll Poll
    if err := c.BindJSON(&updatedPoll); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPoll)
}

func deletePoll(c *gin.Context) {
    id := c.Param("id")
    // Delete Poll
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/poll", getAllPolls)
        api.GET("/poll/:id", getPollByID)
        api.POST("/poll", createPoll)
        api.PUT("/poll/:id", updatePoll)
        api.DELETE("/poll/:id", deletePoll)
    }

    r.Run(":8080")
}
