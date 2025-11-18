package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type GST struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var gsts = []{name}{}

func getAllGSTs(c *gin.Context) {
    c.JSON(http.StatusOK, gsts)
}

func getGSTByID(c *gin.Context) {
    id := c.Param("id")
    // Find GST by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "GST"})
}

func createGST(c *gin.Context) {
    var newGST GST
    if err := c.BindJSON(&newGST); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    gsts = append(gsts, newGST)
    c.JSON(http.StatusCreated, newGST)
}

func updateGST(c *gin.Context) {
    id := c.Param("id")
    var updatedGST GST
    if err := c.BindJSON(&updatedGST); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedGST)
}

func deleteGST(c *gin.Context) {
    id := c.Param("id")
    // Delete GST
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/gst", getAllGSTs)
        api.GET("/gst/:id", getGSTByID)
        api.POST("/gst", createGST)
        api.PUT("/gst/:id", updateGST)
        api.DELETE("/gst/:id", deleteGST)
    }

    r.Run(":8080")
}
