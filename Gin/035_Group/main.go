package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Group struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var groups = []{name}{}

func getAllGroups(c *gin.Context) {
    c.JSON(http.StatusOK, groups)
}

func getGroupByID(c *gin.Context) {
    id := c.Param("id")
    // Find Group by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Group"})
}

func createGroup(c *gin.Context) {
    var newGroup Group
    if err := c.BindJSON(&newGroup); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    groups = append(groups, newGroup)
    c.JSON(http.StatusCreated, newGroup)
}

func updateGroup(c *gin.Context) {
    id := c.Param("id")
    var updatedGroup Group
    if err := c.BindJSON(&updatedGroup); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedGroup)
}

func deleteGroup(c *gin.Context) {
    id := c.Param("id")
    // Delete Group
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/group", getAllGroups)
        api.GET("/group/:id", getGroupByID)
        api.POST("/group", createGroup)
        api.PUT("/group/:id", updateGroup)
        api.DELETE("/group/:id", deleteGroup)
    }

    r.Run(":8080")
}
