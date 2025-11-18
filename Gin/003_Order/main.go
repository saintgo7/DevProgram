package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Order struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var orders = []{name}{}

func getAllOrders(c *gin.Context) {
    c.JSON(http.StatusOK, orders)
}

func getOrderByID(c *gin.Context) {
    id := c.Param("id")
    // Find Order by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Order"})
}

func createOrder(c *gin.Context) {
    var newOrder Order
    if err := c.BindJSON(&newOrder); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    orders = append(orders, newOrder)
    c.JSON(http.StatusCreated, newOrder)
}

func updateOrder(c *gin.Context) {
    id := c.Param("id")
    var updatedOrder Order
    if err := c.BindJSON(&updatedOrder); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedOrder)
}

func deleteOrder(c *gin.Context) {
    id := c.Param("id")
    // Delete Order
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/order", getAllOrders)
        api.GET("/order/:id", getOrderByID)
        api.POST("/order", createOrder)
        api.PUT("/order/:id", updateOrder)
        api.DELETE("/order/:id", deleteOrder)
    }

    r.Run(":8080")
}
