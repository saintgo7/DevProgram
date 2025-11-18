package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type VAT struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var vats = []{name}{}

func getAllVATs(c *gin.Context) {
    c.JSON(http.StatusOK, vats)
}

func getVATByID(c *gin.Context) {
    id := c.Param("id")
    // Find VAT by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "VAT"})
}

func createVAT(c *gin.Context) {
    var newVAT VAT
    if err := c.BindJSON(&newVAT); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    vats = append(vats, newVAT)
    c.JSON(http.StatusCreated, newVAT)
}

func updateVAT(c *gin.Context) {
    id := c.Param("id")
    var updatedVAT VAT
    if err := c.BindJSON(&updatedVAT); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedVAT)
}

func deleteVAT(c *gin.Context) {
    id := c.Param("id")
    // Delete VAT
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/vat", getAllVATs)
        api.GET("/vat/:id", getVATByID)
        api.POST("/vat", createVAT)
        api.PUT("/vat/:id", updateVAT)
        api.DELETE("/vat/:id", deleteVAT)
    }

    r.Run(":8080")
}
