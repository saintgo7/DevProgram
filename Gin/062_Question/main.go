package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Question struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var questions = []{name}{}

func getAllQuestions(c *gin.Context) {
    c.JSON(http.StatusOK, questions)
}

func getQuestionByID(c *gin.Context) {
    id := c.Param("id")
    // Find Question by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Question"})
}

func createQuestion(c *gin.Context) {
    var newQuestion Question
    if err := c.BindJSON(&newQuestion); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    questions = append(questions, newQuestion)
    c.JSON(http.StatusCreated, newQuestion)
}

func updateQuestion(c *gin.Context) {
    id := c.Param("id")
    var updatedQuestion Question
    if err := c.BindJSON(&updatedQuestion); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedQuestion)
}

func deleteQuestion(c *gin.Context) {
    id := c.Param("id")
    // Delete Question
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/question", getAllQuestions)
        api.GET("/question/:id", getQuestionByID)
        api.POST("/question", createQuestion)
        api.PUT("/question/:id", updateQuestion)
        api.DELETE("/question/:id", deleteQuestion)
    }

    r.Run(":8080")
}
