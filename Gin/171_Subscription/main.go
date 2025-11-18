package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Subscription struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var subscriptions = []{name}{}

func getAllSubscriptions(c *gin.Context) {
    c.JSON(http.StatusOK, subscriptions)
}

func getSubscriptionByID(c *gin.Context) {
    id := c.Param("id")
    // Find Subscription by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Subscription"})
}

func createSubscription(c *gin.Context) {
    var newSubscription Subscription
    if err := c.BindJSON(&newSubscription); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    subscriptions = append(subscriptions, newSubscription)
    c.JSON(http.StatusCreated, newSubscription)
}

func updateSubscription(c *gin.Context) {
    id := c.Param("id")
    var updatedSubscription Subscription
    if err := c.BindJSON(&updatedSubscription); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSubscription)
}

func deleteSubscription(c *gin.Context) {
    id := c.Param("id")
    // Delete Subscription
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/subscription", getAllSubscriptions)
        api.GET("/subscription/:id", getSubscriptionByID)
        api.POST("/subscription", createSubscription)
        api.PUT("/subscription/:id", updateSubscription)
        api.DELETE("/subscription/:id", deleteSubscription)
    }

    r.Run(":8080")
}
