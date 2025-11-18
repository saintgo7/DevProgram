package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Middleware struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var middlewares = []{name}{}

func getAllMiddlewares(c *gin.Context) {
    c.JSON(http.StatusOK, middlewares)
}

func getMiddlewareByID(c *gin.Context) {
    id := c.Param("id")
    // Find Middleware by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Middleware"})
}

func createMiddleware(c *gin.Context) {
    var newMiddleware Middleware
    if err := c.BindJSON(&newMiddleware); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    middlewares = append(middlewares, newMiddleware)
    c.JSON(http.StatusCreated, newMiddleware)
}

func updateMiddleware(c *gin.Context) {
    id := c.Param("id")
    var updatedMiddleware Middleware
    if err := c.BindJSON(&updatedMiddleware); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedMiddleware)
}

func deleteMiddleware(c *gin.Context) {
    id := c.Param("id")
    // Delete Middleware
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/middleware", getAllMiddlewares)
        api.GET("/middleware/:id", getMiddlewareByID)
        api.POST("/middleware", createMiddleware)
        api.PUT("/middleware/:id", updateMiddleware)
        api.DELETE("/middleware/:id", deleteMiddleware)
    }

    r.Run(":8080")
}
