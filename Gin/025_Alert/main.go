package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Alert struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var alerts = []{name}{}

func getAllAlerts(c *gin.Context) {
    c.JSON(http.StatusOK, alerts)
}

func getAlertByID(c *gin.Context) {
    id := c.Param("id")
    // Find Alert by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Alert"})
}

func createAlert(c *gin.Context) {
    var newAlert Alert
    if err := c.BindJSON(&newAlert); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    alerts = append(alerts, newAlert)
    c.JSON(http.StatusCreated, newAlert)
}

func updateAlert(c *gin.Context) {
    id := c.Param("id")
    var updatedAlert Alert
    if err := c.BindJSON(&updatedAlert); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAlert)
}

func deleteAlert(c *gin.Context) {
    id := c.Param("id")
    // Delete Alert
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/alert", getAllAlerts)
        api.GET("/alert/:id", getAlertByID)
        api.POST("/alert", createAlert)
        api.PUT("/alert/:id", updateAlert)
        api.DELETE("/alert/:id", deleteAlert)
    }

    r.Run(":8080")
}
