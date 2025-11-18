package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Zone struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var zones = []{name}{}

func getAllZones(c *gin.Context) {
    c.JSON(http.StatusOK, zones)
}

func getZoneByID(c *gin.Context) {
    id := c.Param("id")
    // Find Zone by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Zone"})
}

func createZone(c *gin.Context) {
    var newZone Zone
    if err := c.BindJSON(&newZone); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    zones = append(zones, newZone)
    c.JSON(http.StatusCreated, newZone)
}

func updateZone(c *gin.Context) {
    id := c.Param("id")
    var updatedZone Zone
    if err := c.BindJSON(&updatedZone); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedZone)
}

func deleteZone(c *gin.Context) {
    id := c.Param("id")
    // Delete Zone
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/zone", getAllZones)
        api.GET("/zone/:id", getZoneByID)
        api.POST("/zone", createZone)
        api.PUT("/zone/:id", updateZone)
        api.DELETE("/zone/:id", deleteZone)
    }

    r.Run(":8080")
}
