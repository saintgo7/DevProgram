package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Distributor struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var distributors = []{name}{}

func getAllDistributors(c *gin.Context) {
    c.JSON(http.StatusOK, distributors)
}

func getDistributorByID(c *gin.Context) {
    id := c.Param("id")
    // Find Distributor by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Distributor"})
}

func createDistributor(c *gin.Context) {
    var newDistributor Distributor
    if err := c.BindJSON(&newDistributor); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    distributors = append(distributors, newDistributor)
    c.JSON(http.StatusCreated, newDistributor)
}

func updateDistributor(c *gin.Context) {
    id := c.Param("id")
    var updatedDistributor Distributor
    if err := c.BindJSON(&updatedDistributor); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedDistributor)
}

func deleteDistributor(c *gin.Context) {
    id := c.Param("id")
    // Delete Distributor
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/distributor", getAllDistributors)
        api.GET("/distributor/:id", getDistributorByID)
        api.POST("/distributor", createDistributor)
        api.PUT("/distributor/:id", updateDistributor)
        api.DELETE("/distributor/:id", deleteDistributor)
    }

    r.Run(":8080")
}
