package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Decorator struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var decorators = []{name}{}

func getAllDecorators(c *gin.Context) {
    c.JSON(http.StatusOK, decorators)
}

func getDecoratorByID(c *gin.Context) {
    id := c.Param("id")
    // Find Decorator by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Decorator"})
}

func createDecorator(c *gin.Context) {
    var newDecorator Decorator
    if err := c.BindJSON(&newDecorator); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    decorators = append(decorators, newDecorator)
    c.JSON(http.StatusCreated, newDecorator)
}

func updateDecorator(c *gin.Context) {
    id := c.Param("id")
    var updatedDecorator Decorator
    if err := c.BindJSON(&updatedDecorator); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedDecorator)
}

func deleteDecorator(c *gin.Context) {
    id := c.Param("id")
    // Delete Decorator
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/decorator", getAllDecorators)
        api.GET("/decorator/:id", getDecoratorByID)
        api.POST("/decorator", createDecorator)
        api.PUT("/decorator/:id", updateDecorator)
        api.DELETE("/decorator/:id", deleteDecorator)
    }

    r.Run(":8080")
}
