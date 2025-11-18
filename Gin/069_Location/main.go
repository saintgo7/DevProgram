package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Location struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var locations = []{name}{}

func getAllLocations(c *gin.Context) {
    c.JSON(http.StatusOK, locations)
}

func getLocationByID(c *gin.Context) {
    id := c.Param("id")
    // Find Location by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Location"})
}

func createLocation(c *gin.Context) {
    var newLocation Location
    if err := c.BindJSON(&newLocation); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    locations = append(locations, newLocation)
    c.JSON(http.StatusCreated, newLocation)
}

func updateLocation(c *gin.Context) {
    id := c.Param("id")
    var updatedLocation Location
    if err := c.BindJSON(&updatedLocation); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedLocation)
}

func deleteLocation(c *gin.Context) {
    id := c.Param("id")
    // Delete Location
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/location", getAllLocations)
        api.GET("/location/:id", getLocationByID)
        api.POST("/location", createLocation)
        api.PUT("/location/:id", updateLocation)
        api.DELETE("/location/:id", deleteLocation)
    }

    r.Run(":8080")
}
