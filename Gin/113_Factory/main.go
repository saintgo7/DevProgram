package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Factory struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var factorys = []{name}{}

func getAllFactorys(c *gin.Context) {
    c.JSON(http.StatusOK, factorys)
}

func getFactoryByID(c *gin.Context) {
    id := c.Param("id")
    // Find Factory by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Factory"})
}

func createFactory(c *gin.Context) {
    var newFactory Factory
    if err := c.BindJSON(&newFactory); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    factorys = append(factorys, newFactory)
    c.JSON(http.StatusCreated, newFactory)
}

func updateFactory(c *gin.Context) {
    id := c.Param("id")
    var updatedFactory Factory
    if err := c.BindJSON(&updatedFactory); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedFactory)
}

func deleteFactory(c *gin.Context) {
    id := c.Param("id")
    // Delete Factory
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/factory", getAllFactorys)
        api.GET("/factory/:id", getFactoryByID)
        api.POST("/factory", createFactory)
        api.PUT("/factory/:id", updateFactory)
        api.DELETE("/factory/:id", deleteFactory)
    }

    r.Run(":8080")
}
