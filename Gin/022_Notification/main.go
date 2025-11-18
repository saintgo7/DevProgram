package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Notification struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var notifications = []{name}{}

func getAllNotifications(c *gin.Context) {
    c.JSON(http.StatusOK, notifications)
}

func getNotificationByID(c *gin.Context) {
    id := c.Param("id")
    // Find Notification by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Notification"})
}

func createNotification(c *gin.Context) {
    var newNotification Notification
    if err := c.BindJSON(&newNotification); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    notifications = append(notifications, newNotification)
    c.JSON(http.StatusCreated, newNotification)
}

func updateNotification(c *gin.Context) {
    id := c.Param("id")
    var updatedNotification Notification
    if err := c.BindJSON(&updatedNotification); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedNotification)
}

func deleteNotification(c *gin.Context) {
    id := c.Param("id")
    // Delete Notification
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/notification", getAllNotifications)
        api.GET("/notification/:id", getNotificationByID)
        api.POST("/notification", createNotification)
        api.PUT("/notification/:id", updateNotification)
        api.DELETE("/notification/:id", deleteNotification)
    }

    r.Run(":8080")
}
