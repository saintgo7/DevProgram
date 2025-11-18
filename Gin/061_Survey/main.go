package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Survey struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var surveys = []{name}{}

func getAllSurveys(c *gin.Context) {
    c.JSON(http.StatusOK, surveys)
}

func getSurveyByID(c *gin.Context) {
    id := c.Param("id")
    // Find Survey by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Survey"})
}

func createSurvey(c *gin.Context) {
    var newSurvey Survey
    if err := c.BindJSON(&newSurvey); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    surveys = append(surveys, newSurvey)
    c.JSON(http.StatusCreated, newSurvey)
}

func updateSurvey(c *gin.Context) {
    id := c.Param("id")
    var updatedSurvey Survey
    if err := c.BindJSON(&updatedSurvey); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSurvey)
}

func deleteSurvey(c *gin.Context) {
    id := c.Param("id")
    // Delete Survey
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/survey", getAllSurveys)
        api.GET("/survey/:id", getSurveyByID)
        api.POST("/survey", createSurvey)
        api.PUT("/survey/:id", updateSurvey)
        api.DELETE("/survey/:id", deleteSurvey)
    }

    r.Run(":8080")
}
