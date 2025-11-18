package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Answer struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var answers = []{name}{}

func getAllAnswers(c *gin.Context) {
    c.JSON(http.StatusOK, answers)
}

func getAnswerByID(c *gin.Context) {
    id := c.Param("id")
    // Find Answer by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Answer"})
}

func createAnswer(c *gin.Context) {
    var newAnswer Answer
    if err := c.BindJSON(&newAnswer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    answers = append(answers, newAnswer)
    c.JSON(http.StatusCreated, newAnswer)
}

func updateAnswer(c *gin.Context) {
    id := c.Param("id")
    var updatedAnswer Answer
    if err := c.BindJSON(&updatedAnswer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAnswer)
}

func deleteAnswer(c *gin.Context) {
    id := c.Param("id")
    // Delete Answer
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/answer", getAllAnswers)
        api.GET("/answer/:id", getAnswerByID)
        api.POST("/answer", createAnswer)
        api.PUT("/answer/:id", updateAnswer)
        api.DELETE("/answer/:id", deleteAnswer)
    }

    r.Run(":8080")
}
