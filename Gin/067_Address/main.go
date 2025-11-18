package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Address struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var addresss = []{name}{}

func getAllAddresss(c *gin.Context) {
    c.JSON(http.StatusOK, addresss)
}

func getAddressByID(c *gin.Context) {
    id := c.Param("id")
    // Find Address by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Address"})
}

func createAddress(c *gin.Context) {
    var newAddress Address
    if err := c.BindJSON(&newAddress); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    addresss = append(addresss, newAddress)
    c.JSON(http.StatusCreated, newAddress)
}

func updateAddress(c *gin.Context) {
    id := c.Param("id")
    var updatedAddress Address
    if err := c.BindJSON(&updatedAddress); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAddress)
}

func deleteAddress(c *gin.Context) {
    id := c.Param("id")
    // Delete Address
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/address", getAllAddresss)
        api.GET("/address/:id", getAddressByID)
        api.POST("/address", createAddress)
        api.PUT("/address/:id", updateAddress)
        api.DELETE("/address/:id", deleteAddress)
    }

    r.Run(":8080")
}
