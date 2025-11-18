package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Promotion struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var promotions = []{name}{}

func getAllPromotions(c *gin.Context) {
    c.JSON(http.StatusOK, promotions)
}

func getPromotionByID(c *gin.Context) {
    id := c.Param("id")
    // Find Promotion by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Promotion"})
}

func createPromotion(c *gin.Context) {
    var newPromotion Promotion
    if err := c.BindJSON(&newPromotion); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    promotions = append(promotions, newPromotion)
    c.JSON(http.StatusCreated, newPromotion)
}

func updatePromotion(c *gin.Context) {
    id := c.Param("id")
    var updatedPromotion Promotion
    if err := c.BindJSON(&updatedPromotion); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPromotion)
}

func deletePromotion(c *gin.Context) {
    id := c.Param("id")
    // Delete Promotion
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/promotion", getAllPromotions)
        api.GET("/promotion/:id", getPromotionByID)
        api.POST("/promotion", createPromotion)
        api.PUT("/promotion/:id", updatePromotion)
        api.DELETE("/promotion/:id", deletePromotion)
    }

    r.Run(":8080")
}
