package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Geography struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var geographys = []{name}{}

func getAllGeographys(c *gin.Context) {
    c.JSON(http.StatusOK, geographys)
}

func getGeographyByID(c *gin.Context) {
    id := c.Param("id")
    // Find Geography by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Geography"})
}

func createGeography(c *gin.Context) {
    var newGeography Geography
    if err := c.BindJSON(&newGeography); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    geographys = append(geographys, newGeography)
    c.JSON(http.StatusCreated, newGeography)
}

func updateGeography(c *gin.Context) {
    id := c.Param("id")
    var updatedGeography Geography
    if err := c.BindJSON(&updatedGeography); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedGeography)
}

func deleteGeography(c *gin.Context) {
    id := c.Param("id")
    // Delete Geography
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/geography", getAllGeographys)
        api.GET("/geography/:id", getGeographyByID)
        api.POST("/geography", createGeography)
        api.PUT("/geography/:id", updateGeography)
        api.DELETE("/geography/:id", deleteGeography)
    }

    r.Run(":8080")
}
