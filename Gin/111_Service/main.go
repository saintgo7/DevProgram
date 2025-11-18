package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Service struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var services = []{name}{}

func getAllServices(c *gin.Context) {
    c.JSON(http.StatusOK, services)
}

func getServiceByID(c *gin.Context) {
    id := c.Param("id")
    // Find Service by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Service"})
}

func createService(c *gin.Context) {
    var newService Service
    if err := c.BindJSON(&newService); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    services = append(services, newService)
    c.JSON(http.StatusCreated, newService)
}

func updateService(c *gin.Context) {
    id := c.Param("id")
    var updatedService Service
    if err := c.BindJSON(&updatedService); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedService)
}

func deleteService(c *gin.Context) {
    id := c.Param("id")
    // Delete Service
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/service", getAllServices)
        api.GET("/service/:id", getServiceByID)
        api.POST("/service", createService)
        api.PUT("/service/:id", updateService)
        api.DELETE("/service/:id", deleteService)
    }

    r.Run(":8080")
}
