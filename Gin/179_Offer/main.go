package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Offer struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var offers = []{name}{}

func getAllOffers(c *gin.Context) {
    c.JSON(http.StatusOK, offers)
}

func getOfferByID(c *gin.Context) {
    id := c.Param("id")
    // Find Offer by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Offer"})
}

func createOffer(c *gin.Context) {
    var newOffer Offer
    if err := c.BindJSON(&newOffer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    offers = append(offers, newOffer)
    c.JSON(http.StatusCreated, newOffer)
}

func updateOffer(c *gin.Context) {
    id := c.Param("id")
    var updatedOffer Offer
    if err := c.BindJSON(&updatedOffer); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedOffer)
}

func deleteOffer(c *gin.Context) {
    id := c.Param("id")
    // Delete Offer
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/offer", getAllOffers)
        api.GET("/offer/:id", getOfferByID)
        api.POST("/offer", createOffer)
        api.PUT("/offer/:id", updateOffer)
        api.DELETE("/offer/:id", deleteOffer)
    }

    r.Run(":8080")
}
