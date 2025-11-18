package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Mapper struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var mappers = []{name}{}

func getAllMappers(c *gin.Context) {
    c.JSON(http.StatusOK, mappers)
}

func getMapperByID(c *gin.Context) {
    id := c.Param("id")
    // Find Mapper by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Mapper"})
}

func createMapper(c *gin.Context) {
    var newMapper Mapper
    if err := c.BindJSON(&newMapper); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    mappers = append(mappers, newMapper)
    c.JSON(http.StatusCreated, newMapper)
}

func updateMapper(c *gin.Context) {
    id := c.Param("id")
    var updatedMapper Mapper
    if err := c.BindJSON(&updatedMapper); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedMapper)
}

func deleteMapper(c *gin.Context) {
    id := c.Param("id")
    // Delete Mapper
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/mapper", getAllMappers)
        api.GET("/mapper/:id", getMapperByID)
        api.POST("/mapper", createMapper)
        api.PUT("/mapper/:id", updateMapper)
        api.DELETE("/mapper/:id", deleteMapper)
    }

    r.Run(":8080")
}
