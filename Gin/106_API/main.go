package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type API struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var apis = []{name}{}

func getAllAPIs(c *gin.Context) {
    c.JSON(http.StatusOK, apis)
}

func getAPIByID(c *gin.Context) {
    id := c.Param("id")
    // Find API by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "API"})
}

func createAPI(c *gin.Context) {
    var newAPI API
    if err := c.BindJSON(&newAPI); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    apis = append(apis, newAPI)
    c.JSON(http.StatusCreated, newAPI)
}

func updateAPI(c *gin.Context) {
    id := c.Param("id")
    var updatedAPI API
    if err := c.BindJSON(&updatedAPI); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAPI)
}

func deleteAPI(c *gin.Context) {
    id := c.Param("id")
    // Delete API
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/api", getAllAPIs)
        api.GET("/api/:id", getAPIByID)
        api.POST("/api", createAPI)
        api.PUT("/api/:id", updateAPI)
        api.DELETE("/api/:id", deleteAPI)
    }

    r.Run(":8080")
}
