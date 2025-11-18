package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Export struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var exports = []{name}{}

func getAllExports(c *gin.Context) {
    c.JSON(http.StatusOK, exports)
}

func getExportByID(c *gin.Context) {
    id := c.Param("id")
    // Find Export by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Export"})
}

func createExport(c *gin.Context) {
    var newExport Export
    if err := c.BindJSON(&newExport); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    exports = append(exports, newExport)
    c.JSON(http.StatusCreated, newExport)
}

func updateExport(c *gin.Context) {
    id := c.Param("id")
    var updatedExport Export
    if err := c.BindJSON(&updatedExport); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedExport)
}

func deleteExport(c *gin.Context) {
    id := c.Param("id")
    // Delete Export
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/export", getAllExports)
        api.GET("/export/:id", getExportByID)
        api.POST("/export", createExport)
        api.PUT("/export/:id", updateExport)
        api.DELETE("/export/:id", deleteExport)
    }

    r.Run(":8080")
}
