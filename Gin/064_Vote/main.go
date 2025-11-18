package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Vote struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var votes = []{name}{}

func getAllVotes(c *gin.Context) {
    c.JSON(http.StatusOK, votes)
}

func getVoteByID(c *gin.Context) {
    id := c.Param("id")
    // Find Vote by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Vote"})
}

func createVote(c *gin.Context) {
    var newVote Vote
    if err := c.BindJSON(&newVote); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    votes = append(votes, newVote)
    c.JSON(http.StatusCreated, newVote)
}

func updateVote(c *gin.Context) {
    id := c.Param("id")
    var updatedVote Vote
    if err := c.BindJSON(&updatedVote); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedVote)
}

func deleteVote(c *gin.Context) {
    id := c.Param("id")
    // Delete Vote
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/vote", getAllVotes)
        api.GET("/vote/:id", getVoteByID)
        api.POST("/vote", createVote)
        api.PUT("/vote/:id", updateVote)
        api.DELETE("/vote/:id", deleteVote)
    }

    r.Run(":8080")
}
