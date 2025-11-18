package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Charge struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var charges = []{name}{}

func getAllCharges(c *gin.Context) {
    c.JSON(http.StatusOK, charges)
}

func getChargeByID(c *gin.Context) {
    id := c.Param("id")
    // Find Charge by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Charge"})
}

func createCharge(c *gin.Context) {
    var newCharge Charge
    if err := c.BindJSON(&newCharge); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    charges = append(charges, newCharge)
    c.JSON(http.StatusCreated, newCharge)
}

func updateCharge(c *gin.Context) {
    id := c.Param("id")
    var updatedCharge Charge
    if err := c.BindJSON(&updatedCharge); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedCharge)
}

func deleteCharge(c *gin.Context) {
    id := c.Param("id")
    // Delete Charge
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/charge", getAllCharges)
        api.GET("/charge/:id", getChargeByID)
        api.POST("/charge", createCharge)
        api.PUT("/charge/:id", updateCharge)
        api.DELETE("/charge/:id", deleteCharge)
    }

    r.Run(":8080")
}
