package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Team struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var teams = []{name}{}

func getAllTeams(c *gin.Context) {
    c.JSON(http.StatusOK, teams)
}

func getTeamByID(c *gin.Context) {
    id := c.Param("id")
    // Find Team by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Team"})
}

func createTeam(c *gin.Context) {
    var newTeam Team
    if err := c.BindJSON(&newTeam); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    teams = append(teams, newTeam)
    c.JSON(http.StatusCreated, newTeam)
}

func updateTeam(c *gin.Context) {
    id := c.Param("id")
    var updatedTeam Team
    if err := c.BindJSON(&updatedTeam); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedTeam)
}

func deleteTeam(c *gin.Context) {
    id := c.Param("id")
    // Delete Team
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/team", getAllTeams)
        api.GET("/team/:id", getTeamByID)
        api.POST("/team", createTeam)
        api.PUT("/team/:id", updateTeam)
        api.DELETE("/team/:id", deleteTeam)
    }

    r.Run(":8080")
}
