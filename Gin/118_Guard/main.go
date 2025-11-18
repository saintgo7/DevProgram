package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Guard struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var guards = []{name}{}

func getAllGuards(c *gin.Context) {
    c.JSON(http.StatusOK, guards)
}

func getGuardByID(c *gin.Context) {
    id := c.Param("id")
    // Find Guard by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Guard"})
}

func createGuard(c *gin.Context) {
    var newGuard Guard
    if err := c.BindJSON(&newGuard); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    guards = append(guards, newGuard)
    c.JSON(http.StatusCreated, newGuard)
}

func updateGuard(c *gin.Context) {
    id := c.Param("id")
    var updatedGuard Guard
    if err := c.BindJSON(&updatedGuard); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedGuard)
}

func deleteGuard(c *gin.Context) {
    id := c.Param("id")
    // Delete Guard
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/guard", getAllGuards)
        api.GET("/guard/:id", getGuardByID)
        api.POST("/guard", createGuard)
        api.PUT("/guard/:id", updateGuard)
        api.DELETE("/guard/:id", deleteGuard)
    }

    r.Run(":8080")
}
