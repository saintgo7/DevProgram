package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Endpoint struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var endpoints = []{name}{}

func getAllEndpoints(c *gin.Context) {
    c.JSON(http.StatusOK, endpoints)
}

func getEndpointByID(c *gin.Context) {
    id := c.Param("id")
    // Find Endpoint by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Endpoint"})
}

func createEndpoint(c *gin.Context) {
    var newEndpoint Endpoint
    if err := c.BindJSON(&newEndpoint); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    endpoints = append(endpoints, newEndpoint)
    c.JSON(http.StatusCreated, newEndpoint)
}

func updateEndpoint(c *gin.Context) {
    id := c.Param("id")
    var updatedEndpoint Endpoint
    if err := c.BindJSON(&updatedEndpoint); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedEndpoint)
}

func deleteEndpoint(c *gin.Context) {
    id := c.Param("id")
    // Delete Endpoint
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/endpoint", getAllEndpoints)
        api.GET("/endpoint/:id", getEndpointByID)
        api.POST("/endpoint", createEndpoint)
        api.PUT("/endpoint/:id", updateEndpoint)
        api.DELETE("/endpoint/:id", deleteEndpoint)
    }

    r.Run(":8080")
}
