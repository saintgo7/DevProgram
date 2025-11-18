package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Carrier struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var carriers = []{name}{}

func getAllCarriers(c *gin.Context) {
    c.JSON(http.StatusOK, carriers)
}

func getCarrierByID(c *gin.Context) {
    id := c.Param("id")
    // Find Carrier by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Carrier"})
}

func createCarrier(c *gin.Context) {
    var newCarrier Carrier
    if err := c.BindJSON(&newCarrier); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    carriers = append(carriers, newCarrier)
    c.JSON(http.StatusCreated, newCarrier)
}

func updateCarrier(c *gin.Context) {
    id := c.Param("id")
    var updatedCarrier Carrier
    if err := c.BindJSON(&updatedCarrier); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCarrier)
}

func deleteCarrier(c *gin.Context) {
    id := c.Param("id")
    // Delete Carrier
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/carrier", getAllCarriers)
        api.GET("/carrier/:id", getCarrierByID)
        api.POST("/carrier", createCarrier)
        api.PUT("/carrier/:id", updateCarrier)
        api.DELETE("/carrier/:id", deleteCarrier)
    }

    r.Run(":8080")
}
