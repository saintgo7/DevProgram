package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Refund struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var refunds = []{name}{}

func getAllRefunds(c *gin.Context) {
    c.JSON(http.StatusOK, refunds)
}

func getRefundByID(c *gin.Context) {
    id := c.Param("id")
    // Find Refund by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Refund"})
}

func createRefund(c *gin.Context) {
    var newRefund Refund
    if err := c.BindJSON(&newRefund); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    refunds = append(refunds, newRefund)
    c.JSON(http.StatusCreated, newRefund)
}

func updateRefund(c *gin.Context) {
    id := c.Param("id")
    var updatedRefund Refund
    if err := c.BindJSON(&updatedRefund); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedRefund)
}

func deleteRefund(c *gin.Context) {
    id := c.Param("id")
    // Delete Refund
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/refund", getAllRefunds)
        api.GET("/refund/:id", getRefundByID)
        api.POST("/refund", createRefund)
        api.PUT("/refund/:id", updateRefund)
        api.DELETE("/refund/:id", deleteRefund)
    }

    r.Run(":8080")
}
