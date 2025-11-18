package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Supplier struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var suppliers = []{name}{}

func getAllSuppliers(c *gin.Context) {
    c.JSON(http.StatusOK, suppliers)
}

func getSupplierByID(c *gin.Context) {
    id := c.Param("id")
    // Find Supplier by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Supplier"})
}

func createSupplier(c *gin.Context) {
    var newSupplier Supplier
    if err := c.BindJSON(&newSupplier); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    suppliers = append(suppliers, newSupplier)
    c.JSON(http.StatusCreated, newSupplier)
}

func updateSupplier(c *gin.Context) {
    id := c.Param("id")
    var updatedSupplier Supplier
    if err := c.BindJSON(&updatedSupplier); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSupplier)
}

func deleteSupplier(c *gin.Context) {
    id := c.Param("id")
    // Delete Supplier
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/supplier", getAllSuppliers)
        api.GET("/supplier/:id", getSupplierByID)
        api.POST("/supplier", createSupplier)
        api.PUT("/supplier/:id", updateSupplier)
        api.DELETE("/supplier/:id", deleteSupplier)
    }

    r.Run(":8080")
}
