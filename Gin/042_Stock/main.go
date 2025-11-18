package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Stock struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var stocks = []{name}{}

func getAllStocks(c *gin.Context) {
    c.JSON(http.StatusOK, stocks)
}

func getStockByID(c *gin.Context) {
    id := c.Param("id")
    // Find Stock by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Stock"})
}

func createStock(c *gin.Context) {
    var newStock Stock
    if err := c.BindJSON(&newStock); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    stocks = append(stocks, newStock)
    c.JSON(http.StatusCreated, newStock)
}

func updateStock(c *gin.Context) {
    id := c.Param("id")
    var updatedStock Stock
    if err := c.BindJSON(&updatedStock); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedStock)
}

func deleteStock(c *gin.Context) {
    id := c.Param("id")
    // Delete Stock
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/stock", getAllStocks)
        api.GET("/stock/:id", getStockByID)
        api.POST("/stock", createStock)
        api.PUT("/stock/:id", updateStock)
        api.DELETE("/stock/:id", deleteStock)
    }

    r.Run(":8080")
}
