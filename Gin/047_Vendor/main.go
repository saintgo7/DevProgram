package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Vendor struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var vendors = []{name}{}

func getAllVendors(c *gin.Context) {
    c.JSON(http.StatusOK, vendors)
}

func getVendorByID(c *gin.Context) {
    id := c.Param("id")
    // Find Vendor by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Vendor"})
}

func createVendor(c *gin.Context) {
    var newVendor Vendor
    if err := c.BindJSON(&newVendor); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    vendors = append(vendors, newVendor)
    c.JSON(http.StatusCreated, newVendor)
}

func updateVendor(c *gin.Context) {
    id := c.Param("id")
    var updatedVendor Vendor
    if err := c.BindJSON(&updatedVendor); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedVendor)
}

func deleteVendor(c *gin.Context) {
    id := c.Param("id")
    // Delete Vendor
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/vendor", getAllVendors)
        api.GET("/vendor/:id", getVendorByID)
        api.POST("/vendor", createVendor)
        api.PUT("/vendor/:id", updateVendor)
        api.DELETE("/vendor/:id", deleteVendor)
    }

    r.Run(":8080")
}
