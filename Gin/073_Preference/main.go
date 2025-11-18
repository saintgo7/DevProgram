package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Preference struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var preferences = []{name}{}

func getAllPreferences(c *gin.Context) {
    c.JSON(http.StatusOK, preferences)
}

func getPreferenceByID(c *gin.Context) {
    id := c.Param("id")
    // Find Preference by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Preference"})
}

func createPreference(c *gin.Context) {
    var newPreference Preference
    if err := c.BindJSON(&newPreference); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    preferences = append(preferences, newPreference)
    c.JSON(http.StatusCreated, newPreference)
}

func updatePreference(c *gin.Context) {
    id := c.Param("id")
    var updatedPreference Preference
    if err := c.BindJSON(&updatedPreference); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedPreference)
}

func deletePreference(c *gin.Context) {
    id := c.Param("id")
    // Delete Preference
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/preference", getAllPreferences)
        api.GET("/preference/:id", getPreferenceByID)
        api.POST("/preference", createPreference)
        api.PUT("/preference/:id", updatePreference)
        api.DELETE("/preference/:id", deletePreference)
    }

    r.Run(":8080")
}
