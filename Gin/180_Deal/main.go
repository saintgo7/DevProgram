package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Deal struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var deals = []{name}{}

func getAllDeals(c *gin.Context) {
    c.JSON(http.StatusOK, deals)
}

func getDealByID(c *gin.Context) {
    id := c.Param("id")
    // Find Deal by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Deal"})
}

func createDeal(c *gin.Context) {
    var newDeal Deal
    if err := c.BindJSON(&newDeal); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    deals = append(deals, newDeal)
    c.JSON(http.StatusCreated, newDeal)
}

func updateDeal(c *gin.Context) {
    id := c.Param("id")
    var updatedDeal Deal
    if err := c.BindJSON(&updatedDeal); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedDeal)
}

func deleteDeal(c *gin.Context) {
    id := c.Param("id")
    // Delete Deal
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/deal", getAllDeals)
        api.GET("/deal/:id", getDealByID)
        api.POST("/deal", createDeal)
        api.PUT("/deal/:id", updateDeal)
        api.DELETE("/deal/:id", deleteDeal)
    }

    r.Run(":8080")
}
