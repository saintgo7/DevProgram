package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Warehouse struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var warehouses = []{name}{}

func getAllWarehouses(c *gin.Context) {
    c.JSON(http.StatusOK, warehouses)
}

func getWarehouseByID(c *gin.Context) {
    id := c.Param("id")
    // Find Warehouse by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Warehouse"})
}

func createWarehouse(c *gin.Context) {
    var newWarehouse Warehouse
    if err := c.BindJSON(&newWarehouse); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    warehouses = append(warehouses, newWarehouse)
    c.JSON(http.StatusCreated, newWarehouse)
}

func updateWarehouse(c *gin.Context) {
    id := c.Param("id")
    var updatedWarehouse Warehouse
    if err := c.BindJSON(&updatedWarehouse); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedWarehouse)
}

func deleteWarehouse(c *gin.Context) {
    id := c.Param("id")
    // Delete Warehouse
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/warehouse", getAllWarehouses)
        api.GET("/warehouse/:id", getWarehouseByID)
        api.POST("/warehouse", createWarehouse)
        api.PUT("/warehouse/:id", updateWarehouse)
        api.DELETE("/warehouse/:id", deleteWarehouse)
    }

    r.Run(":8080")
}
