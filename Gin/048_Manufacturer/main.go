package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Manufacturer struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var manufacturers = []{name}{}

func getAllManufacturers(c *gin.Context) {
    c.JSON(http.StatusOK, manufacturers)
}

func getManufacturerByID(c *gin.Context) {
    id := c.Param("id")
    // Find Manufacturer by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Manufacturer"})
}

func createManufacturer(c *gin.Context) {
    var newManufacturer Manufacturer
    if err := c.BindJSON(&newManufacturer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    manufacturers = append(manufacturers, newManufacturer)
    c.JSON(http.StatusCreated, newManufacturer)
}

func updateManufacturer(c *gin.Context) {
    id := c.Param("id")
    var updatedManufacturer Manufacturer
    if err := c.BindJSON(&updatedManufacturer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedManufacturer)
}

func deleteManufacturer(c *gin.Context) {
    id := c.Param("id")
    // Delete Manufacturer
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/manufacturer", getAllManufacturers)
        api.GET("/manufacturer/:id", getManufacturerByID)
        api.POST("/manufacturer", createManufacturer)
        api.PUT("/manufacturer/:id", updateManufacturer)
        api.DELETE("/manufacturer/:id", deleteManufacturer)
    }

    r.Run(":8080")
}
