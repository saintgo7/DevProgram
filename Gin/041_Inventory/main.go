package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Inventory struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var inventorys = []{name}{}

func getAllInventorys(c *gin.Context) {
    c.JSON(http.StatusOK, inventorys)
}

func getInventoryByID(c *gin.Context) {
    id := c.Param("id")
    // Find Inventory by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Inventory"})
}

func createInventory(c *gin.Context) {
    var newInventory Inventory
    if err := c.BindJSON(&newInventory); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    inventorys = append(inventorys, newInventory)
    c.JSON(http.StatusCreated, newInventory)
}

func updateInventory(c *gin.Context) {
    id := c.Param("id")
    var updatedInventory Inventory
    if err := c.BindJSON(&updatedInventory); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedInventory)
}

func deleteInventory(c *gin.Context) {
    id := c.Param("id")
    // Delete Inventory
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/inventory", getAllInventorys)
        api.GET("/inventory/:id", getInventoryByID)
        api.POST("/inventory", createInventory)
        api.PUT("/inventory/:id", updateInventory)
        api.DELETE("/inventory/:id", deleteInventory)
    }

    r.Run(":8080")
}
