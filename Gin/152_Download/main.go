package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Download struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var downloads = []{name}{}

func getAllDownloads(c *gin.Context) {
    c.JSON(http.StatusOK, downloads)
}

func getDownloadByID(c *gin.Context) {
    id := c.Param("id")
    // Find Download by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Download"})
}

func createDownload(c *gin.Context) {
    var newDownload Download
    if err := c.BindJSON(&newDownload); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    downloads = append(downloads, newDownload)
    c.JSON(http.StatusCreated, newDownload)
}

func updateDownload(c *gin.Context) {
    id := c.Param("id")
    var updatedDownload Download
    if err := c.BindJSON(&updatedDownload); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedDownload)
}

func deleteDownload(c *gin.Context) {
    id := c.Param("id")
    // Delete Download
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/download", getAllDownloads)
        api.GET("/download/:id", getDownloadByID)
        api.POST("/download", createDownload)
        api.PUT("/download/:id", updateDownload)
        api.DELETE("/download/:id", deleteDownload)
    }

    r.Run(":8080")
}
