package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Permission struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var permissions = []{name}{}

func getAllPermissions(c *gin.Context) {
    c.JSON(http.StatusOK, permissions)
}

func getPermissionByID(c *gin.Context) {
    id := c.Param("id")
    // Find Permission by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Permission"})
}

func createPermission(c *gin.Context) {
    var newPermission Permission
    if err := c.BindJSON(&newPermission); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    permissions = append(permissions, newPermission)
    c.JSON(http.StatusCreated, newPermission)
}

func updatePermission(c *gin.Context) {
    id := c.Param("id")
    var updatedPermission Permission
    if err := c.BindJSON(&updatedPermission); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPermission)
}

func deletePermission(c *gin.Context) {
    id := c.Param("id")
    // Delete Permission
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/permission", getAllPermissions)
        api.GET("/permission/:id", getPermissionByID)
        api.POST("/permission", createPermission)
        api.PUT("/permission/:id", updatePermission)
        api.DELETE("/permission/:id", deletePermission)
    }

    r.Run(":8080")
}
