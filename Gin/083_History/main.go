package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type History struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var historys = []{name}{}

func getAllHistorys(c *gin.Context) {
    c.JSON(http.StatusOK, historys)
}

func getHistoryByID(c *gin.Context) {
    id := c.Param("id")
    // Find History by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "History"})
}

func createHistory(c *gin.Context) {
    var newHistory History
    if err := c.BindJSON(&newHistory); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    historys = append(historys, newHistory)
    c.JSON(http.StatusCreated, newHistory)
}

func updateHistory(c *gin.Context) {
    id := c.Param("id")
    var updatedHistory History
    if err := c.BindJSON(&updatedHistory); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedHistory)
}

func deleteHistory(c *gin.Context) {
    id := c.Param("id")
    // Delete History
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/history", getAllHistorys)
        api.GET("/history/:id", getHistoryByID)
        api.POST("/history", createHistory)
        api.PUT("/history/:id", updateHistory)
        api.DELETE("/history/:id", deleteHistory)
    }

    r.Run(":8080")
}
