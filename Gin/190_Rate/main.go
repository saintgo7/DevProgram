package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Rate struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var rates = []{name}{}

func getAllRates(c *gin.Context) {
    c.JSON(http.StatusOK, rates)
}

func getRateByID(c *gin.Context) {
    id := c.Param("id")
    // Find Rate by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Rate"})
}

func createRate(c *gin.Context) {
    var newRate Rate
    if err := c.BindJSON(&newRate); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    rates = append(rates, newRate)
    c.JSON(http.StatusCreated, newRate)
}

func updateRate(c *gin.Context) {
    id := c.Param("id")
    var updatedRate Rate
    if err := c.BindJSON(&updatedRate); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedRate)
}

func deleteRate(c *gin.Context) {
    id := c.Param("id")
    // Delete Rate
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/rate", getAllRates)
        api.GET("/rate/:id", getRateByID)
        api.POST("/rate", createRate)
        api.PUT("/rate/:id", updateRate)
        api.DELETE("/rate/:id", deleteRate)
    }

    r.Run(":8080")
}
