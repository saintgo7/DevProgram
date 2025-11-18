package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Plan struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var plans = []{name}{}

func getAllPlans(c *gin.Context) {
    c.JSON(http.StatusOK, plans)
}

func getPlanByID(c *gin.Context) {
    id := c.Param("id")
    // Find Plan by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Plan"})
}

func createPlan(c *gin.Context) {
    var newPlan Plan
    if err := c.BindJSON(&newPlan); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    plans = append(plans, newPlan)
    c.JSON(http.StatusCreated, newPlan)
}

func updatePlan(c *gin.Context) {
    id := c.Param("id")
    var updatedPlan Plan
    if err := c.BindJSON(&updatedPlan); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPlan)
}

func deletePlan(c *gin.Context) {
    id := c.Param("id")
    // Delete Plan
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/plan", getAllPlans)
        api.GET("/plan/:id", getPlanByID)
        api.POST("/plan", createPlan)
        api.PUT("/plan/:id", updatePlan)
        api.DELETE("/plan/:id", deletePlan)
    }

    r.Run(":8080")
}
