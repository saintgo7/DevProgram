package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type SMS struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var smss = []{name}{}

func getAllSMSs(c *gin.Context) {
    c.JSON(http.StatusOK, smss)
}

func getSMSByID(c *gin.Context) {
    id := c.Param("id")
    // Find SMS by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "SMS"})
}

func createSMS(c *gin.Context) {
    var newSMS SMS
    if err := c.BindJSON(&newSMS); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    smss = append(smss, newSMS)
    c.JSON(http.StatusCreated, newSMS)
}

func updateSMS(c *gin.Context) {
    id := c.Param("id")
    var updatedSMS SMS
    if err := c.BindJSON(&updatedSMS); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSMS)
}

func deleteSMS(c *gin.Context) {
    id := c.Param("id")
    // Delete SMS
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/sms", getAllSMSs)
        api.GET("/sms/:id", getSMSByID)
        api.POST("/sms", createSMS)
        api.PUT("/sms/:id", updateSMS)
        api.DELETE("/sms/:id", deleteSMS)
    }

    r.Run(":8080")
}
