package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type File struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var files = []{name}{}

func getAllFiles(c *gin.Context) {
    c.JSON(http.StatusOK, files)
}

func getFileByID(c *gin.Context) {
    id := c.Param("id")
    // Find File by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "File"})
}

func createFile(c *gin.Context) {
    var newFile File
    if err := c.BindJSON(&newFile); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    files = append(files, newFile)
    c.JSON(http.StatusCreated, newFile)
}

func updateFile(c *gin.Context) {
    id := c.Param("id")
    var updatedFile File
    if err := c.BindJSON(&updatedFile); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedFile)
}

func deleteFile(c *gin.Context) {
    id := c.Param("id")
    // Delete File
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/file", getAllFiles)
        api.GET("/file/:id", getFileByID)
        api.POST("/file", createFile)
        api.PUT("/file/:id", updateFile)
        api.DELETE("/file/:id", deleteFile)
    }

    r.Run(":8080")
}
