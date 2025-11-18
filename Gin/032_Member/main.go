package main

import (
    "net/http"
    "github.com/gin-gonic/gin"
)

type Member struct {
    ID   uint   `json:"id"`
    Name string `json:"name"`
}

var members = []{name}{}

func getAllMembers(c *gin.Context) {
    c.JSON(http.StatusOK, members)
}

func getMemberByID(c *gin.Context) {
    id := c.Param("id")
    // Find Member by ID
    c.JSON(http.StatusOK, gin.H{"id": id, "name": "Member"})
}

func createMember(c *gin.Context) {
    var newMember Member
    if err := c.BindJSON(&newMember); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    members = append(members, newMember)
    c.JSON(http.StatusCreated, newMember)
}

func updateMember(c *gin.Context) {
    id := c.Param("id")
    var updatedMember Member
    if err := c.BindJSON(&updatedMember); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    c.JSON(http.StatusOK, updatedMember)
}

func deleteMember(c *gin.Context) {
    id := c.Param("id")
    // Delete Member
    c.JSON(http.StatusNoContent, nil)
}

func main() {
    r := gin.Default()

    api := r.Group("/api")
    {
        api.GET("/member", getAllMembers)
        api.GET("/member/:id", getMemberByID)
        api.POST("/member", createMember)
        api.PUT("/member/:id", updateMember)
        api.DELETE("/member/:id", deleteMember)
    }

    r.Run(":8080")
}
