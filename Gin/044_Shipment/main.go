package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Shipment struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var shipments = []{name}{}

func getAllShipments(c *gin.Context) {
    c.JSON(http.StatusOK, shipments)
}

func getShipmentByID(c *gin.Context) {
    id := c.Param("id")
    // Find Shipment by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Shipment"})
}

func createShipment(c *gin.Context) {
    var newShipment Shipment
    if err := c.BindJSON(&newShipment); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    shipments = append(shipments, newShipment)
    c.JSON(http.StatusCreated, newShipment)
}

func updateShipment(c *gin.Context) {
    id := c.Param("id")
    var updatedShipment Shipment
    if err := c.BindJSON(&updatedShipment); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedShipment)
}

func deleteShipment(c *gin.Context) {
    id := c.Param("id")
    // Delete Shipment
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/shipment", getAllShipments)
        api.GET("/shipment/:id", getShipmentByID)
        api.POST("/shipment", createShipment)
        api.PUT("/shipment/:id", updateShipment)
        api.DELETE("/shipment/:id", deleteShipment)
    }

    r.Run(":8080")
}
