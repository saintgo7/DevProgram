package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Response struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var responses = []{name}{}

func getAllResponses(c *gin.Context) {
    c.JSON(http.StatusOK, responses)
}

func getResponseByID(c *gin.Context) {
    id := c.Param("id")
    // Find Response by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Response"})
}

func createResponse(c *gin.Context) {
    var newResponse Response
    if err := c.BindJSON(&newResponse); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    responses = append(responses, newResponse)
    c.JSON(http.StatusCreated, newResponse)
}

func updateResponse(c *gin.Context) {
    id := c.Param("id")
    var updatedResponse Response
    if err := c.BindJSON(&updatedResponse); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedResponse)
}

func deleteResponse(c *gin.Context) {
    id := c.Param("id")
    // Delete Response
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/response", getAllResponses)
        api.GET("/response/:id", getResponseByID)
        api.POST("/response", createResponse)
        api.PUT("/response/:id", updateResponse)
        api.DELETE("/response/:id", deleteResponse)
    }

    r.Run(":8080")
}
