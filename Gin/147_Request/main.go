package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Request struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var requests = []{name}{}

func getAllRequests(c *gin.Context) {
    c.JSON(http.StatusOK, requests)
}

func getRequestByID(c *gin.Context) {
    id := c.Param("id")
    // Find Request by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Request"})
}

func createRequest(c *gin.Context) {
    var newRequest Request
    if err := c.BindJSON(&newRequest); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    requests = append(requests, newRequest)
    c.JSON(http.StatusCreated, newRequest)
}

func updateRequest(c *gin.Context) {
    id := c.Param("id")
    var updatedRequest Request
    if err := c.BindJSON(&updatedRequest); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedRequest)
}

func deleteRequest(c *gin.Context) {
    id := c.Param("id")
    // Delete Request
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/request", getAllRequests)
        api.GET("/request/:id", getRequestByID)
        api.POST("/request", createRequest)
        api.PUT("/request/:id", updateRequest)
        api.DELETE("/request/:id", deleteRequest)
    }

    r.Run(":8080")
}
