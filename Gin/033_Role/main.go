package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Role struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var roles = []{name}{}

func getAllRoles(c *gin.Context) {
    c.JSON(http.StatusOK, roles)
}

func getRoleByID(c *gin.Context) {
    id := c.Param("id")
    // Find Role by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Role"})
}

func createRole(c *gin.Context) {
    var newRole Role
    if err := c.BindJSON(&newRole); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    roles = append(roles, newRole)
    c.JSON(http.StatusCreated, newRole)
}

func updateRole(c *gin.Context) {
    id := c.Param("id")
    var updatedRole Role
    if err := c.BindJSON(&updatedRole); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedRole)
}

func deleteRole(c *gin.Context) {
    id := c.Param("id")
    // Delete Role
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/role", getAllRoles)
        api.GET("/role/:id", getRoleByID)
        api.POST("/role", createRole)
        api.PUT("/role/:id", updateRole)
        api.DELETE("/role/:id", deleteRole)
    }

    r.Run(":8080")
}
