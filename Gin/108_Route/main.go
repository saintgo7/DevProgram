package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Route struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var routes = []{name}{}

func getAllRoutes(c *gin.Context) {
    c.JSON(http.StatusOK, routes)
}

func getRouteByID(c *gin.Context) {
    id := c.Param("id")
    // Find Route by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Route"})
}

func createRoute(c *gin.Context) {
    var newRoute Route
    if err := c.BindJSON(&newRoute); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    routes = append(routes, newRoute)
    c.JSON(http.StatusCreated, newRoute)
}

func updateRoute(c *gin.Context) {
    id := c.Param("id")
    var updatedRoute Route
    if err := c.BindJSON(&updatedRoute); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedRoute)
}

func deleteRoute(c *gin.Context) {
    id := c.Param("id")
    // Delete Route
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/route", getAllRoutes)
        api.GET("/route/:id", getRouteByID)
        api.POST("/route", createRoute)
        api.PUT("/route/:id", updateRoute)
        api.DELETE("/route/:id", deleteRoute)
    }

    r.Run(":8080")
}
