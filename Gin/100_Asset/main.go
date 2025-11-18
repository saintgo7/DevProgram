package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Asset struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var assets = []{name}{}

func getAllAssets(c *gin.Context) {
    c.JSON(http.StatusOK, assets)
}

func getAssetByID(c *gin.Context) {
    id := c.Param("id")
    // Find Asset by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Asset"})
}

func createAsset(c *gin.Context) {
    var newAsset Asset
    if err := c.BindJSON(&newAsset); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    assets = append(assets, newAsset)
    c.JSON(http.StatusCreated, newAsset)
}

func updateAsset(c *gin.Context) {
    id := c.Param("id")
    var updatedAsset Asset
    if err := c.BindJSON(&updatedAsset); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedAsset)
}

func deleteAsset(c *gin.Context) {
    id := c.Param("id")
    // Delete Asset
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/asset", getAllAssets)
        api.GET("/asset/:id", getAssetByID)
        api.POST("/asset", createAsset)
        api.PUT("/asset/:id", updateAsset)
        api.DELETE("/asset/:id", deleteAsset)
    }

    r.Run(":8080")
}
