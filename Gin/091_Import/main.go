package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Import struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var imports = []{name}{}

func getAllImports(c *gin.Context) {
    c.JSON(http.StatusOK, imports)
}

func getImportByID(c *gin.Context) {
    id := c.Param("id")
    // Find Import by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Import"})
}

func createImport(c *gin.Context) {
    var newImport Import
    if err := c.BindJSON(&newImport); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    imports = append(imports, newImport)
    c.JSON(http.StatusCreated, newImport)
}

func updateImport(c *gin.Context) {
    id := c.Param("id")
    var updatedImport Import
    if err := c.BindJSON(&updatedImport); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedImport)
}

func deleteImport(c *gin.Context) {
    id := c.Param("id")
    // Delete Import
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/import", getAllImports)
        api.GET("/import/:id", getImportByID)
        api.POST("/import", createImport)
        api.PUT("/import/:id", updateImport)
        api.DELETE("/import/:id", deleteImport)
    }

    r.Run(":8080")
}
