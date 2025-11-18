package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Upload struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var uploads = []{name}{}

func getAllUploads(c *gin.Context) {
    c.JSON(http.StatusOK, uploads)
}

func getUploadByID(c *gin.Context) {
    id := c.Param("id")
    // Find Upload by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Upload"})
}

func createUpload(c *gin.Context) {
    var newUpload Upload
    if err := c.BindJSON(&newUpload); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    uploads = append(uploads, newUpload)
    c.JSON(http.StatusCreated, newUpload)
}

func updateUpload(c *gin.Context) {
    id := c.Param("id")
    var updatedUpload Upload
    if err := c.BindJSON(&updatedUpload); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedUpload)
}

func deleteUpload(c *gin.Context) {
    id := c.Param("id")
    // Delete Upload
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/upload", getAllUploads)
        api.GET("/upload/:id", getUploadByID)
        api.POST("/upload", createUpload)
        api.PUT("/upload/:id", updateUpload)
        api.DELETE("/upload/:id", deleteUpload)
    }

    r.Run(":8080")
}
