package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Product struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var products = []{name}{}

func getAllProducts(c *gin.Context) {
    c.JSON(http.StatusOK, products)
}

func getProductByID(c *gin.Context) {
    id := c.Param("id")
    // Find Product by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Product"})
}

func createProduct(c *gin.Context) {
    var newProduct Product
    if err := c.BindJSON(&newProduct); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    products = append(products, newProduct)
    c.JSON(http.StatusCreated, newProduct)
}

func updateProduct(c *gin.Context) {
    id := c.Param("id")
    var updatedProduct Product
    if err := c.BindJSON(&updatedProduct); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedProduct)
}

func deleteProduct(c *gin.Context) {
    id := c.Param("id")
    // Delete Product
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/product", getAllProducts)
        api.GET("/product/:id", getProductByID)
        api.POST("/product", createProduct)
        api.PUT("/product/:id", updateProduct)
        api.DELETE("/product/:id", deleteProduct)
    }

    r.Run(":8080")
}
