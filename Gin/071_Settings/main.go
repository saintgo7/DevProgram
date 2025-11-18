package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Settings struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var settingss = []{name}{}

func getAllSettingss(c *gin.Context) {
    c.JSON(http.StatusOK, settingss)
}

func getSettingsByID(c *gin.Context) {
    id := c.Param("id")
    // Find Settings by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Settings"})
}

func createSettings(c *gin.Context) {
    var newSettings Settings
    if err := c.BindJSON(&newSettings); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    settingss = append(settingss, newSettings)
    c.JSON(http.StatusCreated, newSettings)
}

func updateSettings(c *gin.Context) {
    id := c.Param("id")
    var updatedSettings Settings
    if err := c.BindJSON(&updatedSettings); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedSettings)
}

func deleteSettings(c *gin.Context) {
    id := c.Param("id")
    // Delete Settings
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/settings", getAllSettingss)
        api.GET("/settings/:id", getSettingsByID)
        api.POST("/settings", createSettings)
        api.PUT("/settings/:id", updateSettings)
        api.DELETE("/settings/:id", deleteSettings)
    }

    r.Run(":8080")
}
