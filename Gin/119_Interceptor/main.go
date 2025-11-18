package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Interceptor struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var interceptors = []{name}{}

func getAllInterceptors(c *gin.Context) {
    c.JSON(http.StatusOK, interceptors)
}

func getInterceptorByID(c *gin.Context) {
    id := c.Param("id")
    // Find Interceptor by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Interceptor"})
}

func createInterceptor(c *gin.Context) {
    var newInterceptor Interceptor
    if err := c.BindJSON(&newInterceptor); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    interceptors = append(interceptors, newInterceptor)
    c.JSON(http.StatusCreated, newInterceptor)
}

func updateInterceptor(c *gin.Context) {
    id := c.Param("id")
    var updatedInterceptor Interceptor
    if err := c.BindJSON(&updatedInterceptor); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedInterceptor)
}

func deleteInterceptor(c *gin.Context) {
    id := c.Param("id")
    // Delete Interceptor
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/interceptor", getAllInterceptors)
        api.GET("/interceptor/:id", getInterceptorByID)
        api.POST("/interceptor", createInterceptor)
        api.PUT("/interceptor/:id", updateInterceptor)
        api.DELETE("/interceptor/:id", deleteInterceptor)
    }

    r.Run(":8080")
}
