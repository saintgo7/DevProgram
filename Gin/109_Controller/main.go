package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Controller struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var controllers = []{name}{}

func getAllControllers(c *gin.Context) {
    c.JSON(http.StatusOK, controllers)
}

func getControllerByID(c *gin.Context) {
    id := c.Param("id")
    // Find Controller by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Controller"})
}

func createController(c *gin.Context) {
    var newController Controller
    if err := c.BindJSON(&newController); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    controllers = append(controllers, newController)
    c.JSON(http.StatusCreated, newController)
}

func updateController(c *gin.Context) {
    id := c.Param("id")
    var updatedController Controller
    if err := c.BindJSON(&updatedController); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedController)
}

func deleteController(c *gin.Context) {
    id := c.Param("id")
    // Delete Controller
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/controller", getAllControllers)
        api.GET("/controller/:id", getControllerByID)
        api.POST("/controller", createController)
        api.PUT("/controller/:id", updateController)
        api.DELETE("/controller/:id", deleteController)
    }

    r.Run(":8080")
}
