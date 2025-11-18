package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Retailer struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var retailers = []{name}{}

func getAllRetailers(c *gin.Context) {
    c.JSON(http.StatusOK, retailers)
}

func getRetailerByID(c *gin.Context) {
    id := c.Param("id")
    // Find Retailer by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Retailer"})
}

func createRetailer(c *gin.Context) {
    var newRetailer Retailer
    if err := c.BindJSON(&newRetailer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    retailers = append(retailers, newRetailer)
    c.JSON(http.StatusCreated, newRetailer)
}

func updateRetailer(c *gin.Context) {
    id := c.Param("id")
    var updatedRetailer Retailer
    if err := c.BindJSON(&updatedRetailer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedRetailer)
}

func deleteRetailer(c *gin.Context) {
    id := c.Param("id")
    // Delete Retailer
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/retailer", getAllRetailers)
        api.GET("/retailer/:id", getRetailerByID)
        api.POST("/retailer", createRetailer)
        api.PUT("/retailer/:id", updateRetailer)
        api.DELETE("/retailer/:id", deleteRetailer)
    }

    r.Run(":8080")
}
