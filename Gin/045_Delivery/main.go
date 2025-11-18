package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Delivery struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var deliverys = []{name}{}

func getAllDeliverys(c *gin.Context) {
    c.JSON(http.StatusOK, deliverys)
}

func getDeliveryByID(c *gin.Context) {
    id := c.Param("id")
    // Find Delivery by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Delivery"})
}

func createDelivery(c *gin.Context) {
    var newDelivery Delivery
    if err := c.BindJSON(&newDelivery); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    deliverys = append(deliverys, newDelivery)
    c.JSON(http.StatusCreated, newDelivery)
}

func updateDelivery(c *gin.Context) {
    id := c.Param("id")
    var updatedDelivery Delivery
    if err := c.BindJSON(&updatedDelivery); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedDelivery)
}

func deleteDelivery(c *gin.Context) {
    id := c.Param("id")
    // Delete Delivery
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/delivery", getAllDeliverys)
        api.GET("/delivery/:id", getDeliveryByID)
        api.POST("/delivery", createDelivery)
        api.PUT("/delivery/:id", updateDelivery)
        api.DELETE("/delivery/:id", deleteDelivery)
    }

    r.Run(":8080")
}
