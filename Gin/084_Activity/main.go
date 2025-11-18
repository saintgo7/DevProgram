package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Activity struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var activitys = []{name}{}

func getAllActivitys(c *gin.Context) {
    c.JSON(http.StatusOK, activitys)
}

func getActivityByID(c *gin.Context) {
    id := c.Param("id")
    // Find Activity by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Activity"})
}

func createActivity(c *gin.Context) {
    var newActivity Activity
    if err := c.BindJSON(&newActivity); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    activitys = append(activitys, newActivity)
    c.JSON(http.StatusCreated, newActivity)
}

func updateActivity(c *gin.Context) {
    id := c.Param("id")
    var updatedActivity Activity
    if err := c.BindJSON(&updatedActivity); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedActivity)
}

func deleteActivity(c *gin.Context) {
    id := c.Param("id")
    // Delete Activity
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/activity", getAllActivitys)
        api.GET("/activity/:id", getActivityByID)
        api.POST("/activity", createActivity)
        api.PUT("/activity/:id", updateActivity)
        api.DELETE("/activity/:id", deleteActivity)
    }

    r.Run(":8080")
}
