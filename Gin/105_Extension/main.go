package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Extension struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var extensions = []{name}{}

func getAllExtensions(c *gin.Context) {
    c.JSON(http.StatusOK, extensions)
}

func getExtensionByID(c *gin.Context) {
    id := c.Param("id")
    // Find Extension by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Extension"})
}

func createExtension(c *gin.Context) {
    var newExtension Extension
    if err := c.BindJSON(&newExtension); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    extensions = append(extensions, newExtension)
    c.JSON(http.StatusCreated, newExtension)
}

func updateExtension(c *gin.Context) {
    id := c.Param("id")
    var updatedExtension Extension
    if err := c.BindJSON(&updatedExtension); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedExtension)
}

func deleteExtension(c *gin.Context) {
    id := c.Param("id")
    // Delete Extension
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/extension", getAllExtensions)
        api.GET("/extension/:id", getExtensionByID)
        api.POST("/extension", createExtension)
        api.PUT("/extension/:id", updateExtension)
        api.DELETE("/extension/:id", deleteExtension)
    }

    r.Run(":8080")
}
