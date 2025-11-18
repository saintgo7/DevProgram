package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Graph struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var graphs = []{name}{}

func getAllGraphs(c *gin.Context) {
    c.JSON(http.StatusOK, graphs)
}

func getGraphByID(c *gin.Context) {
    id := c.Param("id")
    // Find Graph by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Graph"})
}

func createGraph(c *gin.Context) {
    var newGraph Graph
    if err := c.BindJSON(&newGraph); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    graphs = append(graphs, newGraph)
    c.JSON(http.StatusCreated, newGraph)
}

func updateGraph(c *gin.Context) {
    id := c.Param("id")
    var updatedGraph Graph
    if err := c.BindJSON(&updatedGraph); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedGraph)
}

func deleteGraph(c *gin.Context) {
    id := c.Param("id")
    // Delete Graph
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/graph", getAllGraphs)
        api.GET("/graph/:id", getGraphByID)
        api.POST("/graph", createGraph)
        api.PUT("/graph/:id", updateGraph)
        api.DELETE("/graph/:id", deleteGraph)
    }

    r.Run(":8080")
}
